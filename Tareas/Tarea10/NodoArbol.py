class NodoArbol:

    def __init__(self, valor, izq=None, der=None):
        self.valor = valor
        self.izq = izq
        self.der = der

    def __str__(self, nivel=0):
        resultado = " " * (4 * nivel) + str(self.valor) + "\n"

        if self.izq:
            resultado += self.izq.__str__(nivel + 1)
        else:
            resultado += " " * (4 * (nivel + 1)) + "None\n"

        if self.der:
            resultado += self.der.__str__(nivel + 1)
        else:
            resultado += " " * (4 * (nivel + 1)) + "None\n"

        return resultado