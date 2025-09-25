import random

class Dado:
    def __init__(self, caras):
        self.caras = caras
        self.historial = []

    def lanzar(self):
        resultado = random.randint(1, self.caras)
        self.historial.append(resultado)
        return resultado

dado = Dado(6)
print("Lanzamiento:", dado.lanzar())
print("Historial:", dado.historial)
