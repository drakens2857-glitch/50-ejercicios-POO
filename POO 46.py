class Freelancer:
    def __init__(self, nombre, habilidades):
        self.nombre = nombre
        self.habilidades = habilidades
        self.reputacion = 0

class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre

class Proyecto:
    def __init__(self, titulo, descripcion, cliente):
        self.titulo = titulo
        self.descripcion = descripcion
        self.cliente = cliente
        self.freelancer = None

class Transaccion:
    def __init__(self, proyecto, monto):
        self.proyecto = proyecto
        self.monto = monto
