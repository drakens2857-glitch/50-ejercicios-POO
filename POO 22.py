class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre

    def permisos(self):
        return []

class Administrador(Usuario):
    def permisos(self):
        return ["crear", "editar", "eliminar", "ver"]

class Cliente(Usuario):
    def permisos(self):
        return ["ver", "comprar"]

class Moderador(Usuario):
    def permisos(self):
        return ["ver", "moderar"]
