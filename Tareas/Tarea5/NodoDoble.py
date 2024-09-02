class NodoDoble:
    def __init__(self, dato, anterior = None, siguiente = None):
        self.dato = dato
        self.anterior = None
        self.siguiente = None

    def get_dato(self):
        return self.dato

    def get_anterior(self):
        return self.anterior

    def get_siguiente(self):
        return self.siguiente

    def set_dato(self, dato):
        self.dato = dato

    def set_anterior(self, anterior):
        self.anterior = anterior

    def set_siguiente(self, siguiente):
        self.siguiente = siguiente

    def __str__(self):
        print(f"dato: {self.dato}, anterior: {self.anterior}, siguiente: {self.siguiente}")