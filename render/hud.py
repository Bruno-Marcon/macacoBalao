from OpenGL.GL import *
from OpenGL.GLUT import *
import glfw
from render.sprite import draw_sprite
from game.tower_types import TOWER_TYPES


def draw_stroke_text(text, x, y, scale=0.1):
    glPushMatrix()
    glTranslatef(x, y, 0)
    glScalef(scale, -scale, scale)  # Corrige orientação

    glLineWidth(1.3)  # Suaviza espessura do traço

    for c in text:
        glutStrokeCharacter(GLUT_STROKE_ROMAN, ord(c))
    glPopMatrix()


def draw_tower_card(x, y, width, height, selected=False, hovered=False):
    """Desenha um card de torre com borda e destaque."""
    glColor4f(0.15, 0.15, 0.2, 0.9)
    glBegin(GL_QUADS)
    glVertex2f(x, y)
    glVertex2f(x + width, y)
    glVertex2f(x + width, y + height)
    glVertex2f(x, y + height)
    glEnd()

    # Borda destacada
    if selected:
        glColor3f(0.2, 1, 0.2)
    elif hovered:
        glColor3f(1, 1, 0.6)
    else:
        glColor3f(0.5, 0.5, 0.5)

    glLineWidth(2)
    glBegin(GL_LINE_LOOP)
    glVertex2f(x, y)
    glVertex2f(x + width, y)
    glVertex2f(x + width, y + height)
    glVertex2f(x, y + height)
    glEnd()


class HUD:
    def __init__(self, coin_texture_id):
        self.coin_texture_id = coin_texture_id
        self.panel_x = 720
        self.width = 80
        self.card_w = 70
        self.card_h = 100
        self.start_y = 120
        self.spacing = 120

    def draw(self, selected_tower_type, money):
        self.draw_panel()
        self.draw_money(money)
        self.draw_towers(selected_tower_type)

    def draw_panel(self):
        glColor4f(0.1, 0.1, 0.1, 0.95)
        glBegin(GL_QUADS)
        glVertex2f(self.panel_x, 0)
        glVertex2f(self.panel_x + self.width, 0)
        glVertex2f(self.panel_x + self.width, 600)
        glVertex2f(self.panel_x, 600)
        glEnd()

        # Título
        glColor3f(1, 1, 1)
        draw_stroke_text("Loja", self.panel_x + 5, 30, scale=0.1)

    def draw_money(self, money):
        coin_x = self.panel_x + 10
        coin_y = 75
        coin_size = 16

        # Moeda
        draw_sprite(self.coin_texture_id, coin_x, coin_y - coin_size // 2, coin_size, coin_size)

        # Texto
        glColor3f(1, 1, 0.3)
        draw_stroke_text(f"${money}", coin_x + coin_size + 5, coin_y, scale=0.09)

        # Separador
        glColor3f(0.3, 0.3, 0.3)
        glBegin(GL_LINES)
        glVertex2f(self.panel_x + 5, 100)
        glVertex2f(self.panel_x + self.width - 5, 100)
        glEnd()

    def draw_towers(self, selected_tower_type):
        mx, my = glfw.get_cursor_pos(glfw.get_current_context())

        for idx, (tower_id, props) in enumerate(TOWER_TYPES.items()):
            x = self.panel_x + 5
            y = self.start_y + idx * self.spacing

            hovered = x <= mx <= x + self.card_w and y <= my <= y + self.card_h
            selected = tower_id == selected_tower_type

            draw_tower_card(x, y, self.card_w, self.card_h, selected, hovered)

            draw_sprite(props["texture_id"], x + 10, y + 10, props["width"], props["height"])

            glColor3f(1, 1, 1)
            draw_stroke_text(tower_id.upper(), x + 5, y + 78, scale=0.07)
            draw_stroke_text(f"${props['cost']}", x + 5, y + 92, scale=0.065)


def get_clicked_tower_type(x, y):
    """Determina se clicou em uma torre com base nas coordenadas."""
    start_y = 120
    spacing = 120
    card_w = 70
    card_h = 100
    card_x = 725

    if not (card_x <= x <= card_x + card_w):
        return None

    for idx, (tower_id, _) in enumerate(TOWER_TYPES.items()):
        cy = start_y + idx * spacing
        if cy <= y <= cy + card_h:
            return tower_id

    return None
