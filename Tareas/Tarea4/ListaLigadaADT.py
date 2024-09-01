from Tareas.Tarea4.ListaLigada import ListaLigada
from Tareas.Tarea4.SmartPhone import SmartPhone
def main():
    lista_smartphones = ListaLigada()

    lista_smartphones.agregar_al_final(SmartPhone("Apple", "iPhone 14", 999))
    lista_smartphones.agregar_al_final(SmartPhone("Samsung", "Galaxy S21", 799))
    lista_smartphones.agregar_al_final(SmartPhone("Google", "Pixel 6", 599))
    lista_smartphones.agregar_al_final(SmartPhone("OnePlus", "9 Pro", 699))
    lista_smartphones.agregar_al_final(SmartPhone("Xiaomi", "Mi 11", 499))

    print("Contenido inicial de la lista:")
    lista_smartphones.transversal()

    lista_smartphones.eliminar(2)

    print("\nContenido después de eliminar el nodo en la posición 2:")
    lista_smartphones.transversal()

    nuevo_smartphone = SmartPhone("Sony", "Xperia 5", 899)
    lista_smartphones.actualizar(1, nuevo_smartphone)

    print("\nContenido después de actualizar el segundo elemento:")
    lista_smartphones.transversal()

    lista_smartphones.agregar_al_inicio(SmartPhone("Motorola", "Edge 20", 699))
    lista_smartphones.agregar_al_final(SmartPhone("Huawei", "P50 Pro", 999))

    print("\nContenido después de agregar al inicio y al final:")
    lista_smartphones.transversal()

    lista_smartphones.eliminar(0)

    print("\nContenido después de eliminar el primer nodo:")
    lista_smartphones.transversal()


if __name__ == '__main__':
    main()

