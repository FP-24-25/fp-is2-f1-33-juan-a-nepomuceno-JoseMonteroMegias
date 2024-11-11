from typing import Callable, Generic, TypeVar
from entrega2.tipos.Agregado_lineal import AgregadoLineal
E = TypeVar('E')
R = TypeVar('R')

class Lista_ordenada(AgregadoLineal[E], Generic[E, R]):
    def __init__(self, order: Callable[[E], R]):
        super().__init__()
        self._order = order

    @staticmethod
    def of(order: Callable[[E], R]) -> "Lista_ordenada[E, R]":
        return Lista_ordenada(order)

    def __index_order(self, e: E) -> int:
        for i, existing_element in enumerate(self._elements):
            if self._order(e) < self._order(existing_element):
                return i
        return len(self._elements)

    def add(self, e: E) -> None:
        index = self.__index_order(e)
        self._elements.insert(index, e)

    def __repr__(self) -> str:
        elements_str = ', '.join(map(str, self._elements))
        return f"ListaOrdenada({elements_str})"
