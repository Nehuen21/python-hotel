"""
Modulo de la Entidad: AlaHotel.

Representa una seccion, ala o piso del hotel, que contiene las habitaciones
y gestiona un presupuesto.
"""

from python_hotel.constantes import PRESUPUESTO_INICIAL_ALA, PRESUPUESTO_MINIMO_OPERACION
from typing import TYPE_CHECKING

# Importaciones solo para type hints para evitar importacion circular
if TYPE_CHECKING:
    from python_hotel.entidades.habitaciones.habitacion import Habitacion
    from python_hotel.entidades.personal.empleado import Empleado


class AlaHotel:
    """
    Entidad que representa un ala o piso del hotel.
    Es responsable de gestionar la lista de habitaciones, empleados
    y el presupuesto para operaciones (ej. limpieza).
    """

    def __init__(self, nombre: str, capacidad: int, presupuesto: float = PRESUPUESTO_INICIAL_ALA):
        """
        Inicializa un Ala del Hotel.

        Args:
            nombre: Nombre identificatorio (ej. "Ala Norte", "Piso 5").
            capacidad: Capacidad maxima (en personas) de esta ala.
            presupuesto: Presupuesto inicial para operaciones.
        """
        if not nombre:
            raise ValueError("El nombre del ala no puede ser nulo o vacio.")
        if capacidad <= 0:
            raise ValueError("La capacidad debe ser mayor a cero.")

        self._nombre: str = nombre
        self._capacidad_maxima: int = capacidad
        self._presupuesto_disponible: float = presupuesto
        
        # Listas de entidades contenidas
        self._habitaciones: list['Habitacion'] = []
        self._empleados: list['Empleado'] = []

    # --- Getters ---

    def get_nombre(self) -> str:
        """Retorna el nombre del ala."""
        return self._nombre

    def get_capacidad_maxima(self) -> int:
        """Retorna la capacidad maxima total (en personas) del ala."""
        return self._capacidad_maxima

    def get_presupuesto_disponible(self) -> float:
        """Retorna el presupuesto actual del ala."""
        return self._presupuesto_disponible

    def get_habitaciones(self) -> list['Habitacion']:
        """Retorna una COPIA de la lista de habitaciones."""
        return self._habitaciones.copy()

    def get_empleados(self) -> list['Empleado']:
        """Retorna una COPIA de la lista de empleados."""
        return self._empleados.copy()

    def get_capacidad_ocupada(self) -> int:
        """
        Calcula y retorna la capacidad total (en personas)
        de las habitaciones ya configuradas.
        """
        return sum(h.get_capacidad() for h in self._habitaciones)

    def get_capacidad_disponible(self) -> int:
        """
        Calcula y retorna la capacidad (en personas) aun disponible
        para configurar nuevas habitaciones.
        """
        return self._capacidad_maxima - self.get_capacidad_ocupada()

    # --- Setters y Modificadores ---

    def set_presupuesto_disponible(self, monto: float) -> None:
        """Actualiza el presupuesto, validando que no sea negativo."""
        if monto < PRESUPUESTO_MINIMO_OPERACION:
            # Permitimos 0, pero no negativo
            raise ValueError("El presupuesto no puede ser negativo.")
        self._presupuesto_disponible = monto

    def add_habitacion(self, habitacion: 'Habitacion') -> None:
        """Agrega una habitacion a la lista del ala."""
        # La logica de negocio (validacion de capacidad)
        # ira en el AlaHotelService.
        self._habitaciones.append(habitacion)

    def set_empleados(self, empleados: list['Empleado']) -> None:
        """Reemplaza la lista de empleados asignados a esta ala."""
        # Se asigna una copia para evitar que modificaciones externas
        # afecten la lista interna.
        self._empleados = empleados.copy()

    def __str__(self) -> str:
        return (
            f"Ala: {self._nombre} (Capacidad: {self.get_capacidad_ocupada()}/{self._capacidad_maxima}) - "
            f"Presupuesto: ${self._presupuesto_disponible:.2f} - "
            f"{len(self._habitaciones)} habitaciones."
        )