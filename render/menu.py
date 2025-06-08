import glfw
from OpenGL.GL import *
from utils.textures import load_texture, render_text
from render.sprite import draw_sprite


class Menu:
    def __init__(self, window_width=800, window_height=600):
        self.window_width = window_width
        self.window_height = window_height

        self.maps = [
            {"name": "Ice Map", "path": "assets/img/maps/mapIce.png"},
            {"name": "Grass Map", "path": "assets/img/maps/mapGrass.png"},
        ]
        self.selected_map = None
        self.loaded_textures = []

        for m in self.maps:
            tex_id, w, h = load_texture(m["path"])
            self.loaded_textures.append((tex_id, w, h))

        self.quit_button = {"x": self.window_width - 120, "y": 20, "w": 100, "h": 40}

    def run(self, window):
        self.set_menu_projection()

        while not glfw.window_should_close(window):
            glClearColor(0.1, 0.1, 0.1, 1)
            glClear(GL_COLOR_BUFFER_BIT)

            render_text("Selecione um Mapa", self.window_width // 2 - 100, 40, size=24)

            total_width = len(self.loaded_textures) * 220
            start_x = (self.window_width - total_width) // 2 + 10

            for i, (tex_id, w, h) in enumerate(self.loaded_textures):
                x = start_x + i * 240
                y = 150
                draw_sprite(tex_id, x, y, 200, 200)
                render_text(self.maps[i]["name"], x + 50, y + 220, size=18)

            self.draw_button(self.quit_button["x"], self.quit_button["y"], self.quit_button["w"], self.quit_button["h"], "Sair")

            glfw.swap_buffers(window)
            glfw.poll_events()

            if glfw.get_mouse_button(window, glfw.MOUSE_BUTTON_LEFT) == glfw.PRESS:
                x, y = glfw.get_cursor_pos(window)

                for i in range(len(self.loaded_textures)):
                    bx = start_x + i * 240
                    by = 150
                    if bx <= x <= bx + 200 and by <= y <= by + 200:
                        self.selected_map = self.maps[i]["path"]
                        print(f"🗺️ Mapa selecionado: {self.maps[i]['name']}")
                        return self.selected_map

                q = self.quit_button
                if q["x"] <= x <= q["x"] + q["w"] and q["y"] <= y <= q["y"] + q["h"]:
                    print("👋 Saindo do menu.")
                    glfw.set_window_should_close(window, True)

    def draw_button(self, x, y, width, height, label):
        glColor3f(0.8, 0.2, 0.2)
        glBegin(GL_QUADS)
        glVertex2f(x, y)
        glVertex2f(x + width, y)
        glVertex2f(x + width, y + height)
        glVertex2f(x, y + height)
        glEnd()

        glColor3f(1, 1, 1)
        render_text(label, x + 20, y + 10, size=16)

    def set_menu_projection(self):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0, self.window_width, 0, self.window_height, -1, 1)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
