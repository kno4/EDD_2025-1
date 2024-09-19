class ColaADT:
    def __init__(self):
        self.cola = []

    def esta_vacia(self):
        return len(self.cola) == 0

    def longitud(self):
        return len(self.cola)

    def frente(self):
        if self.esta_vacia():
            return None  # La cola está vacía
        return self.cola[0]

    def encolar(self, elem):
        self.cola.append(elem)

    def des_encolar(self):
        if self.esta_vacia():
            return None
        return self.cola.pop(0)

    def to_string(self):
        if self.esta_vacia():
            return "Cola vacía"
        return "Cola: " + " <- ".join(map(str, self.cola))
