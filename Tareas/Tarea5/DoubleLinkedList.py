from Tareas.Tarea5.NodoDoble import NodoDoble


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.tamanio = 0

    def esta_vacia(self):
        return self.head is None

    def get_tamanio(self):
        return self.tamanio

    def agregar_al_inicio(self, dato):
        nuevo_nodo = NodoDoble(dato, None, None)
        if self.esta_vacia():
            self.head = self.tail = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.head
            self.head.anterior = nuevo_nodo
            self.tail = nuevo_nodo
        self.tamanio += 1

    def agregar_al_final(self, dato):
        nuevo_nodo = NodoDoble(dato)
        if self.esta_vacia():
            self.head = self.tail = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.tail
            self.tail.siguiente = nuevo_nodo
            self.tail = nuevo_nodo
        self.tamanio += 1

    def agregar_despues_de(self, referencia, dato):
        if self.esta_vacia():
            raise Exception("La lista esta vacia")
        actual = self.head
        while actual and actual.dato != referencia:
            actual = actual.siguiente
        if actual is None:
            raise Exception("Referencia no encontrada")
        nuevo_nodo = NodoDoble(dato)
        nuevo_nodo.siguiente = actual.siguiente
        nuevo_nodo.anterior = actual
        if actual.siguiente:
            actual.siguiente.anterior = nuevo_nodo
        actual.siguiente = nuevo_nodo
        if actual == self.tail:
            self.tail = nuevo_nodo
        self.tamanio += 1

    def obtener(self, posicion):
        if posicion < 0 or posicion >= self.tamanio:
            raise IndexError("Índice fuera de rango")
        actual = self.head
        for _ in range(posicion):
            actual = actual.siguiente
        return actual.valor

    def eliminar_primero(self):
        if self.esta_vacia():
            raise Exception("La lista esta vacia")
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.siguiente
            self.head.anterior = None
        self.tamanio -= 1

    def eliminar_ultimo(self):
        if self.esta_vacia():
            raise Exception("La lista esta vacia")
        if self.head == self.tail:
            self.tail = self.head = None
        else:
            self.tail = self.tail.anterior
            self.tail.siguiente = None
        self.tamanio -= 1

    def eliminar(self, posicion):
        if posicion < 0 or posicion >= self.tamanio:
            raise IndexError("La posicion no es valida")
        if posicion == 0:
            self.eliminar_primero()
            return
        if posicion == self.tamanio -1:
            self.eliminar_ultimo()
            return
        actual = self.head
        for _ in range(posicion):
            actual = actual.siguiente
        actual.anterior.siguiente = actual.siguiente
        actual.siguiente.anterior = actual.anterior
        self.tamanio -= 1

    def buscar(self, valor):
        actual = self.head
        posicion = 0
        while actual:
            if actual.dato == valor:
                return posicion
            actual = actual.siguiente
            posicion += 1
        print("El valor que busca no se encuentra en la lista")
        return -1

    def actualizar(self, posicion, nuevo_dato):
        if posicion < 0 or posicion >= self.tamanio:
            print("Posición no válida")
            return False
        aux = self.head
        for _ in range(posicion):
            aux = aux.get_siguiente()
        aux.set_dato(nuevo_dato)
        return True

    def transversal(self, direccion='izquierda'):
        elementos =[]
        if direccion == 'izquierda':
            actual = self.head
            while actual:
                elementos.append(actual.dato)
                actual = actual.siguiente
        else:
            actual = self.tail
            while actual:
                elementos.append(actual.dato)
                actual = actual.anterior
        return elementos



