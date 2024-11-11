from entrega2.tipos.Lista_ordenada_sin_repeticion import *

#1

lista = Lista_ordenada_sin_repeticion.of(lambda x: -x)
lista.add(23)
lista.add(47)
lista.add(47)
lista.add(1)
lista.add(2)
lista.add(-3)
lista.add(4)
lista.add(5)
print(lista)

#2

elemento = lista.remove()
print(elemento)


#añado de nuevo el 47
lista.add(47)

#3

elemento = lista.remove_all()
print(elemento)


#vuelvo a añadir todo
lista.add(23)
lista.add(47)
lista.add(47)
lista.add(1)
lista.add(2)
lista.add(-3)
lista.add(4)
lista.add(5)

lista.add(0)
print(lista)

lista.add(0)
print(lista)

lista.add(7)
print(lista)
