from entrega2.tipos.Agregado_lineal import AgregadoLineal
from typing import TypeVar
E = TypeVar('E')
class Cola(AgregadoLineal[E]):
    def __init__(self):
        super().__init__()

    @staticmethod
    def of() -> "Cola[E]":
        """Método de factoría que crea e inicializa una nueva cola."""
        return Cola()

    def add(self, e: E) -> None:
        """Añade el elemento al final de la cola."""
        self._elements.append(e)

    def __repr__(self) -> str:
        """Devuelve una representación en cadena de la cola."""
        elements_str = ', '.join(map(str, self._elements))
        return f"Cola({elements_str})"

# Ejemplo de uso
if __name__ == "__main__":
    # Crear una cola de enteros
    cola = Cola.of()
    
    # Añadir elementos a la cola
    cola.add(10)
    cola.add(20)
    cola.add(30)
    
    print(cola)  # Salida: Cola(10, 20, 30)
    
    # Eliminar el primer elemento (el más antiguo) usando remove()
    print("Elemento eliminado:", cola.remove())  # Salida: 10
    print(cola)  # Salida: Cola(20, 30)
