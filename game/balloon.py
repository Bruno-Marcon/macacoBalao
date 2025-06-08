# game/balloon.py
import math

class Balloon:
    def __init__(self, texture_id, width, height, path, speed=100):
        self.texture_id = texture_id
        self.width = width
        self.height = height
        self.path = path
        self.current_point = 0
        self.x, self.y = path[0]
        self.speed = speed  # pixels por segundo
        self.finished = False
        self.alive = True

    def update(self, dt):
        if self.finished or self.current_point >= len(self.path) - 1:
            self.finished = True
            return

        target_x, target_y = self.path[self.current_point + 1]
        dx = target_x - self.x
        dy = target_y - self.y
        dist = math.hypot(dx, dy)

        if dist < 1:
            self.current_point += 1
            if self.current_point >= len(self.path) - 1:
                self.finished = True
            return

        dir_x = dx / dist
        dir_y = dy / dist

        self.x += dir_x * self.speed * dt
        self.y += dir_y * self.speed * dt
import math

class Balloon:
    def __init__(self, texture_id, width, height, path, speed=100):
        self.texture_id = texture_id
        self.width = width
        self.height = height
        self.path = path
        self.current_point = 0
        self.x, self.y = path[0]
        self.speed = speed  # pixels por segundo
        self.finished = False
        self.alive = True  # novo atributo

    def update(self, dt):
        if self.finished or not self.alive or self.current_point >= len(self.path) - 1:
            self.finished = True
            return

        target_x, target_y = self.path[self.current_point + 1]
        dx = target_x - self.x
        dy = target_y - self.y
        dist = math.hypot(dx, dy)

        if dist < 1:
            self.current_point += 1
            if self.current_point >= len(self.path) - 1:
                self.finished = True
            return

        dir_x = dx / dist
        dir_y = dy / dist

        self.x += dir_x * self.speed * dt
        self.y += dir_y * self.speed * dt

    def hit(self):
        self.alive = False
        self.finished = True  # garante que ele pare de andar

    def draw(self, draw_sprite):
        if self.alive:
            draw_sprite(self.texture_id, self.x - self.width // 2, self.y - self.height // 2, self.width, self.height)



    def draw(self, draw_sprite):
        draw_sprite(self.texture_id, self.x - self.width // 2, self.y - self.height // 2, self.width, self.height)
