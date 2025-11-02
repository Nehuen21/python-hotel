"""
Modulo de la Entidad: Empleado.

Representa a un miembro del personal del hotel. Reemplaza a 'Trabajador'.
"""
from __future__ import annotations
from typing import TYPE_CHECKING

# Importaciones solo para type hints para evitar importacion circular
if TYPE_CHECKING:
    from python_hotel.entidades.personal.certificacion import Certificacion
    from python_hotel.entidades.personal.tarea import Tarea

class Empleado:
    """
    Entidad que representa a un empleado del hotel.
    Contiene su informacion personal, su certificacion y sus tareas.
    """

    def __init__(self, dni: int, nombre: str, tareas: list['Tarea']):
        """
        Inicializa un Empleado.

        Args:
            dni: DNI unico del empleado.
            nombre: Nombre completo.
            tareas: Lista de tareas asignadas (puede estar vacia).
        """
        if dni <= 0:
            raise ValueError("El DNI debe ser un numero positivo.")
        if not nombre:
            raise ValueError("El nombre no puede ser nulo o vacio.")

        self._dni: int = dni
        self._nombre: str = nombre
        
        # Guardamos una copia para encapsulamiento
        self._tareas: list['Tarea'] = tareas.copy()
        
        # El empleado se crea sin certificacion, se asigna despues.
        self._certificacion: 'Certificacion' | None = None

    # --- Getters ---

    def get_dni(self) -> int:
        return self._dni

    def get_nombre(self) -> str:
        return self._nombre

    def get_certificacion(self) -> 'Certificacion' | None:
        """Retorna el objeto Certificacion o None si no esta asignado."""
        return self._certificacion

    def get_tareas(self) -> list['Tarea']:
        """Retorna una COPIA de la lista de tareas."""
        return self._tareas.copy()

    # --- Setters ---

    def set_certificacion(self, certificacion: 'Certificacion') -> None:
        """Asigna o actualiza la certificacion del empleado."""
        self._certificacion = certificacion
        
    def set_tareas(self, tareas: list['Tarea']) -> None:
        """Reemplaza la lista de tareas del empleado."""
        self._tareas = tareas.copy() # Guardar copia

    def __str__(self) -> str:
        certificado = "Certificado" if self._certificacion and self._certificacion.esta_certificacion_valida() else "No Certificado"
        return (
            f"Empleado: {self._nombre} (DNI: {self._dni}) - "
            f"Tareas: {len(self._tareas)} - Estado: {certificado}"
        )