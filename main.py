from menu import mostrar_menu
from utils import obtener_opcion, obtener_indice
from models.lista_tareas import ListaTareas
from colorama import init, Fore

init(autoreset=True)

def main():
    """
    Función principal que maneja la interacción con el usuario.
    """
    lista_tareas = ListaTareas()
    opcion = None
    
    while opcion != 5:
        mostrar_menu()
        opcion = obtener_opcion()
        
        if opcion == 1:
            lista_tareas.agregar_tarea()
        elif opcion == 2:
            lista_tareas.marcar_tarea_completada()
        elif opcion == 3:
            lista_tareas.mostrar_tareas()
        elif opcion == 4:
            lista_tareas.eliminar_tarea()
        elif opcion == 5:
            print(Fore.RED + "Saliendo del gestor de tareas.")

if __name__ == "__main__":
    main()
