import random

class Carta:
    def __init__(self, valor, palo):
        self.valor = valor
        self.palo = palo

    def mostrar(self):
        return f"{self.valor} de {self.palo}"

class Mazo:
    def __init__(self):
        valores = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        palos = ['Corazones', 'Diamantes', 'Tréboles', 'Picas']
        self.cartas = [Carta(v, p) for v in valores for p in palos]
        random.shuffle(self.cartas)

    def repartir(self):
        return self.cartas.pop() if self.cartas else None

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mano = []

    def recibir_carta(self, carta):
        self.mano.append(carta)

    def mostrar_mano(self):
        return [c.mostrar() for c in self.mano]
