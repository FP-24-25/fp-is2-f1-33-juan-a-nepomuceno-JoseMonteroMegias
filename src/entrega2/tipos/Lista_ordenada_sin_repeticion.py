from typing import Callable, Generic, TypeVar
from entrega2.tipos.Agregado_lineal import AgregadoLineal
E = TypeVar('E')
R = TypeVar('R')

class Lista_ordenada_sin_repeticion(AgregadoLineal[E], Generic[E, R]):
    def __init__(self, order: Callable[[E], R]):
        super().__init__()
        self._order = order

    def of(order: Callable[[E], R]) -> "Lista_ordenada_sin_repeticion[E, R]":
        return Lista_ordenada_sin_repeticion(order)

    def __index_order(self, e: E) -> int:
        for i, existing_element in enumerate(self._elements):
            if self._order(e) < self._order(existing_element):
                return i
            elif self._order(e) == self._order(existing_element):
                return -1
        return len(self._elements)

    def add(self, e: E) -> None:
        index = self.__index_order(e)
        if index != -1:
            self._elements.insert(index, e)

    def __repr__(self) -> str:
        elements_str = ', '.join(map(str, self._elements))
        return f"ListaOrdenadaSinRepeticion({elements_str})"