from .tarea import Tarea
from colorama import Fore
from helpers import imprimir_mensaje
from utils import obtener_opcion, obtener_indice
import textwrap


class ListaTareas:
    def __init__(self):
        """
        Inicializa una lista vacía de tareas.
        """
        self.tareas = []

    def agregar_tarea(self):
        """
        Agrega una nueva tarea a la lista de tareas pendientes.
        """
        descripcion = input(Fore.YELLOW + "Ingrese la descripción de la nueva tarea: " + Fore.RESET)
        imprimir_mensaje("Tarea añadida con éxito.", Fore.GREEN)
        nueva_tarea = Tarea(descripcion)
        self.tareas.append(nueva_tarea)

    def marcar_tarea_completada(self):
        """
        Marca una tarea como completada.
        """
        if not self.tareas:
            imprimir_mensaje("No hay tareas para marcar como completadas.", Fore.RED)
            return
        
        self.mostrar_tareas()
        print("\n")
        indice = obtener_indice(len(self.tareas))
        if indice is not None:
            self.tareas[indice - 1].marcar_completada()
            imprimir_mensaje("Tarea marcada como completada.", Fore.GREEN)

    def mostrar_tareas(self):
        """
        Muestra todas las tareas pendientes, numeradas y con su estado.
        """
        if not self.tareas:
            imprimir_mensaje("No hay tareas en la lista.", Fore.RED)
        else:
            imprimir_mensaje("Lista de Tareas", Fore.YELLOW)
            ancho_fijo = 39  # Longitud fija para la línea completa
            for i, tarea in enumerate(self.tareas, 1):
                estado = "[Completada]" if tarea.completada else "[Pendiente]"
                estado_color = Fore.GREEN if tarea.completada else Fore.RED
                descripcion_corta = textwrap.shorten(tarea.descripcion, width=ancho_fijo - len(estado) - 5, placeholder="...")
                linea = f"{i}. {descripcion_corta}"
                print(f"{linea: <{ancho_fijo - len(estado)}} {estado_color}{estado}")

    def eliminar_tarea(self):
        """
        Elimina una tarea de la lista.
        """
        if not self.tareas:
            imprimir_mensaje("No hay tareas para eliminar.", Fore.RED)
            return
        
        self.mostrar_tareas()
        print("\n")
        indice = obtener_indice(len(self.tareas))
        if indice is not None:
            del self.tareas[indice - 1]
            imprimir_mensaje("Tarea eliminada con éxito.", Fore.GREEN)
