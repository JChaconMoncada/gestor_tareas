import unittest
from main import agregar_tarea, listar_pendientes, completar_tarea

class TestGestorTareas(unittest.TestCase):

    def setUp(self):
        # Se ejecuta antes de cada prueba. Creamos una lista vacía.
        self.tareas_db = []

    def test_agregar_tarea(self):
        # Prueba 1: Verificar que la tarea se agrega y tiene estado pendiente
        self.tareas_db = agregar_tarea(self.tareas_db, "Estudiar", "Matemáticas Financieras", "28/02/2026")
        self.assertEqual(len(self.tareas_db), 1)
        self.assertEqual(self.tareas_db[0]['estado'], "pendiente")

    def test_listar_pendientes(self):
        # Prueba 2: Verificar que solo lista las pendientes
        self.tareas_db = agregar_tarea(self.tareas_db, "Tarea 1", "Desc 1", "01/03")
        self.tareas_db = agregar_tarea(self.tareas_db, "Tarea 2", "Desc 2", "02/03")
        self.tareas_db[0]['estado'] = 'completada' # Simulamos que una se completó
        
        pendientes = listar_pendientes(self.tareas_db)
        self.assertEqual(len(pendientes), 1)
        self.assertEqual(pendientes[0]['titulo'], "Tarea 2")

    def test_completar_tarea(self):
        # Prueba 3: Verificar el cambio de estado
        self.tareas_db = agregar_tarea(self.tareas_db, "Comprar pan", "Ir a la panadería", "Hoy")
        id_generado = self.tareas_db[0]['id']
        
        resultado = completar_tarea(self.tareas_db, id_generado)
        self.assertTrue(resultado)
        self.assertEqual(self.tareas_db[0]['estado'], "completada")

if __name__ == '__main__':
    unittest.main()