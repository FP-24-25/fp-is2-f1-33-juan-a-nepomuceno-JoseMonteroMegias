from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List

# Definimos un tipo genérico para los elementos en el agregado
E = TypeVar('E')

class AgregadoLineal(ABC, Generic[E]):
    def __init__(self):
        self._elements: List[E] = []  # Lista protegida para almacenar elementos

    @property
    def size(self) -> int:
        """Devuelve el número de elementos en el agregado."""
        return len(self._elements)

    @property
    def is_empty(self) -> bool:
        """Devuelve True si el agregado está vacío, False en caso contrario."""
        return len(self._elements) == 0

    @property
    def elements(self) -> List[E]:
        """Devuelve la lista completa de elementos almacenados en el agregado."""
        return self._elements

    @abstractmethod
    def add(self, e: E) -> None:
        """Método abstracto para añadir un nuevo elemento al agregado."""
        pass

    def add_all(self, ls: List[E]) -> None:
        """Añade una lista de elementos al agregado, utilizando el método add."""
        for item in ls:
            self.add(item)

    def remove(self) -> E:
        """Elimina y devuelve el primer elemento agregado. Si está vacío, muestra un error."""
        assert len(self._elements) > 0, 'El agregado está vacío'
        return self._elements.pop(0)

    def remove_all(self) -> List[E]:
        """Elimina todos los elementos, devolviendo una lista con los elementos eliminados."""
        removed_elements = []
        while not self.is_empty:
            removed_elements.append(self.remove())
        return removed_elements
