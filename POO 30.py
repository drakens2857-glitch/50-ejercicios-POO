class Personaje:
    def __init__(self, nombre, salud):
        self.nombre = nombre
        self.salud = salud
        self.habilidades = []
        self.inventario = []

    def usar_habilidad(self, habilidad, objetivo):
        daño = habilidad.usar()
        objetivo.salud -= daño

class Habilidad:
    def __init__(self, nombre, daño):
        self.nombre = nombre
        self.daño = daño

    def usar(self):
        return self.daño

class Item:
    def __init__(self, nombre, efecto):
        self.nombre = nombre
        self.efecto = efecto
