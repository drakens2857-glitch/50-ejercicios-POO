class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.calificaciones = []

    def agregar_nota(self, nota):
        self.calificaciones.append(nota)

    def promedio(self):
        if self.calificaciones:
            return sum(self.calificaciones) / len(self.calificaciones)
        else:
            return 0

alumno = Estudiante("Laura", 20)
alumno.agregar_nota(4.5)
alumno.agregar_nota(3.8)
print("Promedio:", alumno.promedio())
