from Tareas.Tarea9.Balance_parentesis import balanced


def main():
    expresion = "{(a+b) * (c - d)}"

    if balanced(expresion):
        print("Los parentesis SÍ estan balanceados")
    else:
        print("Los parentesis NO estan balanceados")

if __name__ == "__main__":
    main()