class ListaTareas:
    def __init__(self):
        self.tareas = []

    def agregar(self, tarea):
        self.tareas.append({"tarea": tarea, "completada": False})

    def eliminar(self, indice):
        if 0 <= indice < len(self.tareas):
            self.tareas.pop(indice)

    def marcar_completada(self, indice):
        if 0 <= indice < len(self.tareas):
            self.tareas[indice]["completada"] = True

    def mostrar_tareas(self):
        for i, t in enumerate(self.tareas):
            estado = "✔" if t["completada"] else "✘"
            print(f"{i+1}. {t['tarea']} - {estado}")

lista = ListaTareas()
lista.agregar("Comprar leche")
lista.agregar("Lavar ropa")
lista.marcar_completada(0)
lista.mostrar_tareas()