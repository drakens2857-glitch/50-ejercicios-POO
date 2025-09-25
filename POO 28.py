from datetime import date, timedelta

class Libro:
    def __init__(self, titulo):
        self.titulo = titulo
        self.disponible = True

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.prestamos = []

class Prestamo:
    def __init__(self, libro, usuario):
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = date.today()
        self.fecha_devolucion = self.fecha_prestamo + timedelta(days=14)

    def calcular_multa(self):
        hoy = date.today()
        if hoy > self.fecha_devolucion:
            dias = (hoy - self.fecha_devolucion).days
            return dias * 1000  # multa por día
        return 0
