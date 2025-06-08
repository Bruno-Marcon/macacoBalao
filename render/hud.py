from OpenGL.GL import *
from render.sprite import draw_sprite
from utils.text import draw_text
from game.tower_types import TOWER_TYPES

def draw_hud(selected_tower_type, money):
    # Fundo do HUD
    glColor4f(0.1, 0.1, 0.1, 0.7)
    glBegin(GL_QUADS)
    glVertex2f(720, 0)
    glVertex2f(800, 0)
    glVertex2f(800, 600)
    glVertex2f(720, 600)
    glEnd()

    glColor3f(1, 1, 1)

    # Desenhar cada torre disponível em colunas
    start_y = 40
    spacing = 100
    for idx, (tower_id, props) in enumerate(TOWER_TYPES.items()):
        y = start_y + idx * spacing
        draw_sprite(props["texture_id"], 720 + 40 - props["width"] // 2, y, props["width"], props["height"])
        
        # Nome e custo
        color = (0.2, 1, 0.2) if tower_id == selected_tower_type else (1, 1, 0)
        glColor3f(*color)
        draw_text(f"{tower_id.upper()} - ${props['cost']}", 725, y + props["height"] + 5)

    # Texto de dinheiro
    glColor3f(1, 1, 0)
    draw_text("💰 $" + str(money), 725, 550)


def get_clicked_tower_type(x, y):
    start_y = 40
    spacing = 100
    for idx, (tower_id, props) in enumerate(TOWER_TYPES.items()):
        sprite_y = start_y + idx * spacing
        if 720 <= x <= 800 and sprite_y <= y <= sprite_y + props["height"]:
            return tower_id
    return None

