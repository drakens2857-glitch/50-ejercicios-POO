class ContadorTexto:
    def __init__(self, texto):
        self.texto = texto

    def contar_palabras(self):
        return len(self.texto.split())

    def contar_caracteres(self):
        return len(self.texto)

    def contar_lineas(self):
        return len(self.texto.split("\n"))

texto = """Hola mundo.
Esto es una prueba.
Python es divertido."""
contador = ContadorTexto(texto)
print("Palabras:", contador.contar_palabras())
print("Caracteres:", contador.contar_caracteres())
print("Líneas:", contador.contar_lineas())
