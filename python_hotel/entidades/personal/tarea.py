"""
Modulo de la Entidad: Tarea.

Representa una tarea asignada a un empleado.
"""

from datetime import date

class Tarea:
    """
    Entidad que representa una tarea de mantenimiento o limpieza.
    """

    def __init__(self, id_tarea: int, fecha_programada: date, descripcion: str):
        """
        Inicializa una Tarea.

        Args:
            id_tarea: ID unico de la tarea.
            fecha_programada: Dia en que debe realizarse.
            descripcion: Descripcion de la tarea (ej. "Limpiar Suite 101").
        """
        if id_tarea <= 0:
            raise ValueError("El ID de la tarea debe ser positivo.")
        if not descripcion:
            raise ValueError("La descripcion no puede ser nula o vacia.")

        self._id_tarea: int = id_tarea
        self._fecha_programada: date = fecha_programada
        self._descripcion: str = descripcion
        self._estado: str = "Pendiente" # Estados: Pendiente, Completada

    # --- Getters ---

    def get_id_tarea(self) -> int:
        return self._id_tarea

    def get_fecha_programada(self) -> date:
        return self._fecha_programada

    def get_descripcion(self) -> str:
        return self._descripcion

    def get_estado(self) -> str:
        return self._estado

    # --- Setters ---

    def set_estado(self, estado: str) -> None:
        """Actualiza el estado de la tarea (ej. "Completada")."""
        if not estado:
            raise ValueError("El estado no puede ser nulo o vacio.")
        self._estado = estado

    def __str__(self) -> str:
        return (
            f"Tarea ID: {self._id_tarea} ({self._descripcion}) - "
            f"Fecha: {self._fecha_programada} - Estado: {self._estado}"
        )