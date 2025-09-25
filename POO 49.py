class Datos:
    def __init__(self, entradas, salidas):
        self.entradas = entradas
        self.salidas = salidas

class Modelo:
    def __init__(self, tipo):
        self.tipo = tipo
        self.entrenado = False

class Entrenamiento:
    def __init__(self, modelo, datos):
        self.modelo = modelo
        self.datos = datos

    def ejecutar(self):
        self.modelo.entrenado = True

class Prediccion:
    def __init__(self, modelo, entrada):
        self.modelo = modelo
        self.entrada = entrada

    def resultado(self):
        return "Predicción generada" if self.modelo.entrenado else "Modelo no entrenado"
