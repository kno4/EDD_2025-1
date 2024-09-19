class Cliente:
    def __init__(self, nombre, perfil):
        self.nombre = nombre
        self.perfil = perfil

    def __str__(self):
        return f'Nombre: {self.nombre}, Perfil: {self.perfil}'
