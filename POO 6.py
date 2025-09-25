class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto

    def perimetro(self):
        return 2 * (self.ancho + self.alto)

    def es_cuadrado(self):
        return self.ancho == self.alto

figura = Rectangulo(5, 5)
print("Área:", figura.area())
print("¿Es cuadrado?", figura.es_cuadrado())
