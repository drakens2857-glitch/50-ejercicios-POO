class Reloj:
    def __init__(self, hora, minuto, segundo):
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo

    def avanzar(self):
        self.segundo += 1
        if self.segundo == 60:
            self.segundo = 0
            self.minuto += 1
        if self.minuto == 60:
            self.minuto = 0
            self.hora += 1
        if self.hora == 24:
            self.hora = 0

    def mostrar(self):
        print(f"{self.hora:02d}:{self.minuto:02d}:{self.segundo:02d}")

reloj = Reloj(23, 59, 59)
reloj.avanzar()
reloj.mostrar()
