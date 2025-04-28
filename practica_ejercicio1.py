class PilaCaracteres:
    def __init__(self):
        self.pila = []

    def agregar(self, caracter):
        if len(caracter) == 1:  # Verificar que sea un solo carácter
            self.pila.append(caracter)
        else:
            raise ValueError("Solo se pueden agregar caracteres individuales.")

    def eliminar(self):
        if not self.esta_vacia():
            return self.pila.pop()
        else:
            raise IndexError("La pila está vacía.")

    def esta_vacia(self):
        return len(self.pila) == 0

    def invertir_cadena(self, texto):
        for caracter in texto:
            self.agregar(caracter)
        texto_invertido = ""
        while not self.esta_vacia():
            texto_invertido += self.eliminar()
        return texto_invertido


# Clase principal para interactuar con el usuario
if __name__ == "__main__":
    pila = PilaCaracteres()
    texto = input("Ingrese una cadena de texto: ")
    texto_invertido = pila.invertir_cadena(texto)
    print(f"Texto invertido: {texto_invertido}")