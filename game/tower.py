# game/tower.py
import math
import time
from game.projectile import Projectile


class Tower:
    def __init__(self, x, y, texture_id, width, height, range_radius=150, cooldown=1.0):
        self.x = x
        self.y = y
        self.texture_id = texture_id
        self.width = width
        self.height = height
        self.range = range_radius
        self.cooldown = cooldown
        self.last_shot_time = 0
        self.projectiles = []

    def can_shoot(self, now):
        return now - self.last_shot_time >= self.cooldown

    def distance_to(self, balloon):
        dx = balloon.x - self.x
        dy = balloon.y - self.y
        return math.hypot(dx, dy)

    def update(self, balloons, now):
        for balloon in balloons:
            if balloon.finished:
                continue

            dist = self.distance_to(balloon)
            if dist <= self.range and self.can_shoot(now):
                self.shoot(balloon)
                self.last_shot_time = now
                break

        for proj in self.projectiles:
            proj.update()

            for balloon in balloons:
                if proj.alive and proj.check_collision(balloon):
                    balloon.hit()
                    proj.alive = False
        self.projectiles = [p for p in self.projectiles if p.alive and not p.offscreen()]

    def shoot(self, target):
        self.projectiles.append(Projectile(self.x, self.y, target))

    def draw(self, draw_sprite):
        draw_sprite(self.texture_id, self.x - self.width // 2, self.y - self.height // 2, self.width, self.height)
        for proj in self.projectiles:
            proj.draw()
