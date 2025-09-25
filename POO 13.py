class Temperatura:
    def __init__(self, valor):
        self.valor = valor

    def a_fahrenheit(self):
        return (self.valor * 9/5) + 32

    def a_kelvin(self):
        return self.valor + 273.15

temp = Temperatura(25)
print("Fahrenheit:", temp.a_fahrenheit())
print("Kelvin:", temp.a_kelvin())
