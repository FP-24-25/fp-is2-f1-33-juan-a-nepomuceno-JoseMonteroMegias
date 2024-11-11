from typing import List, TypeVar, Generic

E = TypeVar('E')  # Tipo de los elementos
P = TypeVar('P')  # Tipo de las prioridades

class Cola_de_prioridad(Generic[E, P]):
    def __init__(self):
        self._elements: List[E] = []  # Lista para almacenar los elementos
        self._priorities: List[P] = []  # Lista para almacenar las prioridades
    
    def size(self) -> int:
        """Devuelve el número de elementos en la cola."""
        return len(self._elements)
    
    def is_empty(self) -> bool:
        """Devuelve True si la cola está vacía, False en caso contrario."""
        return len(self._elements) == 0
    
    def elements(self) -> List[E]:
        """Devuelve la lista de los elementos almacenados en la cola."""
        return self._elements
    
    def add(self, e: E, priority: P) -> None:
        """Añade un elemento con su prioridad a la cola, manteniendo el orden correcto."""
        index = self._index_order(priority)
        self._elements.insert(index, e)
        self._priorities.insert(index, priority)
    
    def add_all(self, ls: List[tuple[E, P]]) -> None:
        """Añade una lista de elementos con sus prioridades a la cola."""
        for e, priority in ls:
            self.add(e, priority)
    
    def remove(self) -> E:
        """Elimina y devuelve el elemento con la mayor prioridad."""
        assert len(self._elements) > 0, 'El agregado está vacío'
        return self._elements.pop(0)  # El primer elemento es el de mayor prioridad
    
    def remove_all(self) -> List[E]:
        """Elimina todos los elementos y devuelve una lista con los eliminados."""
        removed_elements = self._elements[:]
        self._elements.clear()
        self._priorities.clear()
        return removed_elements
    
    def _index_order(self, priority: P) -> int:
        """Calcula el índice en el que se debe insertar un nuevo elemento según su prioridad."""
        for i, p in enumerate(self._priorities):
            if priority < p:  # Se insertará antes de este elemento si su prioridad es menor
                return i
        return len(self._elements)  # Si la prioridad es mayor que todas, se añade al final
    
    def decrease_priority(self, e: E, new_priority: P) -> None:
        """Disminuye la prioridad de un elemento y lo recoloca si es necesario."""
        if e in self._elements:
            index = self._elements.index(e)
            old_priority = self._priorities[index]
            if new_priority < old_priority:
                # Elimina el elemento y lo vuelve a añadir con la nueva prioridad
                self._elements.pop(index)
                self._priorities.pop(index)
                self.add(e, new_priority)

    def __repr__(self) -> str:
        """Representación como cadena de la cola de prioridad."""
        return f"ColaPrioridad" + str(list(zip(self._elements, self._priorities)))