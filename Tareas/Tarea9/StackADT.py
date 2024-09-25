class Stack:
    def __init__(self):
        self.dato = []

    def esta_vacia(self):
        return self.length() == 0

    def length(self):
        return len(self.dato)

    def pop(self):
        return self.dato.pop()

    def peek(self):
        return self.dato[-1]

    def push (self, dato):
        self.dato.append(dato)

    def __str__(self):
        info = "-----"
        for elem in self.dato[-1::-1]:
            print (" ",elem," ", "\n|---|")
