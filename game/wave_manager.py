from game.balloon import Balloon
from game.balloon_types import BALLOON_TYPES

class WaveManager:
    def __init__(self, path_points, waves):
        self.path_points = path_points
        self.waves = waves
        self.current_wave = 0
        self.spawn_timer = 0
        self.spawn_interval = 0.3
        self.queue = []
        self.finished = False
        self.spawning = False

    def parse_wave(self, wave_str):
        entries = wave_str.split(',')
        result = []
        for entry in entries:
            count, btype = entry.split('*')
            result += [btype] * int(count)
        return result

    def can_start_next_wave(self, balloons):
        return all(b.finished or not b.alive for b in balloons) and not self.queue

    def start_wave(self):
        if self.current_wave < len(self.waves):
            self.queue = self.parse_wave(self.waves[self.current_wave])
            self.spawning = True
            print(f"🌊 Iniciando wave {self.current_wave + 1}")
            self.current_wave += 1
        else:
            self.finished = True

    def update(self, dt):
        self.spawn_timer += dt
        spawned = []

        if self.spawning and self.queue and self.spawn_timer >= self.spawn_interval:
            btype = self.queue.pop(0)
            props = BALLOON_TYPES[btype]
            balloon = Balloon(
                props["texture_id"],
                props["width"],
                props["height"],
                self.path_points,
                speed=props["speed"],
                health=props["health"]
            )
            spawned.append(balloon)
            self.spawn_timer = 0

        if self.spawning and not self.queue:
            self.spawning = False

        return spawned
