from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from main import GameApp


class BaseState(ABC):
    def __init__(self, app: "GameApp") -> None:
        self.app = app

    @abstractmethod
    def update(self) -> None:
        """Actualiza la lógica del estado en cada fotograma."""

    @abstractmethod
    def draw(self) -> None:
        """Dibuja el estado actual en pantalla."""