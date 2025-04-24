# Trabajo Práctico 5: Programación Orientada a Objetos con TDD

## Información del Estudiante
- **Nombre**: Julia
- **Apellido**: Morandini
- **Legajo**: 64234

## Objetivos
- Implementar una jerarquía de clases utilizando herencia
- Practicar el desarrollo guiado por pruebas (TDD)
- Aplicar conceptos de Programación Orientada a Objetos
- Utilizar control de versiones de manera efectiva

## Descripción General
En este trabajo práctico, implementaremos un sistema simple de gestión de personas en una institución educativa. El sistema permitirá manejar diferentes tipos de personas (personas comunes, profesores y alumnos) con sus características específicas.

## Metodología TDD
Seguiremos el ciclo TDD (Test-Driven Development) en cada etapa:
1. **Rojo**: Escribir una prueba que falle
2. **Verde**: Escribir el código mínimo necesario para que la prueba pase
3. **Refactor**: Mejorar el código manteniendo las pruebas pasando

### Ejemplo de Ciclo TDD
```python
# 1. Rojo: Escribir la prueba primero
class TestPersona(unittest.TestCase):
    def test_crear_persona(self):
        persona = Persona("Juan", "Pérez", "12345678")
        self.assertEqual(persona.nombre, "Juan")
        self.assertEqual(persona.apellido, "Pérez")
        self.assertEqual(persona.dni, "12345678")

# 2. Verde: Implementar el mínimo código necesario
class Persona:
    def __init__(self, nombre, apellido, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni

# 3. Refactor: Mejorar el código si es necesario
```

## Requisitos Previos
- Python 3.x
- unittest (incluido en la biblioteca estándar de Python)
- Git

## Etapas del Desarrollo

### Etapa 1: Configuración Inicial y Clase Base Persona
**Objetivo**: Crear la estructura básica del proyecto y la clase Persona.

1. Crear la estructura de directorios:
   ```
   src/
   tests/
   ```

2. **Rojo**: Crear el archivo de pruebas `tests/test_persona.py` con:
   ```python
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
   ```

3. **Verde**: Implementar en `src/persona.py`:
   ```python
   class Persona:
       def __init__(self, nombre, apellido, dni):
           self.nombre = nombre
           self.apellido = apellido
           self.dni = dni
           self.pensamientos = 0
           self.ultima_idea = "<no penso en nada>"

       def __repr__(self):
           return f"Persona: DNI: {self.dni} Nombre: {self.nombre} Apellido: {self.apellido} Ultima Idea: {self.ultima_idea}"
   ```

4. **Refactor**: Revisar y mejorar el código si es necesario

**Commit**: "Etapa 1: Implementación de la clase base Persona"

### Etapa 2: Agregar Comportamiento a Persona
**Objetivo**: Extender la funcionalidad de la clase Persona.

1. **Rojo**: Agregar pruebas en `tests/test_persona.py`:
   ```python
   def test_pensar_incrementa_contador(self):
       persona = Persona("Juan", "Pérez", "12345678")
       persona.pensar("Hola mundo")
       self.assertEqual(persona.pensamientos, 1)

   def test_pensar_actualiza_ultima_idea(self):
       persona = Persona("Juan", "Pérez", "12345678")
       persona.pensar("Hola mundo")
       self.assertEqual(persona.ultima_idea, "Hola mundo")
   ```

2. **Verde**: Implementar en `src/persona.py`:
   ```python
   def pensar(self, idea):
       self.pensamientos += 1
       self.ultima_idea = idea
   ```

3. **Refactor**: Revisar y mejorar el código si es necesario

**Commit**: "Etapa 2: Agregado comportamiento de pensamiento a Persona"

### Etapa 3: Implementar Clase Profesor
**Objetivo**: Crear la clase Profesor heredando de Persona.

1. **Rojo**: Crear archivo de pruebas `tests/test_profesor.py`:
   ```python
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
   ```

2. **Verde**: Implementar en `src/profesor.py`:
   ```python
   from src.persona import Persona

   class Profesor(Persona):
       def __init__(self, nombre, apellido, dni, sueldo):
           super().__init__(nombre, apellido, dni)
           self.sueldo = sueldo

       def __repr__(self):
           return f"Profesor: DNI: {self.dni} Nombre: {self.nombre} Apellido: {self.apellido} Sueldo: {self.sueldo}"
   ```

3. **Refactor**: Revisar y mejorar el código si es necesario

**Commit**: "Etapa 3: Implementación de la clase Profesor"

### Etapa 4: Implementar Clase Alumno
**Objetivo**: Crear la clase Alumno heredando de Persona.

1. **Rojo**: Crear archivo de pruebas `tests/test_alumno.py`:
   ```python
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
   ```

2. **Verde**: Implementar en `src/alumno.py`:
   ```python
   from src.persona import Persona

   class Alumno(Persona):
       def __init__(self, nombre, apellido, dni, legajo):
           super().__init__(nombre, apellido, dni)
           self.legajo = legajo

       def __repr__(self):
           return f"Alumno: DNI: {self.dni} Nombre: {self.nombre} Apellido: {self.apellido} Legajo: {self.legajo}"
   ```

3. **Refactor**: Revisar y mejorar el código si es necesario

**Commit**: "Etapa 4: Implementación de la clase Alumno"

### Etapa 5: Pruebas y Documentación
**Objetivo**: Completar el proyecto con pruebas unitarias y documentación.

1. **Rojo**: Implementar pruebas adicionales para:
   - Casos límite (valores vacíos, None, etc.)
   - Validación de datos (formato DNI, sueldo positivo, etc.)
   - Interacción entre clases

2. **Verde**: Implementar las validaciones necesarias

3. **Refactor**: Documentar el código con docstrings siguiendo el formato de Google:
   ```python
   def metodo(self, parametro):
       """Descripción del método.
       
       Args:
           parametro: Descripción del parámetro.
           
       Returns:
           Descripción del valor de retorno.
       """
   ```

4. Crear ejemplos de uso en `src/ejemplo.py`

**Commit**: "Etapa 5: Agregadas pruebas unitarias y documentación"

## Criterios de Evaluación
- Correcta implementación de la herencia
- Cobertura de pruebas unitarias (mínimo 80%)
- Calidad del código y documentación
- Uso correcto de control de versiones
- Respeto por los principios de TDD
- Correcta implementación de las pruebas usando unittest
- Seguimiento del ciclo rojo-verde-refactor en cada etapa

## Entrega
- Repositorio Git con todos los commits realizados
- Código fuente en el directorio `src/`
- Pruebas unitarias en el directorio `tests/`
- README.md actualizado con instrucciones de ejecución

## Notas
- Cada etapa debe ser completada y commiteada antes de pasar a la siguiente
- Las pruebas deben ser escritas antes de implementar la funcionalidad (TDD)
- Para ejecutar las pruebas:
  ```bash
  python -m unittest discover tests
  ```
- Recordar seguir el ciclo rojo-verde-refactor en cada etapa