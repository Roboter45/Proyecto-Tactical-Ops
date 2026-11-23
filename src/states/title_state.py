import pyxel
from states.base_state import BaseState
from states.briefing_state import BriefingState


class TitleState(BaseState):
    def update(self) -> None:
        if pyxel.btnp(pyxel.KEY_RETURN) or pyxel.btnp(pyxel.KEY_SPACE):
            self.app.set_state(BriefingState(self.app))

    def draw(self) -> None:
        pyxel.cls(1)
        pyxel.text(44, 52, "TACTICAL OPS", 7)
        pyxel.text(20, 68, "Pulsa ENTER o ESPACIO", 10)