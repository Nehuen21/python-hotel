"""
Archivo integrador generado automaticamente
Directorio: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/patrones/strategy/impl
Fecha: 2025-11-04 18:03:54
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/patrones/strategy/impl/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: mantenimiento_estandar_strategy.py
# Ruta: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/patrones/strategy/impl/mantenimiento_estandar_strategy.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 3/3: mantenimiento_premium_strategy.py
# Ruta: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/patrones/strategy/impl/mantenimiento_premium_strategy.py
# ================================================================================

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

