import pyxel
    
class PjPrueba:
    def __init__(self, x: int, y: int, name: str = "prueba 1") -> None:
        self.x = x
        self.y = y
        self.name = name
        self.color = 8
        self.selected = False
    
    def interact(self) -> None:
        # si lo seleccionas cambia el color
        self.selected = not self.selected
        self.color = 11 if self.selected else 8

    def draw(self, title_size: int) -> None:
        # para calcular el centro de la celda
        draw_x = self.x * title_size + title_size // 2
        draw_y = self.y * title_size + title_size // 2
        radius = title_size // 3
        
        pyxel.circ(draw_x, draw_y, radius, self.color)

        if self.selected:
            pyxel.circb(draw_x, draw_y, radius + 2, 7)

