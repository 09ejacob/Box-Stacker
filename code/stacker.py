# stacker.py
import json
import random
from box import Box

class Stacker:
    def __init__(self, pallet_size=(0.8, 0.144, 1.2), pallet_color=(0.6,0.6,0.6,1.0), spacing=0.01):
        px, ph, pz = pallet_size
        self.boxes = [ Box((0, ph/2, 0), pallet_size, pallet_color) ]
        self.spacing = spacing
        self.items = []

    def load_from_file(self, path):
        with open(path, 'r') as f:
            self.items = json.load(f)

    def stack(self):
        pallet = self.boxes[0]
        pw, ph, pd = pallet.w, pallet.h, pallet.d
        base_y = ph

        for item in self.items:
            w, h, d = item['size']
            count = item.get('count', 1)

            per_x = max(int((pw + self.spacing) // (w + self.spacing)), 1)
            per_z = max(int((pd + self.spacing) // (d + self.spacing)), 1)
            puts = min(count, per_x * per_z)

            for i in range(puts):
                ix = i % per_x
                iz = i // per_x

                x = -pw/2 + w/2 + ix * (w + self.spacing)
                z = -pd/2 + d/2 + iz * (d + self.spacing)
                y = base_y + h/2

                color = (random.random(), random.random(), random.random(), 0.8)
                self.boxes.append(Box((x, y, z), (w, h, d), color))
