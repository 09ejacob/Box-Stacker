# stacker.py

import json
import random
from box import Box

class Stacker:
    def __init__(self,
                 pallet_size=(0.8, 1.2, 0.144),   # (width, length, height)
                 pallet_color=(0.6, 0.6, 0.6, 1.0),
                 allow_rotation=True):
        # unpack pallet dimensions
        self.pw, self.pl, self.ph = pallet_size
        self.allow_rotation = allow_rotation

        # start with the pallet itself in the scene
        self.boxes = [
            Box(
                center=(0, self.ph/2, 0),
                size=(self.pw, self.pl, self.ph),
                color=pallet_color
            )
        ]

        # this will come from JSON
        self.items = []

    def load_from_file(self, path):
        with open(path, 'r') as f:
            self.items = json.load(f)  # expects [{"size":[w,l,h],"count":N}, ...]

    def stack(self):
        # 1) turn each spec into N individual (w,l,h) tuples
        todo = []
        for it in self.items:
            w, l, h = it['size']
            cnt = it.get('count', 1)
            todo += [(w, l, h)] * cnt

        # 2) sort by footprint area, big first (helps corners/edges)
        todo.sort(key=lambda b: b[0] * b[1], reverse=True)

        # 3) we’ll do just one layer at height = pallet top
        layer_y = self.ph

        # 4) track free rectangles on that layer
        #    each rect is (x0, z0, width, length), measured from pallet center
        free = [(-self.pw/2, -self.pl/2, self.pw, self.pl)]

        # 5) place each box in turn (first‐fit *best* free‐rect)
        for w, l, h in todo:
            placed = False
            # try both orientations if allowed
            for rotated in (False, True) if self.allow_rotation else (False,):
                rw, rl = (l, w) if rotated else (w, l)

                # scan free rects for one it fits
                for i, (x0, z0, fw, fl) in enumerate(free):
                    if rw <= fw and rl <= fl:
                        # compute center position
                        x = x0 + rw/2
                        z = z0 + rl/2
                        y = layer_y + h/2

                        # add it (semi-transparent random color)
                        color = (random.random(), random.random(), random.random(), 0.5)
                        self.boxes.append(Box((x, y, z), (w, l, h), color))

                        # remove this free rect
                        free.pop(i)
                        # carve out two new rects: right & top
                        right = (x0 + rw, z0,     fw - rw, rl)
                        top   = (x0,     z0 + rl, fw,      fl - rl)
                        for nr in (right, top):
                            if nr[2] > 1e-6 and nr[3] > 1e-6:
                                free.append(nr)

                        placed = True
                        break
                if placed:
                    break
            # if it didn’t fit anywhere, it’s skipped for now
