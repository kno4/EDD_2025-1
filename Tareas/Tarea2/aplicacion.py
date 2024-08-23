from Tareas.Tarea2.conjuntoADT import ConjuntoADT

def main():
    # Crear tres conjuntos con diferentes tipos de datos
    conjunto_a = ConjuntoADT()
    conjunto_b = ConjuntoADT()
    conjunto_c = ConjuntoADT()

    # Agregar elementos de diferentes tipos a los conjuntos
    conjunto_a.agregar("manzana")
    conjunto_a.agregar(2.5)
    conjunto_a.agregar((1, 2))
    conjunto_a.agregar("pera")

    conjunto_b.agregar("pera")
    conjunto_b.agregar("naranja")
    conjunto_b.agregar(3.14)
    conjunto_b.agregar((3, 4))

    conjunto_c.agregar("manzana")
    conjunto_c.agregar(2.5)

    # Mostrar conjuntos iniciales
    print(f"Conjunto A: {conjunto_a}")
    print(f"Conjunto B: {conjunto_b}")
    print(f"Conjunto C: {conjunto_c}")

    # Comprobar pertenencia de un elemento
    elemento = "pera"
    print(f"¿Conjunto A contiene '{elemento}'? {'Sí' if conjunto_a.contiene(elemento) else 'No'}")

    # Eliminar un elemento de conjunto_a
    conjunto_a.eliminar((1, 2))
    print(f"Conjunto A después de eliminar (1, 2): {conjunto_a}")

    # Comprobar longitud de los conjuntos
    print(f"Longitud de Conjunto A: {conjunto_a.longitud()}")
    print(f"Longitud de Conjunto B: {conjunto_b.longitud()}")
    print(f"Longitud de Conjunto C: {conjunto_c.longitud()}")

    # Verificar igualdad de conjuntos
    conjuntoD = ConjuntoADT()
    conjuntoD.agregar("pera")
    conjuntoD.agregar("naranja")
    conjuntoD.agregar(3.14)
    conjuntoD.agregar((3, 4))

    print(f"Conjunto B: {conjunto_b}")
    print(f"Conjunto D: {conjuntoD}")
    print(f"¿Conjunto B es igual a Conjunto D? {'Sí' if conjunto_b.equals(conjuntoD) else 'No'}")

    # Comprobar subconjunto
    print(f"¿Conjunto C es subconjunto de Conjunto A? {'Sí' if conjunto_c.es_subconjunto(conjunto_a) else 'No'}")
    print(f"¿Conjunto A es subconjunto de Conjunto C? {'Sí' if conjunto_a.es_subconjunto(conjunto_c) else 'No'}")

    # Operaciones de conjuntos: unión, intersección y diferencia
    unionAB = conjunto_a.union(conjunto_b)
    interseccionAB = conjunto_a.interseccion(conjunto_b)
    diferenciaAB = conjunto_a.diferencia(conjunto_b)

    print(f"Unión de Conjunto A y Conjunto B: {unionAB}")
    print(f"Intersección de Conjunto A y Conjunto B: {interseccionAB}")
    print(f"Diferencia de Conjunto A y Conjunto B: {diferenciaAB}")

if __name__ == "__main__":
    main()
