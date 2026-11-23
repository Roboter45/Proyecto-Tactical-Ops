from pathlib import Path
import sys
import pyxel

SRC_DIR = Path(__file__).resolve().parent
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from states.base_state import BaseState
from states.title_state import TitleState


class GameApp:
    def __init__(self) -> None:
        self.state: BaseState = TitleState(self)
        pyxel.init(160, 128, title="Tactical Ops")
        pyxel.run(self.update, self.draw)

    def set_state(self, new_state: BaseState) -> None:
        self.state = new_state

    def update(self) -> None:
        self.state.update()

    def draw(self) -> None:
        self.state.draw()


if __name__ == "__main__":
    GameApp()