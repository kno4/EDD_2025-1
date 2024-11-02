class Empleado:
    def __init__(self, id , nombre, apellido, edad, salario):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.salario = salario

    def __lt__(self, other):
        return self.id < other.id

    def __gt__(self, other):
        return self.id > other.id

    def __eq__(self, other):
        return self.id == other.id

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Salario: {self.salario}"