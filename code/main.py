import pyglet
import viewer
from stacker import Stacker

if __name__ == '__main__':
    st = Stacker()
    
    st.load_from_file('boxes/boxes.json')
    st.stack()
    
    viewer.boxes = st.boxes

    pyglet.app.run()
