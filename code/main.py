from box import Box
import viewer
import pyglet

boxes = [
    Box((0,0,0), (0.8,0.144,1.2), (1,0,0,0.6)), # Default pallet
]

viewer.boxes = boxes

if __name__ == '__main__':
    pyglet.app.run()
