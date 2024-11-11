from typing import Callable, Generic, TypeVar, List
from Agregado_lineal import AgregadoLineal
# Definimos tipos genéricos para los elementos en la lista y para el criterio de ordenación
E = TypeVar('E')
R = TypeVar('R')

class Lista_ordenada(AgregadoLineal[E], Generic[E, R]):
    def __init__(self, order: Callable[[E], R]):
        super().__init__()
        self._order = order  # Almacena la función de ordenación

    @staticmethod
    def of(order: Callable[[E], R]) -> "Lista_ordenada[E, R]":
        """Método de factoría para crear una lista ordenada con el criterio de orden dado."""
        return Lista_ordenada(order)

    def __index_order(self, e: E) -> int:
        """Calcula el índice donde el elemento debe insertarse para mantener el orden."""
        for i, existing_element in enumerate(self._elements):
            # Compara usando la función de ordenación
            if self._order(e) < self._order(existing_element):
                return i
        return len(self._elements)  # Si es mayor que todos, va al final

    def add(self, e: E) -> None:
        """Añade un elemento en la posición correcta para mantener el orden."""
        index = self.__index_order(e)
        self._elements.insert(index, e)

    def __repr__(self) -> str:
        """Devuelve una representación en cadena de la lista ordenada."""
        elements_str = ', '.join(map(str, self._elements))
        return f"ListaOrdenada({elements_str})"

# Ejemplo de uso
if __name__ == "__main__":
    # Lista ordenada con números en orden natural
    lista = Lista_ordenada.of(lambda x: x)
    lista.add(10)
    lista.add(5)
    lista.add(20)
    print(lista)  # Salida: ListaOrdenada(5, 10, 20)

    # Lista ordenada con strings en función de su longitud
    lista_str = Lista_ordenada.of(lambda x: len(x))
    lista_str.add("hola")
    lista_str.add("a")
    lista_str.add("Python")
    print(lista_str)  # Salida: ListaOrdenada(a, hola, Python)
