import unittest
from typing import Callable
from entrega2.tipos.Lista_ordenada import Lista_ordenada  # Asegúrate de que el nombre del archivo y la clase sean correctos

class TestListaOrdenada(unittest.TestCase):
    
    def setUp(self):
        """Método para configurar la lista antes de cada prueba"""
        self.lista = Lista_ordenada.of(lambda x: x)  # Lista ordenada con criterio de orden lambda x: x

    def test_añadir_y_ordenar(self):
        """Prueba que los elementos se añadan y ordenen correctamente"""
        # Añadir los elementos 3, 1, 2
        self.lista.add(3)
        self.lista.add(1)
        self.lista.add(2)
        
        # Verificar el resultado
        self.assertEqual(self.lista.elements(), [1, 2, 3])

    def test_eliminar_elemento(self):
        """Prueba de eliminar el primer elemento con remove()"""
        self.lista.add(3)
        self.lista.add(1)
        self.lista.add(2)
        
        # Eliminar el primer elemento
        removed_element = self.lista.remove()
        
        # Verificar el elemento eliminado
        self.assertEqual(removed_element, 1)
        self.assertEqual(self.lista.elements(), [2, 3])

    def test_eliminar_todos_los_elementos(self):
        """Prueba de eliminar todos los elementos con remove_all()"""
        self.lista.add(3)
        self.lista.add(1)
        self.lista.add(2)
        
        # Eliminar todos los elementos
        removed_elements = self.lista.remove_all()
        
        # Verificar los elementos eliminados
        self.assertEqual(removed_elements, [1, 2, 3])
        self.assertTrue(self.lista.is_empty())

    def test_posicion_correcta_al_agregar(self):
        """Comprobar si los números se añaden en la posición correcta"""
        self.lista.add(3)
        self.lista.add(1)
        self.lista.add(2)

        # Añadir nuevos elementos
        self.lista.add(0)  # Debería ir al principio
        self.assertEqual(self.lista.elements(), [0, 1, 2, 3])
        
        self.lista.add(10)  # Debería ir al final
        self.assertEqual(self.lista.elements(), [0, 1, 2, 3, 10])
        
        self.lista.add(7)  # Debería ir antes de 10
        self.assertEqual(self.lista.elements(), [0, 1, 2, 3, 7, 10])

# Ejecutar las pruebas
if __name__ == '__main__':
    unittest.main()
