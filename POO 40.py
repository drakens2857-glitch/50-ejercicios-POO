class Publicacion:
    def __init__(self, autor, contenido, privacidad):
        self.autor = autor
        self.contenido = contenido
        self.privacidad = privacidad  # 'público', 'amigos', 'privado'

    def puede_ver(self, usuario):
        if self.privacidad == 'público':
            return True
        elif self.privacidad == 'amigos':
            return usuario in self.autor.amigos
        elif self.privacidad == 'privado':
            return usuario == self.autor
        return False
