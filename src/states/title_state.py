import pyxel
from states.base_state import BaseState
from states.briefing_state import BriefingState


class TitleState(BaseState):
    def update(self) -> None:
        if pyxel.btnp(pyxel.KEY_RETURN) or pyxel.btnp(pyxel.KEY_SPACE):
            self.app.set_state(BriefingState(self.app))

    def draw(self) -> None:
        pyxel.cls(1)
        title = "TACTICAL OPS"
        prompt = "Pulsa ENTER o ESPACIO"
        pyxel.text((pyxel.width - len(title) * 4) // 2, 64, title, 7)
        pyxel.text((pyxel.width - len(prompt) * 4) // 2, 84, prompt, 10)