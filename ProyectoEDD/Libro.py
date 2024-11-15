class Libro:
    def __init__(self, id, titulo, autor, stock, precio):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.stock = stock
        self.precio = precio

    def __lt__(self, other):
        return self.id < other.id

    def __gt__(self, other):
        return self.id > other.id

    def __eq__(self, other):
        return self.id == other.id

    def __str__(self):
        return f"{self.titulo} DE {self.autor}; PRECIO: {self.precio}, CANTIDAD EN STOCK: {self.stock}"