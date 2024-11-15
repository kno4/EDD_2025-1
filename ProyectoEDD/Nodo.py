class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

    def __str__(self):
        return f"Valor:{self.valor}, H_I: {str(self.izquierdo)}, H_D: {str(self.derecho)};"