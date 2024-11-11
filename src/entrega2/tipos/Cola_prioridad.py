from typing import List, Tuple, Generic, TypeVar

E = TypeVar('E')  # Tipo de elemento
P = TypeVar('P')  # Tipo de prioridad

class ColaDePrioridad(Generic[E, P]):
    def __init__(self):
        self._elements: List[E] = []  # Lista de elementos
        self._priorities: List[P] = []  # Lista de prioridades correspondientes a los elementos

    def size(self) -> int:
        """Devuelve el número de elementos en la cola de prioridad."""
        return len(self._elements)

    def is_empty(self) -> bool:
        """Devuelve True si la cola está vacía, False en caso contrario."""
        return len(self._elements) == 0

    def elements(self) -> List[E]:
        """Devuelve la lista completa de elementos."""
        return self._elements

    def index_order(self, priority: P) -> int:
        """Calcula el índice en el que se debe insertar el nuevo elemento, basado en su prioridad."""
        for i, p in enumerate(self._priorities):
            if priority > p:  # Si la nueva prioridad es mayor, se inserta antes
                return i
        return len(self._elements)  # Si es la prioridad más baja, se inserta al final

    def add(self, e: E, priority: P) -> None:
        """Añade un elemento con una prioridad determinada en la posición correcta."""
        index = self.index_order(priority)
        self._elements.insert(index, e)
        self._priorities.insert(index, priority)

    def add_all(self, ls: List[Tuple[E, P]]) -> None:
        """Añade múltiples elementos a la cola con sus respectivas prioridades."""
        for e, p in ls:
            self.add(e, p)

    def remove(self) -> E:
        """Elimina y devuelve el elemento con la mayor prioridad (el primero en la lista)."""
        assert len(self._elements) > 0, 'El agregado está vacío'
        return self._elements.pop(0)

    def remove_all(self) -> List[E]:
        """Elimina todos los elementos y devuelve la lista de elementos eliminados."""
        removed_elements = self._elements[:]
        self._elements.clear()
        self._priorities.clear()
        return removed_elements

    def decrease_priority(self, e: E, new_priority: P) -> None:
        """Disminuye la prioridad de un elemento e."""
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
        return f"ColaPrioridad[{', '.join(f'({e}, {p})' for e, p in zip(self._elements, self._priorities))}]"

# Ejemplo de uso
if __name__ == "__main__":
    # Crear una cola de prioridad para gestionar pacientes
    cola = ColaDePrioridad[str, int]()
    
    # Añadir pacientes con sus prioridades
    cola.add("Paciente Grave", 3)  # Menos grave
    cola.add("Paciente Moderado", 2)  # Moderado
    cola.add("Paciente Leve", 1)  # Más grave
    
    print(cola)  # Salida: ColaPrioridad[(Paciente A, 3), (Paciente B, 2), (Paciente C, 1)]
    
    # Eliminar el paciente con la mayor prioridad
    print("Paciente atendido:", cola.remove())  # Salida: Paciente A
    
    # Cambiar la prioridad de un paciente
    cola.decrease_priority("Paciente B", 0)
    print("Después de cambiar la prioridad:", cola)  # Salida: ColaPrioridad[(Paciente B, 0), (Paciente C, 1)]
