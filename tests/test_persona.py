import unittest
from src.persona import Persona

class TestPersona(unittest.TestCase):
    def test_crear_persona(self):
        persona = Persona("Juan", "Pérez", "12345678")
        self.assertEqual(persona.nombre, "Juan")
        self.assertEqual(persona.apellido, "Pérez")
        self.assertEqual(persona.dni, "12345678")

    def test_repr_persona(self):
        persona = Persona("Juan", "Pérez", "12345678")
        expected = "Persona: DNI: 12345678 Nombre: Juan Apellido: Pérez Ultima Idea: <no penso en nada>"
        self.assertEqual(str(persona), expected)

    def test_pensar_incrementa_contador(self):
        persona = Persona("Juan", "Pérez", "12345678")
        persona.pensar("Hola mundo")
        self.assertEqual(persona.pensamientos, 1)

    def test_pensar_actualiza_ultima_idea(self):
        persona = Persona("Juan", "Pérez", "12345678")
        persona.pensar("Hola mundo")
        self.assertEqual(persona.ultima_idea, "Hola mundo")

    def test_actualizar_ultima_idea(self):
        persona = Persona("Ana", "García", "87654321")
        persona.ultima_idea = "Aprender Python"
        expected = "Persona: DNI: 87654321 Nombre: Ana Apellido: García Ultima Idea: Aprender Python"
        self.assertEqual(str(persona), expected)

    def test_pensamientos_increment(self):
        persona = Persona("Luis", "Martínez", "11223344")
        persona.pensamientos += 1
        self.assertEqual(persona.pensamientos, 1)
        persona.pensamientos += 2
        self.assertEqual(persona.pensamientos, 3)

    def test_empty_nombre_apellido(self):
        persona = Persona("", "", "00000000")
        expected = "Persona: DNI: 00000000 Nombre:  Apellido:  Ultima Idea: <no penso en nada>"
        self.assertEqual(str(persona), expected)

    def test_invalid_dni(self):
        with self.assertRaises(ValueError):
            Persona("Juan", "Pérez", "")

    def test_pensar_empty_string(self):
        persona = Persona("Juan", "Pérez", "12345678")
        persona.pensar("")
        self.assertEqual(persona.ultima_idea, "")
        self.assertEqual(persona.pensamientos, 1)

    def test_repr_special_characters(self):
        persona = Persona("José", "O'Connor", "98765432")
        persona.pensar("¡Hola, mundo!")
        expected = "Persona: DNI: 98765432 Nombre: José Apellido: O'Connor Ultima Idea: ¡Hola, mundo!"
        self.assertEqual(str(persona), expected)

    def test_multiple_pensar_calls(self):
        persona = Persona("Juan", "Pérez", "12345678")
        persona.pensar("Idea 1")
        persona.pensar("Idea 2")
        self.assertEqual(persona.pensamientos, 2)
        self.assertEqual(persona.ultima_idea, "Idea 2")

if __name__ == "__main__":
    unittest.main()

#python -m tests.test_persona xq no detecta el src -_-