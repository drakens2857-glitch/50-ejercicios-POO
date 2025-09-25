class Proyecto:
    def __init__(self, nombre):
        self.nombre = nombre
        self.tareas = []
        self.equipo = []

class Tarea:
    def __init__(self, descripcion, responsable):
        self.descripcion = descripcion
        self.responsable = responsable
        self.completada = False

class Miembro:
    def __init__(self, nombre):
        self.nombre = nombre

class Equipo:
    def __init__(self):
        self.miembros = []

    def agregar_miembro(self, miembro):
        self.miembros.append(miembro)
