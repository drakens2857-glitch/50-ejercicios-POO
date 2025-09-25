class Instrumento:
    def tocar(self):
        pass

class Guitarra(Instrumento):
    def tocar(self):
        return "🎸 Tocando acordes de guitarra"

class Piano(Instrumento):
    def tocar(self):
        return "🎹 Tocando melodía en piano"

class Bateria(Instrumento):
    def tocar(self):
        return "🥁 Tocando ritmo en batería"
