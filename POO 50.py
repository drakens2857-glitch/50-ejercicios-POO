class Mundo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.objetos = []

class Objeto:
    def __init__(self, tipo, propiedades):
        self.tipo = tipo
        self.propiedades = propiedades

class Interaccion:
    def __init__(self, usuario, objeto, accion):
        self.usuario = usuario
        self.objeto = objeto
        self.accion = accion

class EconomiaVirtual:
    def __init__(self):
        self.transacciones = []

    def registrar_transaccion(self, usuario, monto):
        self.transacciones.append((usuario, monto))
