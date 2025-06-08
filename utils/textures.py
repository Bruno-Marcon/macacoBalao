# utils/textures.py
from OpenGL.GL import *
from PIL import Image, ImageFont, ImageDraw
import numpy as np

def load_texture(path, max_size=None):
    image = Image.open(path).convert("RGBA")

    if max_size:
        image.thumbnail(max_size, Image.ANTIALIAS)

    image_data = image.tobytes("raw", "RGBA", 0, -1)
    width, height = image.size

    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)

    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0,
                 GL_RGBA, GL_UNSIGNED_BYTE, image_data)

    glBindTexture(GL_TEXTURE_2D, 0)
    return texture_id, width, height


def render_text(text, x, y, size=16):
    font = ImageFont.truetype("arial.ttf", size)
    img = Image.new("RGBA", (400, 50), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.text((0, 0), text, font=font, fill=(255, 255, 255, 255))

    img_data = np.array(img)
    img_data = np.flipud(img_data)

    glRasterPos2f(x, y)
    glDrawPixels(img.width, img.height, GL_RGBA, GL_UNSIGNED_BYTE, img_data)
