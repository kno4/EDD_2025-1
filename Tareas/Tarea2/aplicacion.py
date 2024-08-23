from Tareas.Tarea2.conjuntoADT import ConjuntoADT

def main():
    #crea tres conjuntos
    conjunto_a = ConjuntoADT()
    conjunto_b = ConjuntoADT()
    conjunto_c = ConjuntoADT()

    #agrega elementos
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

    #muestra los conjuntos iniciales
    print(f"Conjunto A: {conjunto_a}")
    print(f"Conjunto B: {conjunto_b}")
    print(f"Conjunto C: {conjunto_c}")

    #comprueba que pertenece a un conjunto
    elemento = "pera"
    print(f"¿Conjunto A contiene '{elemento}'? {'Sí' if conjunto_a.contiene(elemento) else 'No'}")

    #elimina de un conjunto (en este caso el "a")
    conjunto_a.eliminar((1, 2))
    print(f"Conjunto A después de eliminar (1, 2): {conjunto_a}")

    #imprime la longitud de los conjuntos
    print(f"Longitud de Conjunto A: {conjunto_a.longitud()}")
    print(f"Longitud de Conjunto B: {conjunto_b.longitud()}")
    print(f"Longitud de Conjunto C: {conjunto_c.longitud()}")

    #verifica si dos conjutos son iguales
    conjunto_d = ConjuntoADT()
    conjunto_d.agregar("pera")
    conjunto_d.agregar("naranja")
    conjunto_d.agregar(3.14)
    conjunto_d.agregar((3, 4))

    print(f"Conjunto B: {conjunto_b}")
    print(f"Conjunto D: {conjunto_d}")
    print(f"¿Conjunto B es igual a Conjunto D? {'Sí' if conjunto_b.equals(conjunto_d) else 'No'}")

    #comprueba si un conjunto es subconjunto de otro
    print(f"¿Conjunto C es subconjunto de Conjunto A? {'Sí' if conjunto_c.es_subconjunto(conjunto_a) else 'No'}")
    print(f"¿Conjunto A es subconjunto de Conjunto C? {'Sí' if conjunto_a.es_subconjunto(conjunto_c) else 'No'}")

    #operaciones entre conjuntos
    union_ab = conjunto_a.union(conjunto_b)
    interseccion_ab = conjunto_a.interseccion(conjunto_b)
    diferencia_ab = conjunto_a.diferencia(conjunto_b)

    print(f"Unión de Conjunto A y Conjunto B: {union_ab}")
    print(f"Intersección de Conjunto A y Conjunto B: {interseccion_ab}")
    print(f"Diferencia de Conjunto A y Conjunto B: {diferencia_ab}")

if __name__ == "__main__":
    main()
