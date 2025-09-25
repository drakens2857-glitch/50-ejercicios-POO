class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.publicaciones = []

    def publicar(self, contenido):
        self.publicaciones.append(Publicacion(self, contenido))

class Publicacion:
    def __init__(self, autor, contenido):
        self.autor = autor
        self.contenido = contenido
        self.comentarios = []
        self.likes = 0

    def comentar(self, usuario, texto):
        self.comentarios.append(Comentario(usuario, texto))

    def dar_like(self):
        self.likes += 1

class Comentario:
    def __init__(self, usuario, texto):
        self.usuario = usuario
        self.texto = texto
