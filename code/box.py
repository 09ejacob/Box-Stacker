import pyglet
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

class Box:
    def __init__(self, center, size, color=(1,1,1,0.5)):
        self.x, self.y, self.z = center
        self.w, self.h, self.d = size
        self.r, self.g, self.b, self.a = color

    def draw(self):
        glColor4f(self.r, self.g, self.b, self.a)
        glPushMatrix()
        glTranslatef(self.x, self.y, self.z)
        glScalef(self.w, self.h, self.d)
        glBegin(GL_QUADS)

        # front
        glNormal3f(0, 0, 1)
        glVertex3f(-.5, -.5,  .5)
        glVertex3f( .5, -.5,  .5)
        glVertex3f( .5,  .5,  .5)
        glVertex3f(-.5,  .5,  .5)

        # back
        glNormal3f(0, 0, -1)
        glVertex3f(-.5, -.5, -.5)
        glVertex3f(-.5,  .5, -.5)
        glVertex3f( .5,  .5, -.5)
        glVertex3f( .5, -.5, -.5)

        # left
        glNormal3f(-1, 0, 0)
        glVertex3f(-.5, -.5, -.5)
        glVertex3f(-.5, -.5,  .5)
        glVertex3f(-.5,  .5,  .5)
        glVertex3f(-.5,  .5, -.5)

        # right
        glNormal3f(1, 0, 0)
        glVertex3f( .5, -.5, -.5)
        glVertex3f( .5,  .5, -.5)
        glVertex3f( .5,  .5,  .5)
        glVertex3f( .5, -.5,  .5)

        # top
        glNormal3f(0, 1, 0)
        glVertex3f(-.5,  .5, -.5)
        glVertex3f(-.5,  .5,  .5)
        glVertex3f( .5,  .5,  .5)
        glVertex3f( .5,  .5, -.5)
        
        # bottom
        glNormal3f(0, -1, 0)
        glVertex3f(-.5, -.5, -.5)
        glVertex3f( .5, -.5, -.5)
        glVertex3f( .5, -.5,  .5)
        glVertex3f(-.5, -.5,  .5)
        
        glEnd()
        glPopMatrix()
