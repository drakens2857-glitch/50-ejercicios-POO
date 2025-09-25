class CuentaBanco:
    def __init__(self, saldo_inicial=0):
        self.__saldo = saldo_inicial

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
            print(f" Depósito exitoso: ${monto}")
        else:
            print(" El monto debe ser positivo.")

    def retirar(self, monto):
        if monto <= 0:
            print(" El monto debe ser positivo.")
        elif monto > self.__saldo:
            print(" Fondos insuficientes.")
        else:
            self.__saldo -= monto
            print(f" Retiro exitoso: ${monto}")

    def consultar_saldo(self):
        print(f" Saldo actual: ${self.__saldo}")
        return self.__saldo

cuenta = CuentaBanco(100000000000)
cuenta.depositar(50000)
cuenta.retirar(3000)
