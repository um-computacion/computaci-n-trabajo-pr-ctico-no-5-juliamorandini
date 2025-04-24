import unittest
from src.profesor import Profesor

class TestProfesor(unittest.TestCase):
    def test_crear_profesor(self):
        profesor = Profesor("Juan", "Pérez", "12345678", 50000)
        self.assertEqual(profesor.nombre, "Juan")
        self.assertEqual(profesor.apellido, "Pérez")
        self.assertEqual(profesor.dni, "12345678")
        self.assertEqual(profesor.sueldo, 50000)

    def test_repr_profesor(self):
        profesor = Profesor("Juan", "Pérez", "12345678", 50000)
        expected = "Profesor: DNI: 12345678 Nombre: Juan Apellido: Pérez Sueldo: 50000"
        self.assertEqual(str(profesor), expected)

#mas tests de nuevo, quiero ver si no se me esta pasando nada
    def test_invalid_dni(self):
        with self.assertRaises(ValueError):
            Profesor("Juan", "Pérez", "", 50000)

    def test_negative_sueldo(self):
        with self.assertRaises(ValueError):
            Profesor("Juan", "Pérez", "12345678", -1000)

    def test_actualizar_sueldo(self):
        profesor = Profesor("Ana", "García", "87654321", 40000)
        profesor.sueldo = 45000
        self.assertEqual(profesor.sueldo, 45000)

    def test_repr_special_characters(self):
        profesor = Profesor("José", "O'Connor", "98765432", 60000)
        expected = "Profesor: DNI: 98765432 Nombre: José Apellido: O'Connor Sueldo: 60000"
        self.assertEqual(str(profesor), expected)

    def test_empty_nombre_apellido(self):
        profesor = Profesor("", "", "00000000", 30000)
        expected = "Profesor: DNI: 00000000 Nombre:  Apellido:  Sueldo: 30000"
        self.assertEqual(str(profesor), expected)

if __name__ == "__main__":
    unittest.main()


# python -m tests.test_profesor