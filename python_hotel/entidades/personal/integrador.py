"""
Archivo integrador generado automaticamente
Directorio: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/entidades/personal
Fecha: 2025-11-04 18:03:54
Total de archivos integrados: 5
"""

# ================================================================================
# ARCHIVO 1/5: __init__.py
# Ruta: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/entidades/personal/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/5: certificacion.py
# Ruta: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/entidades/personal/certificacion.py
# ================================================================================

"""
Modulo de la Entidad: Certificacion.

Representa la certificacion profesional de un empleado (ej. higiene,
mantenimiento electrico, etc.). Reemplaza a 'AptoMedico'.
"""

from datetime import date

class Certificacion:
    """
    Entidad que almacena los datos de una certificacion profesional.
    """

    def __init__(self, 
                 es_valida: bool, 
                 fecha_emision: date, 
                 especializacion: str,
                 observaciones: str = "Sin observaciones"):
        """
        Inicializa la certificacion.

        Args:
            es_valida: True si la certificacion esta vigente.
            fecha_emision: Cuando fue emitida.
            especializacion: El area de la certificacion (ej. "Limpieza Nivel 3").
            observaciones: Notas adicionales.
        """
        if not especializacion:
            raise ValueError("La especializacion no puede ser nula o vacia.")

        self._es_valida: bool = es_valida
        self._fecha_emision: date = fecha_emision
        self._especializacion: str = especializacion
        self._observaciones: str = observaciones

    # --- Getters ---

    def esta_certificacion_valida(self) -> bool:
        """Retorna True si la certificacion esta vigente y es valida."""
        return self._es_valida

    def get_fecha_emision(self) -> date:
        return self._fecha_emision
    
    def get_especializacion(self) -> str:
        return self._especializacion

    def get_observaciones(self) -> str:
        return self._observaciones

# ================================================================================
# ARCHIVO 3/5: empleado.py
# Ruta: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/entidades/personal/empleado.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 4/5: equipo_limpieza.py
# Ruta: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/entidades/personal/equipo_limpieza.py
# ================================================================================

"""
Modulo de la Entidad: EquipoLimpieza.

Representa el equipamiento fisico utilizado para tareas de limpieza
o mantenimiento. Reemplaza a 'Herramienta'.
"""

class EquipoLimpieza:
    """
    Entidad que representa una herramienta o equipo (ej. aspiradora, carro).
    """

    def __init__(self, id_equipo: int, nombre: str, certificado_higiene: bool):
        """
        Inicializa el equipo.

        Args:
            id_equipo: ID unico del equipo.
            nombre: Nombre del equipo (ej. "Aspiradora Industrial V-100").
            certificado_higiene: True si cumple con normas H&S.
        """
        if id_equipo <= 0:
            raise ValueError("El ID del equipo debe ser positivo.")
        if not nombre:
            raise ValueError("El nombre no puede ser nulo o vacio.")

        self._id_equipo: int = id_equipo
        self._nombre: str = nombre
        self._certificado_higiene: bool = certificado_higiene

    # --- Getters ---

    def get_id_equipo(self) -> int:
        return self._id_equipo

    def get_nombre(self) -> str:
        return self._nombre

    def tiene_certificado_higiene(self) -> bool:
        return self._certificado_higiene

    def __str__(self) -> str:
        return f"Equipo: {self._nombre} (ID: {self._id_equipo})"

# ================================================================================
# ARCHIVO 5/5: tarea.py
# Ruta: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/entidades/personal/tarea.py
# ================================================================================

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

