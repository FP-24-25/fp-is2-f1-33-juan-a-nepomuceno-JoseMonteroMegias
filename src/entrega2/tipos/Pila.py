from entrega2.tipos.Agregado_lineal import AgregadoLineal
from typing import TypeVar
E = TypeVar('E')
class Pila(AgregadoLineal[E]):
    def __init__(self):
        super().__init__()

    @staticmethod
    def of() -> "Pila[E]":
        """Método de factoría que crea e inicializa una nueva pila."""
        return Pila()

    def add(self, e: E) -> None:
        """Añade un elemento a la parte superior de la pila (al principio)."""
        self._elements.insert(0, e)

    def __repr__(self) -> str:
        """Representación como cadena de la pila."""
        elements_str = ', '.join(map(str, self._elements))
        return f"Pila({elements_str})"

# Ejemplo de uso
if __name__ == "__main__":
    # Crear una pila de enteros
    pila = Pila.of()

    # Añadir elementos a la pila
    pila.add(10)
    pila.add(20)
    pila.add(30)

    print(pila)  # Salida: Pila(30, 20, 10)

    # Eliminar el primer elemento (el más reciente)
    print("Elemento eliminado:", pila.remove())  # Salida: 30
    print(pila)  # Salida: Pila(20, 10)
