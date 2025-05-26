# main.py
import pyglet
import viewer
from stacker import Stacker

# main.py
if __name__ == '__main__':
    st = Stacker()
    st.load_from_file('boxes/boxes.json')   # <-- no “..”
    st.stack()
    viewer.boxes = st.boxes
    pyglet.app.run()
