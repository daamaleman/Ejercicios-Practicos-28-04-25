class Tarea:
    def __init__(self, nombre, descripcion, prioridad):
        self.nombre = nombre
        self.descripcion = descripcion
        self.prioridad = prioridad

    def __str__(self):
        return f"Tarea: {self.nombre}\nDescripción: {self.descripcion}\nPrioridad: {self.prioridad}"


class PilaTareas:
    def __init__(self):
        self.pila = []

    def push(self, tarea):
        self.pila.append(tarea)

    def pop(self):
        if not self.esta_vacia():
            return self.pila.pop()
        else:
            print("La pila está vacía.")
            return None

    def peek(self):
        if not self.esta_vacia():
            return self.pila[-1]
        else:
            print("La pila está vacía.")
            return None

    def esta_vacia(self):
        return len(self.pila) == 0


class Main:
    def ejecutar(self):
        pila_tareas = PilaTareas()

        # Pedir al usuario que ingrese tres tareas
        for i in range(3):
            print(f"Ingrese los datos de la tarea {i + 1}:")
            nombre = input("Nombre de la tarea: ")
            descripcion = input("Descripción de la tarea: ")
            prioridad = input("Prioridad de la tarea (Alta, Media, Baja): ")
            tarea = Tarea(nombre, descripcion, prioridad)
            pila_tareas.push(tarea)

        # Procesar tareas una a una
        print("\nProcesando tareas:")
        while not pila_tareas.esta_vacia():
            tarea_actual = pila_tareas.pop()
            print(tarea_actual)


if __name__ == "__main__":
    main = Main()
    main.ejecutar()
