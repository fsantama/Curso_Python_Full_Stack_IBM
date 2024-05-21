from colorama import Fore
from helpers import imprimir_mensaje

def obtener_opcion():
    """
    Solicita al usuario que ingrese una opción y la devuelve como un entero.
    """
    while True:
        opcion = input(Fore.YELLOW + "Seleccione una opción: " + Fore.RESET).strip()
        if opcion.isdigit():
            opcion_entero = int(opcion)
            if 1 <= opcion_entero <= 5:
                return opcion_entero
            else:
                imprimir_mensaje("Error: Por favor, seleccione una opción del 1 al 5.", Fore.RED)
        else:
            imprimir_mensaje("Error: Ingrese un número entero.", Fore.RED)


def obtener_indice(num_tareas):
    """
    Solicita al usuario que ingrese un índice y lo devuelve como un entero.
    Verifica que el índice esté dentro del rango de tareas.
    
    Parámetros:
    num_tareas (int): El número total de tareas actuales.
    """
    while True:
        indice = input(Fore.YELLOW + "Ingrese el índice de la tarea: " + Fore.RESET).strip()
        if indice.isdigit():
            indice_correcto = int(indice)
            if 1 <= indice_correcto <= num_tareas:
                return indice_correcto
            else:
                imprimir_mensaje(f"Error: Por favor, seleccione un índice entre 1 y {num_tareas}.", Fore.RED)
        else:
            imprimir_mensaje("Error: Ingrese un número entero.", Fore.RED)
