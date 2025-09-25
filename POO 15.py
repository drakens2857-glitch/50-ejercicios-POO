class Semaforo:
    def __init__(self):
        self.estado = "rojo"

    def cambiar(self):
        if self.estado == "rojo":
            self.estado = "verde"
        elif self.estado == "verde":
            self.estado = "amarillo"
        else:
            self.estado = "rojo"

s = Semaforo()
s.cambiar()
print("Estado actual:", s.estado)
