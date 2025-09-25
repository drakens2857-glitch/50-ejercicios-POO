class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre

    def calcular_pago(self):
        pass

class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, salario_mensual):
        super().__init__(nombre)
        self.salario_mensual = salario_mensual

    def calcular_pago(self):
        return self.salario_mensual

class EmpleadoMedioTiempo(Empleado):
    def __init__(self, nombre, horas, tarifa):
        super().__init__(nombre)
        self.horas = horas
        self.tarifa = tarifa

    def calcular_pago(self):
        return self.horas * self.tarifa
