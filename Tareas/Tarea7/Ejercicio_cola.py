from Tareas.Tarea7.ColaADT import ColaADT
from Tareas.Tarea7.Paciente import Paciente

class Gestion:
    def __init__(self):
        self.cola_pacientes = ColaADT()

    def registrar_paciente(self, nombre):
        paciente = Paciente(nombre)
        self.cola_pacientes.encolar(paciente)
        print(f"Paciente {nombre} registrado")

    def atender_paciente(self):
        if self.cola_pacientes.esta_vacia():
            print("No hay pacientes que atender")
        else:
            print(f"Atendiendo a: {self.cola_pacientes.frente()}")
            cola_paciente = self.cola_pacientes.des_encolar()

    def mostrar_cola(self):
        print(self.cola_pacientes.to_string())

    def mostrar_siguiente(self):
        if self.cola_pacientes.esta_vacia():
            print("No hay pacientes esperando")
        else:
            print(f"El siguiente paciente es {self.cola_pacientes.frente()}")

    def verificar_cola_vacia(self):
        if self.cola_pacientes.esta_vacia():
            print("No hay pacientes esperando")
        else:
            print("Hay pacientes esperando")
