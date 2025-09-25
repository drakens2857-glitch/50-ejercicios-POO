class Vehiculo:
    def __init__(self, tipo, capacidad):
        self.tipo = tipo
        self.capacidad = capacidad

class Ruta:
    def __init__(self, origen, destino, distancia):
        self.origen = origen
        self.destino = destino
        self.distancia = distancia

class Ticket:
    def __init__(self, pasajero, vehiculo, ruta, precio):
        self.pasajero = pasajero
        self.vehiculo = vehiculo
        self.ruta = ruta
        self.precio = precio
