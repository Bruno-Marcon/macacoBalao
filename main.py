import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import glutInit
import sys
import time

from utils.textures import load_texture, render_text
from render.sprite import draw_sprite
from render.map import draw_path
from render.menu import Menu
from render.hud import HUD, get_clicked_tower_type

from game.path import path_points
from game.balloon import Balloon
from game.tower import Tower
from game.wave_manager import WaveManager
from game.waves import waves
from game.balloon_types import load_balloon_textures
from game.tower_types import TOWER_TYPES, load_tower_textures

glutInit()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_TITLE = "Fabão Balão"

money = 25
lives = 20
placing_tower = False
preview_pos = None
towers = []
selected_tower_type = None

def show_game_over():
    message = "FIM DE JOGO!"
    font_size = 48
    text_x = 200
    text_y = 300

    glColor4f(0, 0, 0, 0.7)
    glBegin(GL_QUADS)
    glVertex2f(100, text_y - 20)
    glVertex2f(700, text_y - 20)
    glVertex2f(700, text_y + 60)
    glVertex2f(100, text_y + 60)
    glEnd()

    glColor3f(0, 0, 0)
    render_text(message, text_x + 2, text_y + 2, size=font_size)

    glColor3f(1, 0.2, 0.2)
    render_text(message, text_x, text_y, size=font_size)


def is_on_path(x, y):
    for px, py in path_points:
        if abs(x - px) < 25 and abs(y - py) < 25:
            return True
    return False


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
    glEnable(GL_LINE_SMOOTH)
    glHint(GL_LINE_SMOOTH_HINT, GL_NICEST)
    glEnable(GL_POLYGON_SMOOTH)
    glHint(GL_POLYGON_SMOOTH_HINT, GL_NICEST)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    return window


def main_loop(window, map_texture):
    global money, lives, placing_tower, preview_pos, selected_tower_type

    main_loop.mouse_released = True

    load_balloon_textures()
    load_tower_textures()

    wave_manager = WaveManager(path_points, waves)
    balloons = []
    last_time = time.time()

    while not glfw.window_should_close(window):
        current_time = time.time()
        dt = current_time - last_time
        last_time = current_time

        glClearColor(0.2, 0.2, 0.25, 1)
        glClear(GL_COLOR_BUFFER_BIT)

        draw_sprite(map_texture, 0, 0, 800, 600)
        hud.draw(selected_tower_type, money)

        if wave_manager.can_start_next_wave(balloons):
            wave_manager.start_wave()

        new_balloons = wave_manager.update(dt)
        balloons.extend(new_balloons)

        for balloon in balloons:
            if not balloon.finished:
                balloon.update(dt)
                balloon.draw(draw_sprite)
            elif balloon.alive:
                lives -= 1
                balloon.alive = False
                print(f"❌ Balão escapou! Vidas restantes: {lives}")
                if lives <= 0:
                    show_game_over()
                    glfw.swap_buffers(window)  # garante renderização do texto
                    time.sleep(3)              # exibe por 3 segundos
                    glfw.set_window_should_close(window, True)

        for balloon in balloons:
            if not balloon.alive and not balloon.was_counted:
                money += 2
                balloon.was_counted = True
                print(f"💰 Balão destruído! Dinheiro: ${money}")

        for tower in towers:
            tower.update(balloons, current_time)
            tower.draw(draw_sprite)

        if placing_tower and preview_pos and selected_tower_type:
            x, y = preview_pos
            props = TOWER_TYPES[selected_tower_type]
            glColor4f(1, 1, 1, 0.5)
            draw_sprite(props["texture_id"], x - props["width"] // 2, y - props["height"] // 2, props["width"], props["height"])
            glColor4f(1, 1, 1, 1)

        if glfw.get_mouse_button(window, glfw.MOUSE_BUTTON_LEFT) == glfw.RELEASE:
            main_loop.mouse_released = True

        elif glfw.get_mouse_button(window, glfw.MOUSE_BUTTON_LEFT) == glfw.PRESS and main_loop.mouse_released:
            main_loop.mouse_released = False
            x, y = glfw.get_cursor_pos(window)
            x, y = int(x), int(y)

            if placing_tower and selected_tower_type:
                if not is_on_path(x, y):
                    props = TOWER_TYPES[selected_tower_type]
                    if money >= props["cost"]:
                        towers.append(Tower(
                            x - props["width"] // 2, y - props["height"] // 2,
                            props["texture_id"], props["width"], props["height"],
                            range_radius=props["range"], cooldown=props["cooldown"]
                        ))
                        money -= props["cost"]
                        print(f"📍 Torre {selected_tower_type} posicionada | Dinheiro restante: ${money}")
                    else:
                        print("❌ Dinheiro insuficiente!")
                    placing_tower = False
                    preview_pos = None
                else:
                    print("🚫 Não pode posicionar sobre o caminho!")
            else:
                clicked_type = get_clicked_tower_type(x, y)
                if clicked_type:
                    selected_tower_type = clicked_type
                    placing_tower = True
                    print(f"🛠️ Selecionou torre: {selected_tower_type}")

        if placing_tower:
            px, py = glfw.get_cursor_pos(window)
            preview_pos = (int(px), int(py))

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()


if __name__ == "__main__":
    window = init_window()

    menu = Menu()
    selected_map_path = menu.run(window)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, WINDOW_WIDTH, WINDOW_HEIGHT, 0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    map_texture, _, _ = load_texture(selected_map_path)
    coin_texture_id, _, _ = load_texture("assets/img/ui/coin.png")
    hud = HUD(coin_texture_id)


    main_loop(window, map_texture)