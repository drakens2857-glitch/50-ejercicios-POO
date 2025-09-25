class Cuenta:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
        self.transacciones = []

    def depositar(self, monto):
        self.saldo += monto
        self.transacciones.append(Transaccion("Depósito", monto))

    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            self.transacciones.append(Transaccion("Retiro", -monto))

class Transaccion:
    def __init__(self, tipo, monto):
        self.tipo = tipo
        self.monto = monto

class Tarjeta:
    def __init__(self, numero, tipo):
        self.numero = numero
        self.tipo = tipo  # débito o crédito

class Prestamo:
    def __init__(self, monto, interes, plazo):
        self.monto = monto
        self.interes = interes
        self.plazo = plazo

    def calcular_total(self):
        return self.monto * (1 + self.interes / 100)
