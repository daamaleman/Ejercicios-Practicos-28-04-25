class ValidadorParentesis:
    def _init_(self):
        self.pila = []

    def es_balanceado(self, expresion):
        for caracter in expresion:
            if caracter == '(':
                self.pila.append(caracter)
            elif caracter == ')':
                if not self.pila: # Si la pila esta vacia
                    return False
                self.pila.pop() # Elimina el ultimo '('

        return len(self.pila) == 0

if _name_ == "_main_":
    validador = ValidadorParentesis()

    while True:
        print("Ingrese una expresion matematica:")
        expresion = input().strip()

        if validador.es_balanceado(expresion):
            print("✅ Los paréntesis están correctamente balanceados")
        else:
            print("❌ Los paréntesis NO están balanceados")
        
        # Limpiar la pila para la próxima expresión
        validador.pila = []