# main.py
import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
from PIL import Image
import sys
import time

from utils.textures import load_texture
from render.sprite import draw_sprite
from render.map import draw_path

from game.path import path_points
from game.balloon import Balloon
from game.tower import Tower

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_TITLE = "Bloons Tower Defense - OpenGL"

# ✅ Estados globais
money = 0
lives = 20

def init_window():
    if not glfw.init():
        print("Erro ao inicializar GLFW")
        sys.exit()

    window = glfw.create_window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE, None, None)
    if not window:
        glfw.terminate()
        print("Erro ao criar janela GLFW")
        sys.exit()

    glfw.make_context_current(window)

    glViewport(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, WINDOW_WIDTH, WINDOW_HEIGHT, 0)
    glMatrixMode(GL_MODELVIEW)

    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    return window

def main_loop(window):
    global money, lives

    map_texture, _, _ = load_texture("assets/img/map.png")
    balloon_texture, bw, bh = load_texture("assets/img/enemies.png")
    tower_texture, tw, th = load_texture("assets/img/monkey1.png")

    balloons = [Balloon(balloon_texture, bw, bh, path_points)]
    # tower = Tower(300, 300, tower_texture, tw, th)

    last_time = time.time()

    while not glfw.window_should_close(window):
        current_time = time.time()
        dt = current_time - last_time
        last_time = current_time

        glClearColor(0.2, 0.2, 0.25, 1)
        glClear(GL_COLOR_BUFFER_BIT)

        draw_sprite(map_texture, 0, 0, 800, 600)
        draw_path(path_points, size=40)

        for balloon in balloons:
            if not balloon.finished:
                balloon.update(dt)
                balloon.draw(draw_sprite)
            else:
                if balloon.alive:
                    lives -= 1
                    balloon.alive = False
                    print(f"❌ Balão escapou! Vidas restantes: {lives}")
                    if lives <= 0:
                        print("🏳️ Fim de jogo!")
                        glfw.set_window_should_close(window, True)

        # Verifica balões destruídos
        for balloon in balloons:
            if not balloon.alive and not balloon.finished:
                money += 5  # valor de recompensa
                balloon.finished = True
                print(f"💰 Balão destruído! Dinheiro: ${money}")

        # tower.update(balloons, current_time)
        # tower.draw(draw_sprite)

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    window = init_window()
    main_loop(window)
