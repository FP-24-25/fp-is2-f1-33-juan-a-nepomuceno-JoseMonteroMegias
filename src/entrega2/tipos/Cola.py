from entrega2.tipos.Agregado_lineal import AgregadoLineal
from typing import TypeVar
E = TypeVar('E')
class Cola(AgregadoLineal[E]):
    def __init__(self):
        super().__init__()

    @staticmethod
    def of() -> "Cola[E]":
        return Cola()

    def add(self, e: E) -> None:
        self._elements.append(e)

    def __repr__(self) -> str:
        elements_str = ', '.join(map(str, self._elements))
        return f"Cola({elements_str})"