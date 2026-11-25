import pyxel
from states.base_state import BaseState


class BattleState(BaseState):
    TILE_SIZE = 16
    GRID_COLS = 15
    GRID_ROWS = 10

    def __init__(self, app) -> None:
        super().__init__(app)
        self.cursor_x = 0
        self.cursor_y = 0

    def update(self) -> None:
        if pyxel.btnp(pyxel.KEY_LEFT) or pyxel.btnp(pyxel.KEY_A):
            self.cursor_x = max(0, self.cursor_x - 1)
        elif pyxel.btnp(pyxel.KEY_RIGHT) or pyxel.btnp(pyxel.KEY_D):
            self.cursor_x = min(self.GRID_COLS - 1, self.cursor_x + 1)
        elif pyxel.btnp(pyxel.KEY_UP) or pyxel.btnp(pyxel.KEY_W):
            self.cursor_y = max(0, self.cursor_y - 1)
        elif pyxel.btnp(pyxel.KEY_DOWN) or pyxel.btnp(pyxel.KEY_S):
            self.cursor_y = min(self.GRID_ROWS - 1, self.cursor_y + 1)

        if pyxel.btnp(pyxel.KEY_B):
            from states.briefing_state import BriefingState
            self.app.set_state(BriefingState(self.app))

    def _draw_cursor(self) -> None:
        x = self.cursor_x * self.TILE_SIZE
        y = self.cursor_y * self.TILE_SIZE
        s = self.TILE_SIZE - 1
        arm = 4  # largo de cada patita de la L

        # Esquina superior izquierda
        pyxel.line(x, y, x + arm, y, 10)
        pyxel.line(x, y, x, y + arm, 10)

        # Esquina superior derecha
        pyxel.line(x + s - arm, y, x + s, y, 10)
        pyxel.line(x + s, y, x + s, y + arm, 10)

        # Esquina inferior izquierda
        pyxel.line(x, y + s - arm, x, y + s, 10)
        pyxel.line(x, y + s, x + arm, y + s, 10)

        # Esquina inferior derecha
        pyxel.line(x + s - arm, y + s, x + s, y + s, 10)
        pyxel.line(x + s, y + s - arm, x + s, y + s, 10)

    def draw(self) -> None:
        pyxel.cls(3)
        self._draw_cursor()