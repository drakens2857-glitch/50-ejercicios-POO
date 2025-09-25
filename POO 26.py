class Materia:
    def __init__(self, nombre):
        self.nombre = nombre

class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.calificaciones = {}

    def agregar_calificacion(self, materia, nota):
        self.calificaciones[materia.nombre] = nota

    def promedio(self):
        if not self.calificaciones:
            return 0
        return sum(self.calificaciones.values()) / len(self.calificaciones)

    def estado_final(self):
        return "Aprobado" if self.promedio() >= 3.0 else "Reprobado"
