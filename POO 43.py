class Producto:
    def __init__(self, nombre, stock):
        self.nombre = nombre
        self.stock = stock

class Proveedor:
    def __init__(self, nombre):
        self.nombre = nombre

class Orden:
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad

class Almacen:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def predecir_stock(self, producto, ventas_diarias):
        return producto.stock - ventas_diarias * 7  # predicción semanal
