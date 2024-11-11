from entrega2.tipos.Cola import *

#1

cola = Cola.of()
cola.add(23)
cola.add(47)
cola.add(1)
cola.add(2)
cola.add(-3)
cola.add(4)
cola.add(5)
print(cola)

elemento=cola.remove_all()
print(elemento)
