class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre

class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.productos = []
        self.descuento = 0

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def aplicar_descuento(self, porcentaje):
        self.descuento = porcentaje

    def total(self):
        subtotal = sum(p.precio for p in self.productos)
        return subtotal * (1 - self.descuento / 100)
