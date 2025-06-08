from OpenGL.GL import *


def draw_path(path_points, size=40):
    glColor4f(1, 0, 0, 0.3)
    for x, y in path_points:
        glBegin(GL_QUADS)
        glVertex2f(x - size / 2, y - size / 2)
        glVertex2f(x + size / 2, y - size / 2)
        glVertex2f(x + size / 2, y + size / 2)
        glVertex2f(x - size / 2, y + size / 2)
        glEnd()
