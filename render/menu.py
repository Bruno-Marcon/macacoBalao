# render/menu.py
import glfw
from OpenGL.GL import *
from render.sprite import draw_sprite
from utils.textures import load_texture

class Menu:
    def __init__(self):
        self.maps = [
            {"name": "Ice Map", "path": "assets/img/maps/mapIce.png"},
            {"name": "Grass Map", "path": "assets/img/maps/mapGrass.png"},
        ]
        self.selected_map = None
        self.loaded_textures = []

        for m in self.maps:
            tex_id, w, h = load_texture(m["path"])
            self.loaded_textures.append((tex_id, w, h))

    def run(self, window):
        while not glfw.window_should_close(window):
            glClearColor(0.1, 0.1, 0.1, 1)
            glClear(GL_COLOR_BUFFER_BIT)

            for i, (tex_id, w, h) in enumerate(self.loaded_textures):
                x = 100 + i * 300
                y = 150
                draw_sprite(tex_id, x, y, 200, 200)

            glfw.swap_buffers(window)
            glfw.poll_events()

            if glfw.get_mouse_button(window, glfw.MOUSE_BUTTON_LEFT) == glfw.PRESS:
                x, y = glfw.get_cursor_pos(window)
                for i in range(len(self.loaded_textures)):
                    bx = 100 + i * 300
                    by = 150
                    if bx <= x <= bx + 200 and by <= y <= by + 200:
                        self.selected_map = self.maps[i]["path"]
                        print(f"🗺️ Mapa selecionado: {self.maps[i]['name']}")
                        return self.selected_map
