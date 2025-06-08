from OpenGL.GL import *

# Mapeamento bem simples só para os números 0–9 com retângulos verticais/horizontais
number_segments = {
    '0': [(0,0), (1,0), (1,2), (0,2), (0,0)],
    '1': [(0.5,0), (0.5,2)],
    '2': [(0,2), (1,2), (1,1), (0,1), (0,0), (1,0)],
    '3': [(0,2), (1,2), (0.5,1), (1,1), (0.5,0), (1,0)],
    '4': [(0,2), (0,1), (1,1), (1,2), (1,0)],
    '5': [(1,2), (0,2), (0,1), (1,1), (1,0), (0,0)],
    '6': [(1,2), (0,2), (0,0), (1,0), (1,1), (0,1)],
    '7': [(0,2), (1,2), (0.5,0)],
    '8': [(0,0), (1,0), (1,2), (0,2), (0,0), (0,1), (1,1)],
    '9': [(1,0), (1,2), (0,2), (0,1), (1,1)],
}

def draw_digit(x, y, digit, scale=5):
    glBegin(GL_LINE_STRIP)
    for dx, dy in number_segments.get(digit, []):
        glVertex2f(x + dx * scale, y - dy * scale)
    glEnd()
