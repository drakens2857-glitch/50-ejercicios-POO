class Perfil:
    def __init__(self, usuario):
        self.usuario = usuario
        self.historial = []

    def reproducir(self, contenido):
        self.historial.append(contenido)

class Contenido:
    def __init__(self, titulo, genero):
        self.titulo = titulo
        self.genero = genero

class Recomendacion:
    def __init__(self, perfil):
        self.perfil = perfil

    def sugerir(self):
        generos = [c.genero for c in self.perfil.historial]
        return max(set(generos), key=generos.count) if generos else None
