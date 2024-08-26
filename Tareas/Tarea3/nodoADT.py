class NodoADT:
    def __init__(self, dato = None, siguiente = None):
        self.dato = dato
        self.siguiente = siguiente

    def __str__(self):
        return f'{self.dato} {self.siguiente}'

