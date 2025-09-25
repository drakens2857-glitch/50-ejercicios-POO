class Producto:
    def __init__(self, nombre, categoria, stock):
        self.nombre = nombre
        self.categoria = categoria
        self.stock = stock

class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def buscar_por_categoria(self, categoria):
        return [p.nombre for p in self.productos if p.categoria == categoria]

    def reporte_stock(self):
        return {p.nombre: p.stock for p in self.productos}
