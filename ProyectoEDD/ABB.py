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

    def buscar(self, valor):
        return self._buscar(valor, self.raiz)

    def _buscar(self, nodo_actual, valor):
        if nodo_actual is None:
            return False
        elif valor == nodo_actual.valor:
            return True
        elif valor < nodo_actual.valor:
            return self._buscar(nodo_actual.izquierdo, valor)
        else:
            return self._buscar(nodo_actual.derecho, valor)

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

    def _eliminar(self, nodo, valor):
        if nodo is None:
            return nodo

        if valor < nodo.valor:
            nodo.izquierdo = self._eliminar(nodo.izquierdo,valor)
        elif valor > nodo.valor:
            nodo.derecho = self._eliminar(nodo.derecho,valor)
        else:
             if nodo.izquierdo is None and nodo.derecho is None:
                 return nodo
             if nodo.izquierdo is None:
                 return nodo.derecho
             if nodo.derecho is None:
                 return nodo.izquierdo

             sucesor = self._encontrar_min(nodo.derecho)
             nodo.valor = sucesor.valor
             nodo.derecho = self._eliminar(nodo.derecho, sucesor.valor)
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
