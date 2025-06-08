import math
from OpenGL.GL import *


class Projectile:
    def __init__(self, x, y, target, speed=500):
        self.x = x
        self.y = y
        dx = target.x - x
        dy = target.y - y
        dist = math.hypot(dx, dy)
        self.vx = (dx / dist) * speed
        self.vy = (dy / dist) * speed
        self.alive = True

    def update(self):
        self.x += self.vx * 0.016
        self.y += self.vy * 0.016

    def draw(self):
        if not self.alive:
            return
        glColor3f(1, 1, 0)
        glBegin(GL_QUADS)
        glVertex2f(self.x - 3, self.y - 3)
        glVertex2f(self.x + 3, self.y - 3)
        glVertex2f(self.x + 3, self.y + 3)
        glVertex2f(self.x - 3, self.y + 3)
        glEnd()

    def offscreen(self):
        return self.x < 0 or self.x > 1280 or self.y < 0 or self.y > 720

    def check_collision(self, balloon):
        if not balloon.alive:
            return False
        dx = balloon.x - self.x
        dy = balloon.y - self.y
        distance = math.hypot(dx, dy)
        return distance < 20  # raio aproximado do balão