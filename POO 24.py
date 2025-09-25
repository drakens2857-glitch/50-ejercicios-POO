class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
        self.movimientos = []

    def depositar(self, monto):
        self.saldo += monto
        self.movimientos.append(f"Depósito: +{monto}")

    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            self.movimientos.append(f"Retiro: -{monto}")
        else:
            self.movimientos.append("Retiro fallido: fondos insuficientes")

    def transferir(self, monto, otra_cuenta):
        if monto <= self.saldo:
            self.retirar(monto)
            otra_cuenta.depositar(monto)
            self.movimientos.append(f"Transferencia a {otra_cuenta.titular}: -{monto}")
        else:
            self.movimientos.append("Transferencia fallida: fondos insuficientes")
