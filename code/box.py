import pyglet
from pyglet.gl import (
    glEnable, glBlendFunc, glColor4f, glNormal3f,
    glPushMatrix, glTranslatef, glScalef, glBegin, glVertex3f, glEnd, glPopMatrix,
    GL_QUADS, GL_DEPTH_TEST, GL_BLEND, GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA
)

class Box:
    def __init__(self, center, size, color=(1,1,1,0.5)):
        self.x, self.y, self.z = center
        self.w, self.l, self.h = size
        self.r, self.g, self.b, self.a = color

    def draw(self):
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        glColor4f(self.r, self.g, self.b, self.a)
        glPushMatrix()
        glTranslatef(self.x, self.y, self.z)

        glScalef(self.w, self.h, self.l)

        glBegin(GL_QUADS)
        # front  (+Z)
        glNormal3f(0, 0, 1)
        glVertex3f(-0.5, -0.5,  0.5)
        glVertex3f( 0.5, -0.5,  0.5)
        glVertex3f( 0.5,  0.5,  0.5)
        glVertex3f(-0.5,  0.5,  0.5)
        # back   (–Z)
        glNormal3f(0, 0, -1)
        glVertex3f(-0.5, -0.5, -0.5)
        glVertex3f(-0.5,  0.5, -0.5)
        glVertex3f( 0.5,  0.5, -0.5)
        glVertex3f( 0.5, -0.5, -0.5)
        # left   (–X)
        glNormal3f(-1, 0, 0)
        glVertex3f(-0.5, -0.5, -0.5)
        glVertex3f(-0.5, -0.5,  0.5)
        glVertex3f(-0.5,  0.5,  0.5)
        glVertex3f(-0.5,  0.5, -0.5)
        # right  (+X)
        glNormal3f(1, 0, 0)
        glVertex3f( 0.5, -0.5, -0.5)
        glVertex3f( 0.5,  0.5, -0.5)
        glVertex3f( 0.5,  0.5,  0.5)
        glVertex3f( 0.5, -0.5,  0.5)
        # top    (+Y)
        glNormal3f(0, 1, 0)
        glVertex3f(-0.5,  0.5, -0.5)
        glVertex3f(-0.5,  0.5,  0.5)
        glVertex3f( 0.5,  0.5,  0.5)
        glVertex3f( 0.5,  0.5, -0.5)
        # bottom (–Y)
        glNormal3f(0, -1, 0)
        glVertex3f(-0.5, -0.5, -0.5)
        glVertex3f( 0.5, -0.5, -0.5)
        glVertex3f( 0.5, -0.5,  0.5)
        glVertex3f(-0.5, -0.5,  0.5)
        glEnd()

        glPopMatrix()
