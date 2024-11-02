from Tareas.ArbolBinarioDeBusqueda.NodoArbolBinarioDeBusqueda import NodoArbolBinarioDeBusqueda


class ArbolBinarioDeBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = NodoArbolBinarioDeBusqueda(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo_actual, valor):
        if valor < nodo_actual.valor:
            if nodo_actual.izquierdo is None:
                nodo_actual.izquierdo = NodoArbolBinarioDeBusqueda(valor)
            else:
                self._insertar_recursivo(nodo_actual.izquierdo, valor)
        elif valor > nodo_actual.valor:
            if nodo_actual.derecho is None:
                nodo_actual.derecho = NodoArbolBinarioDeBusqueda(valor)
            else:
                self._insertar_recursivo(nodo_actual.derecho, valor)
        else:
            print("El valor ya esta en el Arbol")

    def buscar(self, valor):
        return self._buscar_recursivo(valor, self.raiz)

    def _buscar_recursivo(self, nodo_actual, valor):
        if nodo_actual is None:
            return False
        elif valor == nodo_actual.valor:
            return True
        elif valor < nodo_actual.valor:
            return self._buscar_recursivo(nodo_actual.izquierdo, valor)
        else:
            return self._buscar_recursivo(nodo_actual.derecho, valor)

    def recorrer_en_orden(self):
        elementos = []
        self._recorrer_en_orden_recursivo(self.raiz, elementos)
        return elementos

    def _recorrer_en_orden_recursivo(self, nodo_actual, elementos):
        if nodo_actual:
            self._recorrer_en_orden_recursivo(nodo_actual.izquierdo, elementos)
            elementos.append(nodo_actual.valor)
            self._recorrer_en_orden_recursivo(nodo_actual.derecho, elementos)

    def eliminar(self, valor):
        self.raiz = self._eliminar_recursivo(self.raiz, valor)

    def _eliminar_recursivo(self, nodo, valor):
        if nodo is None:
            return nodo

        if valor < nodo.valor:
            nodo.izquierdo = self._eliminar_recursivo(nodo.izquierdo, valor)
        elif valor > nodo.valor:
            nodo.derecho = self._eliminar_recursivo(nodo.derecho, valor)
        else:
            if nodo.izquierdo is None and nodo.derecho is None:
                return None


            if nodo.izquierdo is None:
                return nodo.derecho
            elif nodo.derecho is None:
                return nodo.izquierdo

            sucesor = self._encontrar_minimo(nodo.derecho)
            nodo.valor = sucesor.valor
            nodo.derecho = self._eliminar_recursivo(nodo.derecho, sucesor.valor)
        return nodo

    @staticmethod
    def _encontrar_minimo(nodo):
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





