"""
Estrategia Concreta: Mantenimiento Premium.

Aplica para Suite y SuitePresidencial.
"""

from python_hotel.patrones.strategy.mantenimiento_strategy import MantenimientoStrategy
from datetime import date
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_hotel.entidades.habitaciones.habitacion import Habitacion

class MantenimientoPremiumStrategy(MantenimientoStrategy):
    """
    Estrategia concreta para habitaciones premium (Suite, Presidencial).

    El tiempo de mantenimiento es siempre constante, independientemente
    de la ocupacion. El tiempo exacto (ej. 60 o 90 min) se inyecta
    en el constructor.
    """

    def __init__(self, tiempo_constante_minutos: int):
        """
        Args:
            tiempo_constante_minutos: El tiempo fijo (ej. 60 para Suite).
        """
        if tiempo_constante_minutos <= 0:
            raise ValueError("El tiempo de mantenimiento debe ser positivo.")
        self._tiempo_constante = tiempo_constante_minutos

    def calcular_mantenimiento(
        self,
        fecha: date,
        ocupacion_actual_ala: float,
        habitacion: 'Habitacion'
    ) -> int:
        """
        Calcula el tiempo de mantenimiento (en minutos).

        Args:
            fecha: Fecha actual (ignorado).
            ocupacion_actual_ala: Nivel de ocupacion (ignorado).
            habitacion: La habitacion a mantener (ignorado).

        Returns:
            El tiempo total en minutos (siempre el valor constante).
        """
        
        # La logica es simple: siempre retorna el valor constante
        return self._tiempo_constante