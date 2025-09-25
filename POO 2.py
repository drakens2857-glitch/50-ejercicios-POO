class Calculadora:

    def __init__(self):
        pass
    def suma(self, a, b):
        return a + b
    def resta(self, a, b):
        return a - b
    def multiplicacion(self, a, b):
        return a * b
    def division(self, a, b):
        if b == 0:
            return "No es posible dividir por cero."
        return a / b

calc = Calculadora()

print("La suma es:", calc.suma(10, 5))
print("La resta es:", calc.resta(8, 5))
print("La multiplicación es :", calc.multiplicacion(4, 5))
print("La división es valida:", calc.division(17, 5))
