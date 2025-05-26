import pyglet
from pyglet.gl import (
    glViewport, glMatrixMode, glLoadIdentity,
    glEnable, glTranslatef, glRotatef, glPushMatrix, glPopMatrix,
    glScalef, glBegin, glEnd, glVertex3f,
    GL_PROJECTION, GL_MODELVIEW, GL_DEPTH_TEST, GL_QUADS,
    gluPerspective
)

# --- define a Box by center + size, and draw with GL_QUADS ---
class Box:
    def __init__(self, center, size):
        self.x, self.y, self.z = center
        self.w, self.h, self.d = size

    def draw(self):
        glPushMatrix()
        glTranslatef(self.x, self.y, self.z)
        glScalef(self.w, self.h, self.d)
        glBegin(GL_QUADS)

        # front
        glVertex3f(-0.5, -0.5,  0.5)
        glVertex3f( 0.5, -0.5,  0.5)
        glVertex3f( 0.5,  0.5,  0.5)
        glVertex3f(-0.5,  0.5,  0.5)

        # back
        glVertex3f(-0.5, -0.5, -0.5)
        glVertex3f(-0.5,  0.5, -0.5)
        glVertex3f( 0.5,  0.5, -0.5)
        glVertex3f( 0.5, -0.5, -0.5)

        # left
        glVertex3f(-0.5, -0.5, -0.5)
        glVertex3f(-0.5, -0.5,  0.5)
        glVertex3f(-0.5,  0.5,  0.5)
        glVertex3f(-0.5,  0.5, -0.5)

        # right
        glVertex3f( 0.5, -0.5, -0.5)
        glVertex3f( 0.5,  0.5, -0.5)
        glVertex3f( 0.5,  0.5,  0.5)
        glVertex3f( 0.5, -0.5,  0.5)

        # top
        glVertex3f(-0.5,  0.5, -0.5)
        glVertex3f(-0.5,  0.5,  0.5)
        glVertex3f( 0.5,  0.5,  0.5)
        glVertex3f( 0.5,  0.5, -0.5)

        # bottom
        glVertex3f(-0.5, -0.5, -0.5)
        glVertex3f( 0.5, -0.5, -0.5)
        glVertex3f( 0.5, -0.5,  0.5)
        glVertex3f(-0.5, -0.5,  0.5)
        
        glEnd()
        glPopMatrix()

boxes = [
    Box(center=(0, 0, 0),   size=(1, 1, 1)),
    Box(center=(2, 0, 0),   size=(0.5, 2, 0.5)),
    Box(center=(0, 2, -1),  size=(1, 0.5, 2)),
]

# --- window + camera state ---
window = pyglet.window.Window(800, 600, "3D view", resizable=True)
yaw = 30
pitch = -20
dist = 8.0
pan_x = pan_y = 0.0

@window.event
def on_resize(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60.0, width/float(height), 0.1, 1000.0)
    glMatrixMode(GL_MODELVIEW)
    return True

@window.event
def on_draw():
    window.clear()
    glEnable(GL_DEPTH_TEST)
    glLoadIdentity()

    glTranslatef(pan_x, pan_y, -dist)
    glRotatef(-pitch, 1, 0, 0)
    glRotatef(yaw,   0, 1, 0)

    for b in boxes:
        b.draw()

@window.event
def on_mouse_drag(x, y, dx, dy, buttons, mods):
    global yaw, pitch, pan_x, pan_y

    if buttons & pyglet.window.mouse.LEFT:
        yaw   += dx * 0.3
        pitch += dy * 0.3

    elif buttons & (pyglet.window.mouse.RIGHT | pyglet.window.mouse.MIDDLE):
        pan_x += dx * (dist / window.width)
        pan_y += dy * (dist / window.height)

@window.event
def on_mouse_scroll(x, y, scroll_x, scroll_y):
    global dist
    dist = max(1.0, dist - scroll_y * 0.5)

if __name__ == '__main__':
    pyglet.app.run()
