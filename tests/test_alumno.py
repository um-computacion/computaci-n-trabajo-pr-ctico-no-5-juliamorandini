import unittest
from src.alumno import Alumno

class TestAlumno(unittest.TestCase):
    def test_crear_alumno(self):
        alumno = Alumno("Juan", "Pérez", "12345678", "A123")
        self.assertEqual(alumno.nombre, "Juan")
        self.assertEqual(alumno.apellido, "Pérez")
        self.assertEqual(alumno.dni, "12345678")
        self.assertEqual(alumno.legajo, "A123")

    def test_repr_alumno(self):
        alumno = Alumno("Juan", "Pérez", "12345678", "A123")
        expected = "Alumno: DNI: 12345678 Nombre: Juan Apellido: Pérez Legajo: A123"
        self.assertEqual(str(alumno), expected)

#mas tests falla siempre con el dni
    def test_invalid_dni(self):
        with self.assertRaises(ValueError):
            Alumno("Juan", "Pérez", "", "A123")

    def test_invalid_legajo(self):
        with self.assertRaises(ValueError):
            Alumno("Juan", "Pérez", "12345678", "")

    def test_empty_nombre_apellido(self):
        alumno = Alumno("", "", "12345678", "A123")
        expected = "Alumno: DNI: 12345678 Nombre:  Apellido:  Legajo: A123"
        self.assertEqual(str(alumno), expected)

    def test_repr_special_characters(self):
        alumno = Alumno("José", "O'Connor", "98765432", "B456")
        expected = "Alumno: DNI: 98765432 Nombre: José Apellido: O'Connor Legajo: B456"
        self.assertEqual(str(alumno), expected)

    def test_actualizar_legajo(self):
        alumno = Alumno("Ana", "García", "87654321", "C789")
        alumno.legajo = "D101"
        self.assertEqual(alumno.legajo, "D101")

if __name__ == "__main__":
    unittest.main()


#python -m tests.test_alumno