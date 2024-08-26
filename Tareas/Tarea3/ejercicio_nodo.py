from Tareas.Tarea3.nodoADT import NodoADT
def main():
    head_5 = NodoADT(600)
    head_4 = NodoADT(400, head_5)
    head_3 = NodoADT(300,head_4)
    head_2 = NodoADT(200,head_3)
    head = NodoADT(100, head_2)
    print(head)
    print("-----------------------")
    head_3.dato = 333
    print(head)
    print("-----------------------")
    head_6 =NodoADT(700)
    head_5.siguiente = head_6
    print(head)
    print("-----------------------")
    head_0 = NodoADT(50, head)
    print(head_0)
if __name__ == '__main__':
    main()


