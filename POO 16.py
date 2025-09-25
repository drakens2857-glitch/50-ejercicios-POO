class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def info(self):
        return f"{self.marca} {self.modelo}"

class Carro(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas

    def info(self):
        return f"Carro: {super().info()}, {self.puertas} puertas"

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo

    def info(self):
        return f"Motocicleta: {super().info()}, tipo {self.tipo}"

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, marchas):
        super().__init__(marca, modelo)
        self.marchas = marchas

    def info(self):
        return f"Bicicleta: {super().info()}, {self