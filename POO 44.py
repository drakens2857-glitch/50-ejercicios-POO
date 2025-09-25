import random

class Empresa:
    def __init__(self, nombre, precio_inicial):
        self.nombre = nombre
        self.precio = precio_inicial

    def actualizar_precio(self):
        cambio = random.uniform(-0.05, 0.05)
        self.precio *= (1 + cambio)

class Portafolio:
    def __init__(self):
        self.inversiones = []

    def agregar(self, empresa, cantidad):
        self.inversiones.append((empresa, cantidad))

    def rendimiento_total(self):
        return sum(e.precio * c for e, c in self.inversiones)

class Transaccion:
    def __init__(self, empresa, cantidad, tipo):
        self.empresa = empresa
        self.cantidad = cantidad
        self.tipo = tipo  # compra o venta
