class Contacto:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono

class Agenda:
    def __init__(self):
        self.contactos = []

    def agregar(self, contacto):
        self.contactos.append(contacto)

    def buscar(self, nombre):
        for c in self.contactos:
            if c.nombre == nombre:
                return c.telefono
        return "No encontrado"

a = Agenda()
a.agregar(Contacto("Ana", "123456"))
print("Teléfono de Ana:", a.buscar("Ana"))
