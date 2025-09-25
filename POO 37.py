class Curso:
    def __init__(self, titulo):
        self.titulo = titulo
        self.modulos = []

class Modulo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.lecciones = []

class Leccion:
    def __init__(self, titulo, contenido):
        self.titulo = titulo
        self.contenido = contenido

class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.progreso = {}

    def completar_leccion(self, curso, leccion):
        self.progreso.setdefault(curso.titulo, []).append(leccion.titulo)

    def obtener_certificado(self, curso):
        completadas = self.progreso.get(curso.titulo, [])
        total = sum(len(m.lecciones) for m in curso.modulos)
        return "Certificado otorgado" if len(completadas) == total else "Curso incompleto"
