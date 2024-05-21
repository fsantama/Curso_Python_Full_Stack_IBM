from colorama import Fore

def imprimir_mensaje(mensaje, color):
    """
    Imprime un mensaje con un formato específico y color.
    
    Parámetros:
    mensaje (str): El mensaje a imprimir.
    color (str): El color del mensaje.
    """
    print("\n" + "-"*40)
    print(color + mensaje)
    print("-"*40)