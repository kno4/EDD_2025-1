from Tareas.Tarea9.StackADT import Stack


def balanced(expresion):
    stack = Stack()
    signos_apert = "{("
    cierre_signos = "})"
    match_signos = {")":"(", "}":"{"}

    for char in expresion:
        if char in signos_apert:
            stack.push(char)
        elif char in cierre_signos:
            if stack.esta_vacia() or stack.pop() != match_signos[char]:
                return False
    return stack.esta_vacia()

