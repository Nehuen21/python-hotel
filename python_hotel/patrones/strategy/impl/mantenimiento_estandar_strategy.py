"""
Estrategia Concreta: Mantenimiento Estandar.

Aplica para HabitacionSimple y HabitacionDoble.
"""

from python_hotel.patrones.strategy.mantenimiento_strategy import MantenimientoStrategy
from python_hotel.constantes import (
    MANTENIMIENTO_ESTANDAR_BASICO,
    MANTENIMIENTO_ESTANDAR_COMPLETO,
    UMBRAL_OCUPACION_ESTANDAR
)
from datetime import date
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_hotel.entidades.habitaciones.habitacion import Habitacion

class MantenimientoEstandarStrategy(MantenimientoStrategy):
    """
    Estrategia concreta para habitaciones estandar (Simple, Doble).

    El tiempo de mantenimiento es variable:
    - Si la ocupacion del ala es baja (< 30%), se hace limpieza completa (60 min).
    - Si la ocupacion es alta (>= 30%), se hace limpieza basica (30 min).
    """

    def calcular_mantenimiento(
        self,
        fecha: date,
        ocupacion_actual_ala: float,
        habitacion: 'Habitacion'
    ) -> int:
        """
        Calcula el tiempo de mantenimiento (en minutos) basado en la ocupacion.

        Args:
            fecha: Fecha actual (ignorado en esta estrategia).
            ocupacion_actual_ala: Nivel de ocupacion del ala (0.0 a 100.0).
            habitacion: La habitacion a mantener (ignorada en esta estrategia).

        Returns:
            El tiempo total en minutos requerido.
        """
        
        # Logica condicional basada en la ocupacion
        if ocupacion_actual_ala < UMBRAL_OCUPACION_ESTANDAR:
            # Baja ocupacion -> Limpieza completa
            return MANTENIMIENTO_ESTANDAR_COMPLETO
        else:
            # Alta ocupacion -> Limpieza basica
            return MANTENIMIENTO_ESTANDAR_BASICO