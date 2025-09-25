class Paciente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.historial = []

class Doctor:
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad

class Cita:
    def __init__(self, paciente, doctor, fecha, diagnostico=None):
        self.paciente = paciente
        self.doctor = doctor
        self.fecha = fecha
        self.diagnostico = diagnostico
        paciente.historial.append(self)
