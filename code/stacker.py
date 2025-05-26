import json
import random
from box import Box

class Stacker:
    def __init__(self,
                 pallet_size=(0.8, 1.2, 0.144),
                 pallet_color=(0.6, 0.6, 0.6, 1.0)):
        self.pallet_size = pallet_size
        pw, pl, ph = pallet_size

        self.boxes = [Box((0, ph/2, 0), pallet_size, pallet_color)]
        self.items  = []

    def load_from_file(self, path):
        with open(path, 'r') as f:
            self.items = json.load(f)

    def stack(self):
        pw, pl, ph = self.pallet_size
        todo = []
        for it in self.items:
            w, l, h = it['size']
            cnt = it.get('count', 1)
            todo += [(w, l, h)] * cnt

        todo.sort(key=lambda b: b[0] * b[1], reverse=True)

        layer_y   = ph
        remaining = todo[:]

        while remaining:
            free_rects    = [(-pw/2, -pl/2, pw, pl)]
            placed_heights = []

            while True:
                best = None
                for idx, (w, l, h) in enumerate(remaining):
                    for rect in free_rects:
                        x0, z0, rw, rl = rect
                        if w <= rw and l <= rl:
                            leftover = (rw*rl) - (w*l)
                            if best is None or leftover < best[0]:
                                best = (leftover, idx, rect, w, l, h)
                if not best:
                    break

                _, idx, rect, w, l, h = best
                x0, z0, rw, rl = rect

                x = x0 + w/2
                z = z0 + l/2
                y = layer_y + h/2

                color = (random.random(), random.random(), random.random(), 0.5)
                self.boxes.append(Box((x, y, z), (w, l, h), color))
                placed_heights.append(h)

                free_rects.remove(rect)
                right = (x0 + w, z0,      rw - w, l)
                top   = (x0,     z0 + l,  rw,     rl - l)
                for nr in (right, top):
                    if nr[2] > 1e-6 and nr[3] > 1e-6:
                        free_rects.append(nr)

                remaining.pop(idx)

            if not placed_heights:
                break

            layer_y += max(placed_heights)
