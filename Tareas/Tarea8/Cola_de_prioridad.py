from Tareas.Tarea7.ColaADT import ColaADT
from Tareas.Tarea8.Cliente_banco import Cliente


class ColaDePrioridad:
    def __init__(self, max_prioridad):
        self.max_prioridad = max_prioridad
        self.colas = [ColaADT() for _ in range(max_prioridad + 1)]

    def longitud(self):
        total = 0
        for cola in self.colas:
            total += cola.longitud()
        return total

    def esta_vacia(self):
        return self.longitud() == 0

    def encolar(self, prioridad, elemento):
        if 1 <= prioridad <= self.max_prioridad:
            self.colas[prioridad].encolar(elemento)

    def desencolar(self):
        if self.esta_vacia():
            print("No hay elementos")
        else:
            for cola in self.colas:
                if not cola.esta_vacia():
                    return cola.des_encolar()

    def __str__(self):
        result = []
        for i, cola in enumerate(self.colas):
            result.append(f"Prioridad {i}: {cola}")
        return "\n".join(result)

# Mapeo de perfiles a prioridades
PERFILES_PRIORIDAD = {
    "No es cliente": 5,
    "Cliente nuevo": 4,
    "Cliente frecuente": 3,
    "Cliente premium": 2,
    "Celebridad": 1
}

def main():
    cola = ColaDePrioridad(5)

    cliente1 = Cliente("Cliente1", "Cliente nuevo")
    cliente2 = Cliente("Cliente2", "Cliente nuevo")
    cola.encolar(PERFILES_PRIORIDAD[cliente1.perfil], cliente1)
    cola.encolar(PERFILES_PRIORIDAD[cliente2.perfil], cliente2)

    cliente3 = Cliente("Cliente3", "No es cliente")
    cliente4 = Cliente("Cliente4", "No es cliente")
    cliente5 = Cliente("Cliente5", "No es cliente")
    cola.encolar(PERFILES_PRIORIDAD[cliente3.perfil], cliente3)
    cola.encolar(PERFILES_PRIORIDAD[cliente4.perfil], cliente4)
    cola.encolar(PERFILES_PRIORIDAD[cliente5.perfil], cliente5)

    celebridad = Cliente("Celebridad 1", "Celebridad")
    cola.encolar(PERFILES_PRIORIDAD[celebridad.perfil],celebridad)

    print("Estado de la cola actual: ")
    print(cola)

    siguiente_cliente = cola.desencolar()
    if siguiente_cliente:
        print(f"Atendiendo a {siguiente_cliente}, retirando $10,000")

    cliente_frecuente = Cliente("Cliente 6", "Cliente frecuente")
    cliente_premium = Cliente("Cliente 7", "Cliente premium")
    cola.encolar(PERFILES_PRIORIDAD[cliente_frecuente.perfil], cliente_frecuente)
    cola.encolar(PERFILES_PRIORIDAD[cliente_premium.perfil], cliente_premium)

    siguiente_cliente = cola.desencolar()
    if siguiente_cliente:
        print(f"Atendiendo a {siguiente_cliente}")

    print("Estado de la cola despues de atender algunos clientes: ")
    print(cola)

    while not cola.esta_vacia():
        siguiente_cliente = cola.desencolar()
        if siguiente_cliente:
            print(f"Atendiendo a {siguiente_cliente}")

    print("Estado final de la cola: ")
    print(cola)

if __name__ == "__main__":
    main()
