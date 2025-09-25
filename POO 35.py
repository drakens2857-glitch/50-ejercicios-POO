class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.disponible = True

class Huesped:
    def __init__(self, nombre):
        self.nombre = nombre

class Reserva:
    def __init__(self, huesped, habitacion, dias):
        self.huesped = huesped
        self.habitacion = habitacion
        self.dias = dias
        self.total = habitacion.precio * dias
        habitacion.disponible = False

class Hotel:
    def __init__(self, nombre):
        self.nombre = nombre
        self.habitaciones = []

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    def habitaciones_disponibles(self):
        return [h for h in self.habitaciones if h.disponible]
