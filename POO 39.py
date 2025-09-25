class Grupo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.miembros = []

class Evento:
    def __init__(self, titulo, fecha):
        self.titulo = titulo
        self.fecha = fecha

class Mensaje:
    def __init__(self, emisor, contenido):
        self.emisor = emisor
        self.contenido = contenido

class Notificacion:
    def __init__(self, usuario, mensaje):
        self.usuario = usuario
        self.mensaje = mensaje

class Privacidad:
    def __init__(self, nivel):
        self.nivel = nivel  # público, amigos, privado
