import pyxel
from states.base_state import BaseState


class BriefingState(BaseState):
    def update(self) -> None:
        if pyxel.btnp(pyxel.KEY_B):
            from states.title_state import TitleState
            self.app.set_state(TitleState(self.app))

    def draw(self) -> None:
        pyxel.cls(2)
        pyxel.text(16, 16, "MISION 01: BRIEFING", 7)
        pyxel.text(16, 32, "Has pulsado ENTER/ESPACIO!", 10)
        pyxel.text(16, 52, "Pulsa B para volver", 13)