class Tarea:
    def __init__(self, descripcion):
        """
        Inicializa una nueva tarea con la descripción proporcionada y la marca como pendiente.
        """
        self.descripcion = descripcion
        self.completada = False

    def marcar_completada(self):
        """
        Marca la tarea como completada.
        """
        self.completada = True

    def __str__(self):
        """
        Devuelve una representación en cadena de la tarea, mostrando su estado (completada o pendiente).
        """
        estado = "Completada" if self.completada else "Pendiente"
        return f"{self.descripcion} [{estado}]"
