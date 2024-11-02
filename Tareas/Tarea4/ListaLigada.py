from Tareas.Tarea4.Nodo import Nodo

class ListaLigada:
    def __init__(self):
        self._cabeza = None
        self._tamanio = 0

    def tamanio(self):
        return self._tamanio

    def agregar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.esta_vacia():
            self._cabeza = nuevo_nodo
        else:
            aux = self._cabeza
            while aux.get_siguiente() is not None:
                aux = aux.get_siguiente()
            aux.set_siguiente(nuevo_nodo)
        self._tamanio += 1

    def esta_vacia(self):
        return self._cabeza is None


    def agregar_al_inicio(self, dato):
        nuevo_nodo = Nodo(dato,self._cabeza)
        self._cabeza = nuevo_nodo
        self._tamanio += 1

    def get_tamanio(self):
        aux = self._cabeza
        contador = 0
        while aux.get_siguiente() is not None:
            contador += 1
            aux = aux.get_siguiente()
        return contador

    def agregar_despues_de(self, ref, nuevo_dato):
        # Buscar el nodo_actual con el dato `nodo_anterior_dato`
        aux = self._cabeza
        while aux is not None:
            if aux.get_dato() == ref:
                break
            aux = aux.get_siguiente()

        if aux is None:
            print(f"Nodo con dato '{ref}' no encontrado.")
        else:
            # Crear el nuevo nodo_actual y ajustar los punteros
            nuevo_nodo = Nodo(nuevo_dato)
            nuevo_nodo.set_siguiente(aux.get_siguiente())
            aux.set_siguiente(nuevo_nodo)
            self._tamanio += 1

    def buscar(self, dato):
        aux = self._cabeza
        posicion = 0
        while aux is not None:
            if aux.get_dato() == dato:
                return posicion
            aux = aux.get_siguiente()
            posicion += 1
        # Devuelve -1 si el dato no se encuentra en la lista
        return -1

    def transversal(self):
        aux = self._cabeza
        while aux is not None:
            print(aux.get_dato(), "-->", end=" ")
            aux = aux.get_siguiente()
        print("\n")

    def eliminar(self, posicion):
        if posicion < 0 or posicion >= self._tamanio:
            print("Posición no válida")
            return

        if posicion == 0:
            self._cabeza = self._cabeza.get_siguiente()
        else:
            aux = self._cabeza
            for _ in range(posicion - 1):
                aux = aux.get_siguiente()
            aux.set_siguiente(aux.get_siguiente().get_siguiente())
        self._tamanio -= 1

    def actualizar(self, posicion, nuevo_dato):
        if posicion < 0 or posicion >= self._tamanio:
            print("Posición no válida")
            return False

        aux = self._cabeza
        for _ in range(posicion):
            aux = aux.get_siguiente()
        aux.set_dato(nuevo_dato)
        return True

    def eliminar_primero(self, dato):
            if self.esta_vacia():
                print("La lista está vacía, no se puede eliminar el primer nodo_actual.")
                return

            self._cabeza = self._cabeza.get_siguiente()
            self._tamanio -= 1

    def eliminar_ultimo(self):
        if self.esta_vacia():
            print("La lista está vacía, no se puede eliminar el último nodo_actual.")
            return

        #cuando solo haya un nodo_actual y sea la cabeza
        if self._cabeza.get_siguiente() is None:
            self._cabeza = None
        else:
            #Recorre la lista hasta encontrar el penúltimo nodo_actual
            aux = self._cabeza
            while aux.get_siguiente().get_siguiente() is not None:
                aux = aux.get_siguiente()
            aux.set_siguiente(None)
        self._tamanio -= 1


