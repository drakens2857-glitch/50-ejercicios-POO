class Paciente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.historial = []

class Doctor:
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad

class Cita:
    def __init__(self, paciente, doctor, fecha):
        self.paciente = paciente
        self.doctor = doctor
        self.fecha = fecha

class Receta:
    def __init__(self, paciente, medicamentos):
        self.paciente = paciente
        self.medicamentos = medicamentos
        paciente.historial.append(self)
