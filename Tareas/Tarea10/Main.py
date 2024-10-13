from Tareas.Tarea10.NodoArbol import NodoArbol


def main():
    arbol = NodoArbol(10, NodoArbol(5, NodoArbol(1)),NodoArbol(15, NodoArbol(25)))
    arbol2 = NodoArbol("Diego", NodoArbol("Pedro",NodoArbol("Susan"),NodoArbol("Diana")),NodoArbol("Mario"))
    print(arbol)
    print(arbol2)

if __name__ == "__main__":
    main()