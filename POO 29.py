class Recurso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.reservas = []

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre

class Reserva:
    def __init__(self, recurso, usuario, fecha):
        self.recurso = recurso
        self.usuario = usuario
        self.fecha = fecha
        recurso.reservas.append(self)
