import pyglet
from pyglet.gl import GLfloat
from pyglet.gl import (
    glViewport, glMatrixMode, glLoadIdentity,
    glEnable, glBlendFunc, glLightfv, glColor4f, glNormal3f,
    glTranslatef, glRotatef, glPushMatrix, glPopMatrix,
    glScalef, glBegin, glEnd, glVertex3f,
    GL_PROJECTION, GL_MODELVIEW, GL_DEPTH_TEST, GL_BLEND,
    GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA,
    GL_LIGHTING, GL_LIGHT0, GL_POSITION,
    GL_QUADS, gluPerspective
)
from box import Box

boxes = [
]

window = pyglet.window.Window(800, 600, "3D view", resizable=True)
yaw = 30; pitch = -20; dist = 8.0; pan_x = pan_y = 0.0

@window.event
def on_resize(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION); glLoadIdentity()
    gluPerspective(20.0, width/float(height), 0.1, 1000.0)
    glMatrixMode(GL_MODELVIEW)
    return True

@window.event
def on_draw():
    window.clear()
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_BLEND); glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glEnable(GL_LIGHTING); glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, (GLfloat * 4)(1.0, 1.0, 1.0, 0.0))
    glLoadIdentity()
    glTranslatef(pan_x, pan_y, -dist)
    glRotatef(-pitch, 1, 0, 0); glRotatef(yaw, 0, 1, 0)

    for b in boxes:
        b.draw()

@window.event
def on_mouse_drag(x, y, dx, dy, buttons, mods):
    global yaw, pitch, pan_x, pan_y
    if buttons & pyglet.window.mouse.LEFT:
        yaw   += dx * 0.3; pitch += dy * 0.3
    else:
        pan_x += dx * (dist/window.width); pan_y += dy * (dist/window.height)

@window.event
def on_mouse_scroll(x, y, sx, sy):
    global dist; dist = max(1.0, dist - sy * 0.5)

if __name__ == '__main__':
    pyglet.app.run()
