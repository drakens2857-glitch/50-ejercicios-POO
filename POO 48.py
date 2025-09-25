class Animal:
    def __init__(self, especie, dieta):
        self.especie = especie
        self.dieta = dieta

class Planta:
    def __init__(self, tipo):
        self.tipo = tipo

class Clima:
    def __init__(self, temperatura, humedad):
        self.temperatura = temperatura
        self.humedad = humedad

class CadenaAlimenticia:
    def __init__(self):
        self.relaciones = []

    def agregar_relacion(self, depredador, presa):
        self.relaciones.append((depredador, presa))
