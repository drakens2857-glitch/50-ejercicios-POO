class Mascota:

    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    def presentarse(self):
        print(f"Hola, soy {self.nombre}, soy un {self.especie} y tengo {self.edad} años.")

mascota1 = Mascota("Luna", "hamster", 3)
mascota2 = Mascota("set", "loro", 5)
mascota3 = Mascota("Milo", "gato", 7)

mascota1.presentarse()
mascota2.presentarse()
mascota3.presentarse()
