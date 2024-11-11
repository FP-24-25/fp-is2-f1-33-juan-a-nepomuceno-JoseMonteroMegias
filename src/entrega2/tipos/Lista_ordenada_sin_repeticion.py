from typing import Callable, Generic, TypeVar, List
from Agregado_lineal import AgregadoLineal
# Definimos tipos genéricos para los elementos y el criterio de ordenación
E = TypeVar('E')
R = TypeVar('R')

class Lista_ordenada_sin_repeticion(AgregadoLineal[E], Generic[E, R]):
    def __init__(self, order: Callable[[E], R]):
        super().__init__()
        self._order = order  # Función de ordenación

    @staticmethod
    def of(order: Callable[[E], R]) -> "Lista_ordenada_sin_repeticion[E, R]":
        """Método de factoría para crear una lista ordenada sin repetición con un criterio de orden dado."""
        return Lista_ordenada_sin_repeticion(order)

    def __index_order(self, e: E) -> int:
        """Calcula el índice en el que se debe insertar el elemento para mantener el orden sin repetición."""
        for i, existing_element in enumerate(self._elements):
            if self._order(e) < self._order(existing_element):
                return i
            elif self._order(e) == self._order(existing_element):
                return -1  # Indica que el elemento ya existe y no debe ser insertado
        return len(self._elements)  # Si es mayor que todos, va al final

    def add(self, e: E) -> None:
        """Añade el elemento solo si no está ya presente, manteniendo el orden."""
        index = self.__index_order(e)
        if index != -1:  # Solo se inserta si el elemento no está presente
            self._elements.insert(index, e)

    def __repr__(self) -> str:
        """Devuelve una representación en cadena de la lista ordenada sin repetición."""
        elements_str = ', '.join(map(str, self._elements))
        return f"ListaOrdenadaSinRepeticion({elements_str})"

# Ejemplo de uso
if __name__ == "__main__":
    # Lista ordenada sin repetición para números en orden natural
    lista = Lista_ordenada_sin_repeticion.of(lambda x: x)
    lista.add(10)
    lista.add(5)
    lista.add(20)
    lista.add(10)  # Intento de duplicado, no debería añadirse
    print(lista)  # Salida: ListaOrdenadaSinRepeticion(5, 10, 20)

    # Lista ordenada sin repetición para strings en función de su longitud
    lista_str = Lista_ordenada_sin_repeticion.of(lambda x: len(x))
    lista_str.add("hola")
    lista_str.add("a")
    lista_str.add("Python")
    lista_str.add("hey")  # "hey" tiene misma longitud que "a", se ignora
    print(lista_str)  # Salida: ListaOrdenadaSinRepeticion(a, hola, Python)
