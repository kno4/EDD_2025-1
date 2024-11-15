from ProyectoEDD.Libro import Libro
from ProyectoEDD.ABB import ABB
def main():

    abb = ABB()
    abb.insertar(Libro(1500, "Cien años de soledad", "Gabriel Garcia Marquez", 25, 650))
    abb.insertar(Libro(1250, "Cien años de soledad DELUXE", "Gabriel Garcia Marquez", 25, 950))



if __name__ == '__main__':
    main()