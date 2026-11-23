import pyxel


class GameApp:
    def __init__(self) -> None:
        self.screen = "title"
        pyxel.init(160, 128, title="Tactical Ops")
        pyxel.run(self.update, self.draw)

    def update(self) -> None:
        if self.screen == "title":
            if pyxel.btnp(pyxel.KEY_RETURN) or pyxel.btnp(pyxel.KEY_SPACE):
                self.screen = "battle_test"
        elif self.screen == "battle_test":
            if pyxel.btnp(pyxel.KEY_ESCAPE):
                self.screen = "title"

    def draw(self) -> None:
        if self.screen == "title":
            pyxel.cls(1)
            pyxel.text(44, 52, "TACTICAL OPS", 7)
            pyxel.text(24, 68, "Pulsa ENTER para probar", 10)
        elif self.screen == "battle_test":
            pyxel.cls(2)
            pyxel.text(16, 16, "PANTALLA DE PRUEBA", 7)
            pyxel.text(16, 30, "ESC para volver", 13)


if __name__ == "__main__":
    GameApp()