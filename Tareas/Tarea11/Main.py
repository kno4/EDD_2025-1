from Tareas.Tarea9.StackADT import Stack


def elimin_elemento_medio(stack, n, actual= 0):

    if actual == n // 2:
        stack.pop()
        return

    elemento = stack.pop()
    elimin_elemento_medio(stack, n, actual + 1)
    stack.push(elemento)

def eliminar_medio(stack):
    n = stack.length()
    if n == 0:
        return
    elimin_elemento_medio(stack, n)

pila = Stack()
pila.push("Maria")
pila.push("Jimena")
pila.push("Cris")
pila.push("Selene")
pila.push("Fernanda")
pila.push("Bob")
pila.push("Miriam")
pila.push("Julia")

print("Pila antes de eliminar el valor de enmedio: ")
pila.__str__()

eliminar_medio(pila)

print("Pila después de eliminar el valor de enmedio")
pila.__str__()

print(".-.-.-.-.-.-.-.-.-.-.-.-.-.-.")

def suma_lista(lista):
    if not lista:
        return 0
    else:
        return lista[0] + suma_lista(lista[1:])

mi_lista = [1, 2, 3, 4, 5, 6, 7]
res = suma_lista(mi_lista)
print(f"La suma de la lista es: {res}")