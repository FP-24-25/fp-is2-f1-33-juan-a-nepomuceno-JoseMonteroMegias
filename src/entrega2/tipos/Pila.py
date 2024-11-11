from entrega2.tipos.Agregado_lineal import AgregadoLineal
from typing import TypeVar
E = TypeVar('E')
class Pila(AgregadoLineal[E]):
    def __init__(self):
        super().__init__()

    @staticmethod
    def of() -> "Pila[E]":
        return Pila()

    def add(self, e: E) -> None:
        self._elements.insert(0, e)

    def __repr__(self) -> str:
        elements_str = ', '.join(map(str, self._elements))
        return f"Pila({elements_str})"