class ElementoSistema:
    def __init__(self, nombre):
        self.nombre = nombre

class Archivo(ElementoSistema):
    def __init__(self, nombre, tamaño):
        super().__init__(nombre)
        self.tamaño = tamaño

class Carpeta(ElementoSistema):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.elementos = []

    def agregar_elemento(self, elemento):
        self.elementos.append(elemento)

    def listar_contenido(self):
        return [e.nombre for e in self.elementos]
