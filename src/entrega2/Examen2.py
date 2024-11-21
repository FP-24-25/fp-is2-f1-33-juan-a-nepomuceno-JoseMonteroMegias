from entrega2.tipos.Agregado_lineal import AgregadoLineal
from typing import TypeVar

E = TypeVar('E')

#A PARTIR DE AQUI, HASTA QUE SE INDIQUE LO CONTRARIO ES EL EJERCICIO 1 DEL EXAMEN


class ColaConLimite(AgregadoLineal[E]):
    def __init__(self, capacidad: int):
        super().__init__()
        self.capacidad = capacidad

    def add(self, e: E) -> None:
        if self.is_full:
            raise OverflowError("La cola está llena.")
        self._elements.append(e)

    @property
    def is_full(self) -> bool:
        return self.size >= self.capacidad

    @classmethod
    def of(cls, capacidad: int):
        return cls(capacidad)




#A PARTIR DE AQUI, HASTA QUE SE INDIQUE LO CONTRARIO ES EL EJERCICIO 2 DEL EXAMEN


from typing import Callable, Generic, TypeVar, List

E = TypeVar('E')

class AgregadoLineal(Generic[E]):
    def __init__(self):
        self._elements: List[E] = []

    @property
    def size(self) -> int:
        return len(self._elements)

    @property
    def is_empty(self) -> bool:
        return len(self._elements) == 0

    @property
    def elements(self) -> List[E]:
        return self._elements

    def add(self, e: E) -> None:
        self._elements.append(e)

    def add_all(self, ls: List[E]) -> None:
        for item in ls:
            self.add(item)

    def remove(self) -> E:
        assert len(self._elements) > 0
        return self._elements.pop(0)

    def remove_all(self) -> List[E]:
        removed_elements = []
        while not self.is_empty:
            removed_elements.append(self.remove())
        return removed_elements

    def contains(self, e: E) -> bool:
        return e in self._elements

    def find(self, func: Callable[[E], bool]) -> E | None:
        for element in self._elements:
            if func(element):
                return element
        return None

    def filter(self, func: Callable[[E], bool]) -> List[E]:
        return [element for element in self._elements if func(element)]




#A PARTIR DE AQUI, HASTA EL FINAL ES EL EJERCICIO 3 EN EL QUE PONGO EN USO TODAS LAS FUNCIONES AGREGADAS EN LOS EJERCICIOS 1 Y 2

# Crear una cola con capacidad de 3 elementos
cola = ColaConLimite.of(3)

# Agregar elementos a la cola
cola.add("Tarea 1")
cola.add("Tarea 2")
cola.add("Tarea 3")

print("Elementos en la cola:", cola.elements)  # ['Tarea 1', 'Tarea 2', 'Tarea 3']

# Intentar agregar un elemento más, lo que debe lanzar OverflowError
try:
    cola.add("Tarea 4")
except OverflowError as e:
    print(e)  # "La cola está llena."

# Verificar si la cola está llena
print("¿La cola está llena?", cola.is_full)  # True

# Eliminar un elemento (FIFO)
primer_elemento = cola.remove()
print("Primer elemento eliminado:", primer_elemento)  # "Tarea 1"

# Mostrar elementos restantes en la cola
print("Elementos restantes en la cola:", cola.elements)  # ['Tarea 2', 'Tarea 3']


# Crear un agregado lineal
agregado = AgregadoLineal[int]()
agregado.add_all([10, 15, 20, 25, 30])

# Mostrar elementos actuales
print("Elementos en el agregado:", agregado.elements)  # [10, 15, 20, 25, 30]

# Verificar si un elemento está contenido
print("¿El agregado contiene 15?", agregado.contains(15))  # True
print("¿El agregado contiene 100?", agregado.contains(100))  # False

# Encontrar el primer elemento mayor que 18
mayor_que_18 = agregado.find(lambda x: x > 18)
print("Primer elemento mayor que 18:", mayor_que_18)  # 20

# Intentar encontrar un elemento que no cumpla la condición
mayor_que_100 = agregado.find(lambda x: x > 100)
print("Elemento mayor que 100:", mayor_que_100)  # None

# Filtrar elementos pares
pares = agregado.filter(lambda x: x % 2 == 0)
print("Elementos pares:", pares)  # [10, 20, 30]

# Filtrar elementos mayores que 20
mayores_que_20 = agregado.filter(lambda x: x > 20)
print("Elementos mayores que 20:", mayores_que_20)  # [25, 30]

# Eliminar todos los elementos del agregado
todos_los_elementos = agregado.remove_all()
print("Elementos eliminados:", todos_los_elementos)  # [10, 15, 20, 25, 30]

# Verificar si el agregado está vacío
print("¿El agregado está vacío?", agregado.is_empty)  # True
