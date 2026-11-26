import pyxel
from states.base_state import BaseState
from entities.pj_prueba import PjPrueba


class BattleState(BaseState):
    TILE_SIZE = 16
    GRID_COLS = 15
    GRID_ROWS = 10

    def __init__(self, app) -> None:
        super().__init__(app)
        self.cursor_x = 0
        self.cursor_y = 0
        self.character = PjPrueba(x=3, y=3, name="Soldado 1")

    def update(self) -> None:
        # 1. Movimiento libre del cursor con WASD o flechas
        if pyxel.btnp(pyxel.KEY_LEFT) or pyxel.btnp(pyxel.KEY_A):
            self.cursor_x = max(0, self.cursor_x - 1)
        elif pyxel.btnp(pyxel.KEY_RIGHT) or pyxel.btnp(pyxel.KEY_D):
            self.cursor_x = min(self.GRID_COLS - 1, self.cursor_x + 1)
        elif pyxel.btnp(pyxel.KEY_UP) or pyxel.btnp(pyxel.KEY_W):
            self.cursor_y = max(0, self.cursor_y - 1)
        elif pyxel.btnp(pyxel.KEY_DOWN) or pyxel.btnp(pyxel.KEY_S):
            self.cursor_y = min(self.GRID_ROWS - 1, self.cursor_y + 1)

        # 2. Lógica de selección y colocación con [E] o ESPACIO
        if pyxel.btnp(pyxel.KEY_E) or pyxel.btnp(pyxel.KEY_SPACE):
            if not self.character.selected:
                # Si el personaje no está seleccionado, comprobamos si el cursor está sobre él
                if self.cursor_x == self.character.x and self.cursor_y == self.character.y:
                    self.character.selected = True
                    self.character.color = 11  # Cambia a color claro al seleccionarlo
            else:
                # Si ya estaba seleccionado, lo movemos a la casilla actual del cursor y lo soltamos
                self.character.x = self.cursor_x
                self.character.y = self.cursor_y
                self.character.selected = False
                self.character.color = 8   # Vuelve a su color normal

        # Volver al briefing
        if pyxel.btnp(pyxel.KEY_B):
            from states.briefing_state import BriefingState
            self.app.set_state(BriefingState(self.app))

    def _draw_cursor(self) -> None:
        x = self.cursor_x * self.TILE_SIZE
        y = self.cursor_y * self.TILE_SIZE
        s = self.TILE_SIZE - 1
        arm = 4

        pyxel.line(x, y, x + arm, y, 10)
        pyxel.line(x, y, x, y + arm, 10)
        pyxel.line(x + s - arm, y, x + s, y, 10)
        pyxel.line(x + s, y, x + s, y + arm, 10)
        pyxel.line(x, y + s - arm, x, y + s, 10)
        pyxel.line(x, y + s, x + arm, y + s, 10)
        pyxel.line(x + s - arm, y + s, x + s, y + s, 10)
        pyxel.line(x + s, y + s - arm, x + s, y + s, 10)

    def draw(self) -> None:
        pyxel.cls(3)
        self.character.draw(self.TILE_SIZE)
        self._draw_cursor()
        
        # Texto de ayuda dinámico según si el personaje está seleccionado o no
        if self.character.selected:
            msg = "WASD: Mover cursor | [E] Colocar pj aquí | [B] Briefing"
        else:
            msg = "WASD: Mover cursor | [E] Seleccionar pj | [B] Briefing"
        pyxel.text(4, 150, msg, 7)