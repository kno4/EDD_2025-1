from ProyectoEDD.Nodo import Nodo

class ABB:

    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar(self.raiz, valor)

    def _insertar(self, nodo_actual, valor):
        if valor < nodo_actual.valor:
            if nodo_actual.izquierdo is None:
                nodo_actual.izquierdo = Nodo(valor)
            else:
                self._insertar(nodo_actual.izquierdo, valor)
        elif valor > nodo_actual.valor:
            if nodo_actual.derecho is None:
                nodo_actual.derecho = Nodo(valor)
            else:
                self._insertar(nodo_actual.derecho, valor)
        else:
            print("Este libro ya ha sido agregado")

    def buscar(self, libro):
        return self._buscar(self.raiz, libro.id)
    def _buscar(self, nodo_actual, id_libro):
        if nodo_actual is None:
            return False
        elif id_libro == nodo_actual.valor.id:
            return True
        elif id_libro < nodo_actual.valor.id:
            return self._buscar(nodo_actual.izquierdo, id_libro)
        else:
            return self._buscar(nodo_actual.derecho, id_libro)

    def recorrer_en_orden(self):
        elementos = []
        self._recorrer_en_orden(self.raiz, elementos)
        return elementos

    def _recorrer_en_orden(self, nodo_actual, elementos):
        if nodo_actual:
            self._recorrer_en_orden(nodo_actual.izquierdo, elementos)
            elementos.append(nodo_actual.izquierdo)
            self._recorrer_en_orden(nodo_actual.derecho, elementos)

    def eliminar(self, valor):
        self.raiz = self._eliminar(self.raiz, valor)

    def _eliminar(self, nodo, id_libro):
        if nodo is None:
            return nodo

        if id_libro < nodo.valor.id:  # Comparar por ID del libro
            nodo.izquierdo = self._eliminar(nodo.izquierdo, id_libro)
        elif id_libro > nodo.valor.id:  # Comparar por ID del libro
            nodo.derecho = self._eliminar(nodo.derecho, id_libro)
        else:
            # Nodo encontrado, proceder con eliminación
            if nodo.izquierdo is None and nodo.derecho is None:
                return None
            if nodo.izquierdo is None:
                return nodo.derecho
            if nodo.derecho is None:
                return nodo.izquierdo

            sucesor = self._encontrar_min(nodo.derecho)
            nodo.valor = sucesor.valor
            nodo.derecho = self._eliminar(nodo.derecho, sucesor.valor.id)  # Corregir aquí también
        return nodo

    @staticmethod
    def _encontrar_min(nodo):
        while nodo.izquierdo is not None:
            nodo = nodo.izquierdo
        return nodo

    def en_orden(self):
        elementos = []
        self._en_orden(self.raiz, elementos)
        return elementos

    def _en_orden(self, nodo_actual, elementos):
        if nodo_actual:
            self._en_orden(nodo_actual.izquierdo, elementos)
            elementos.append(nodo_actual.valor)
            self._en_orden(nodo_actual.derecho, elementos)

    def imprimir_arbol(self, nodo=None, nivel=0, prefijo="Raíz: "):
        nodo = nodo or self.raiz
        if nodo is not None:
            print(" " * (nivel * 4) + prefijo + str(nodo.valor))
            if nodo.izquierdo is not None or nodo.derecho is not None:
                if nodo.izquierdo:
                    self.imprimir_arbol(nodo.izquierdo, nivel + 1, "Izq: ")
                else:
                    print(" " * ((nivel + 1) * 4) + "Izq: None")
                if nodo.derecho:
                    self.imprimir_arbol(nodo.derecho, nivel + 1, "Der: ")
                else:
                    print(" " * ((nivel + 1) * 4) + "Der: None")
