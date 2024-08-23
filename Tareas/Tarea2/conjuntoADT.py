class ConjuntoADT:
    def __init__(self):
        self._elementos = []

    def longitud(self):
        """Devuelve el número de elementos en el conjunto."""
        return len(self._elementos)

    def contiene(self, elemento):
        """Devuelve True si el elemento está en el conjunto, False de lo contrario."""
        return elemento in self._elementos

    def agregar(self, elemento):
        """Agrega un elemento al conjunto si no está presente."""
        if not self.contiene(elemento):
            self._elementos.append(elemento)

    def eliminar(self, elemento):
        """Elimina el elemento del conjunto si está presente."""
        if self.contiene(elemento):
            self._elementos.remove(elemento)

    def equals(self, otro_conjunto):
        """Comprueba si el conjunto actual y otro_conjunto tienen los mismos elementos."""
        if self.longitud() != otro_conjunto.longitud():
            return False
        for elemento in self._elementos:
            if not otro_conjunto.contiene(elemento):
                return False
        return True

    def es_subconjunto(self, otro_conjunto):
        """Devuelve True si todos los elementos del conjunto están en otro_conjunto."""
        for elemento in self._elementos:
            if not otro_conjunto.contiene(elemento):
                return False
        return True

    def union(self, otro_conjunto):
        """Retorna un nuevo conjunto que es la unión del conjunto actual y otro_conjunto."""
        nuevo_conjunto = ConjuntoADT()
        # Agregar todos los elementos del conjunto actual
        nuevo_conjunto._elementos = self._elementos.copy()
        # Agregar todos los elementos del otro conjunto si no están ya presentes
        for elemento in otro_conjunto._elementos:
            if not nuevo_conjunto.contiene(elemento):
                nuevo_conjunto.agregar(elemento)
        return nuevo_conjunto

    def interseccion(self, otro_conjunto):
        """Retorna un nuevo conjunto que es la intersección del conjunto actual y otro_conjunto."""
        nuevo_conjunto = ConjuntoADT()
        for elemento in self._elementos:
            if otro_conjunto.contiene(elemento):
                nuevo_conjunto.agregar(elemento)
        return nuevo_conjunto

    def diferencia(self, otro_conjunto):
        """Retorna un nuevo conjunto con los elementos del conjunto actual que no están en otro_conjunto."""
        nuevo_conjunto = ConjuntoADT()
        for elemento in self._elementos:
            if not otro_conjunto.contiene(elemento):
                nuevo_conjunto.agregar(elemento)
        return nuevo_conjunto

    def __str__(self):
        """Devuelve una representación en cadena del conjunto."""
        return "{" + ", ".join(str(elemento) for elemento in self._elementos) + "}"
