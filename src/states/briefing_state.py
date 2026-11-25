import pyxel
from states.base_state import BaseState
from states.battle_state import BattleState


class BriefingState(BaseState):
    def update(self) -> None:
        if pyxel.btnp(pyxel.KEY_RETURN) or pyxel.btnp(pyxel.KEY_SPACE):
            self.app.set_state(BattleState(self.app))
        elif pyxel.btnp(pyxel.KEY_B):
            from states.title_state import TitleState
            self.app.set_state(TitleState(self.app))

    def draw(self) -> None:
        pyxel.cls(2)
        pyxel.text(16, 16, "MISION 01: BRIEFING", 7)
        pyxel.text(16, 36, "ENTER: Desplegar escuadron", 10)
        pyxel.text(16, 52, "B: Volver al titulo", 13)