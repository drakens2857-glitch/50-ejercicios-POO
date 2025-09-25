class Producto:
    def __init__(self, codigo, nombre, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def aplicar_descuento(self, porcentaje):
        descuento = self.precio * (porcentaje / 100)
        self.precio -= descuento

p1 = Producto("A001", "Camiseta", 20000, 10)
p1.aplicar_descuento(20)
print("Nuevo precio:", p1.precio)
