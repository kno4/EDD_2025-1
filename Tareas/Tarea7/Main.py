from Tareas.Tarea7.Ejercicio_cola import Gestion


def main():
    clinica = Gestion()

    clinica.registrar_paciente("Manuel Medrano")
    clinica.registrar_paciente("Cristina Salazar")
    clinica.registrar_paciente("Julian Chavez")

    clinica.mostrar_cola()
    clinica.mostrar_siguiente()
    clinica.atender_paciente()
    clinica.mostrar_siguiente()

    clinica.registrar_paciente("Gabriel Rodriguez")
    clinica.registrar_paciente("Mariana Torres")

    clinica.atender_paciente()
    clinica.mostrar_cola()

main()