class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.carrito = Carrito()

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Carrito:
    def __init__(self):
        self.productos = []

    def agregar(self, producto):
        self.productos.append(producto)

    def total(self):
        return sum(p.precio for p in self.productos)

class Orden:
    def __init__(self, usuario):
        self.usuario = usuario
        self.total = usuario.carrito.total()

class Pago:
    def __init__(self, orden, metodo):
        self.orden = orden
        self.metodo = metodo

    def procesar(self):
        return f"Pago de ${self.orden.total} procesado con {self.metodo}"
