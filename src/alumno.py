from src.persona import Persona

class Alumno(Persona):
    def __init__(self, nombre, apellido, dni, legajo):
        super().__init__(nombre, apellido, dni)
        if not dni.isdigit():
            raise ValueError("DNI debe ser un número") #siempre el DNI hace que los tests fallen 
        if not legajo:
            raise ValueError("Legajo no puede estar vacío")
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.legajo = legajo

    def __repr__(self):
        return f"Alumno: DNI: {self.dni} Nombre: {self.nombre} Apellido: {self.apellido} Legajo: {self.legajo}"