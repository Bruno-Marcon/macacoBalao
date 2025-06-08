from PIL import ImageFont, ImageDraw, Image
import numpy as np
from OpenGL.GL import *

def draw_text(text, x, y, size=16):
    font = ImageFont.truetype("arial.ttf", size)
    img = Image.new("RGBA", (400, 50), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.text((0, 0), text, font=font, fill=(255, 255, 255, 255))

    img_data = np.array(img)
    img_data = np.flipud(img_data)

    glRasterPos2f(x, y)
    glDrawPixels(img.width, img.height, GL_RGBA, GL_UNSIGNED_BYTE, img_data)

def draw_stroke_text(text, x, y, scale=0.1):
    glPushMatrix()
    glTranslatef(x, y, 0)
    glScalef(scale, scale, scale)
    for c in text:
        glutStrokeCharacter(GLUT_STROKE_ROMAN, ord(c))
    glPopMatrix()
