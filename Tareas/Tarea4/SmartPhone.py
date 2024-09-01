class SmartPhone:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
    def __str__(self):
        return f"{self.marca} {self.modelo} -${self.precio}"