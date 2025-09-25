class Candidato:
    def __init__(self, nombre, partido):
        self.nombre = nombre
        self.partido = partido
        self.votos = 0

class Votante:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula
        self.voto_emitido = False

class Eleccion:
    def __init__(self):
        self.candidatos = []
        self.votantes = []

    def registrar_candidato(self, candidato):
        self.candidatos.append(candidato)

    def registrar_votante(self, votante):
        self.votantes.append(votante)

    def votar(self, votante, candidato):
        if not votante.voto_emitido:
            candidato.votos += 1
            votante.voto_emitido = True
