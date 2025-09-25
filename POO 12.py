class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print("Libro prestado.")
        else:
            print("No disponible.")

    def devolver(self):
        self.disponible = True
        print("Libro devuelto.")

libro = Libro("1984", "George Orwell", "123456789")
libro.prestar()
libro.devolver()
