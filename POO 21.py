class ProductoCarrito:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def subtotal(self):
        return self.precio * self.cantidad

class CarritoCompras:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def total(self):
        return sum(p.subtotal() for p in self.productos)
