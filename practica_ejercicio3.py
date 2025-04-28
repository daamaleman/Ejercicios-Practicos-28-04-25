class HistorialNavegador:
    def __init__(self):
        self.historial = []

    def visitarPagina(self, url):
        """Agrega una nueva página al historial."""
        self.historial.append(url)
        print(f"Visitaste: {url}")

    def paginaActual(self):
        """Muestra la página en el tope de la pila."""
        if self.historial:
            return self.historial[-1]
        return "No hay páginas en el historial."

    def volverPaginaAnterior(self):
        """Elimina la página actual para volver a la anterior."""
        if self.historial:
            pagina = self.historial.pop()
            print(f"Regresaste desde: {pagina}")
        else:
            print("No hay páginas para regresar.")

# Clase Main para simular el uso del historial
def main():
    navegador = HistorialNavegador()
    while True:
        print("\nOpciones:")
        print("1. Visitar nueva página")
        print("2. Mostrar página actual")
        print("3. Volver a la página anterior")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            url = input("Ingresa la URL de la nueva página: ")
            navegador.visitarPagina(url)
        elif opcion == "2":
            print(f"Página actual: {navegador.paginaActual()}")
        elif opcion == "3":
            navegador.volverPaginaAnterior()
        elif opcion == "4":
            print("Saliendo del navegador...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    main()