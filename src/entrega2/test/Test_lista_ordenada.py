from entrega2.tipos.Lista_ordenada import *

# 1

lista = Lista_ordenada.of(lambda x: x)
lista.add(3)
lista.add(1)
lista.add(2)
print(lista)

# 2

elemento = lista.remove()
print(elemento)



#añado de nuevo el 1
lista.add(1)

#3

elemento = lista.remove_all()
print(elemento)


#añado de nuevo los tres numeros
lista.add(3)
lista.add(1)
lista.add(2)

#4

lista.add(0)
print(lista)

lista.add(10)
print(lista)

lista.add(7)
print(lista)