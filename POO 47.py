class Paquete:
    def __init__(self, codigo, destino):
        self.codigo = codigo
        self.destino = destino

class Vehiculo:
    def __init__(self, tipo, capacidad):
        self.tipo = tipo
        self.capacidad = capacidad

class Ruta:
    def __init__(self, origen, destino, distancia):
        self.origen = origen
        self.destino = destino
        self.distancia = distancia

class Almacen:
    def __init__(self, ubicacion):
        self.ubicacion = ubicacion
        self.paquetes = []

    def recibir_paquete(self, paquete):
        self.paquetes.append(paquete)
