from Tareas.ArbolBinarioDeBusqueda.ArbolBinarioDeBusqueda import ArbolBinarioDeBusqueda
from Tareas.ArbolBinarioDeBusqueda.Empleado import Empleado


def main():
    arbol = ArbolBinarioDeBusqueda()
    arbol.insertar(Empleado(5, "Eva", "H", 35, 16000))
    arbol.insertar(Empleado(2, "Sebas", "G", 26, 13000))
    arbol.insertar(Empleado(3, "Santi", "P", 29, 1500))
    arbol.insertar(Empleado(6, "Sandra", "L", 27, 15000))

    print("Arbol Binario DeBusqueda:", arbol.en_orden())
    arbol.imprimir_arbol()


if __name__ == '__main__':
    main()