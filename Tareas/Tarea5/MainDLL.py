from Tareas.Tarea5.DoubleLinkedList import DoubleLinkedList


def main():
    lista = DoubleLinkedList()

    lista.agregar_al_inicio(50)
    lista.agregar_al_final(60)
    lista.agregar_al_final(65)
    lista.agregar_al_final(70)
    lista.agregar_al_final(80)
    lista.agregar_al_final(90)

    print("Contenido de la lista:", lista.transversal())

    lista.eliminar(2)
    print("Después de eliminar el elemento en la posición 2:", lista.transversal())

    lista.actualizar(3, 88)
    print("Después de actualizar el cuarto elemento a 88:", lista.transversal())

    posicion = lista.buscar(80)
    if posicion != -1:
        print(f"El valor 80 se encuentra en la posición: {posicion}")
    else:
        print("El valor 80 no se encuentra en la lista")


if __name__ == "__main__":
    main()