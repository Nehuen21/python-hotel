"""
Archivo integrador generado automaticamente
Directorio: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/patrones/strategy
Fecha: 2025-11-04 18:03:54
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/patrones/strategy/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: mantenimiento_strategy.py
# Ruta: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/patrones/strategy/mantenimiento_strategy.py
# ================================================================================

"""
Modulo de la Interfaz (ABC) para el Patron Strategy.

Define el contrato que todas las estrategias concretas de mantenimiento
deben implementar.
"""

from abc import ABC, abstractmethod
from datetime import date
from typing import TYPE_CHECKING

# Importacion solo para type hints
if TYPE_CHECKING:
    from python_hotel.entidades.habitaciones.habitacion import Habitacion

class MantenimientoStrategy(ABC):
    """
    Interfaz abstracta (ABC) para el patron Strategy.

    Define un algoritmo intercambiable para calcular el tiempo de
    mantenimiento de una habitacion.
    """

    @abstractmethod
    def calcular_mantenimiento(
        self,
        fecha: date,
        ocupacion_actual_ala: float,
        habitacion: 'Habitacion'
    ) -> int:
        """
        Calcula el tiempo de mantenimiento requerido (en minutos).

        Args:
            fecha: Fecha actual, por si la estrategia depende de la temporada.
            ocupacion_actual_ala: Nivel de ocupacion del ala (0.0 a 100.0).
            habitacion: La instancia de la habitacion a mantener.

        Returns:
            El tiempo total en minutos requerido para el mantenimiento.
        """
        pass

