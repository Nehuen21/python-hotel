"""
Modulo de la Entidad Concreta: HabitacionSimple.
"""

from python_hotel.entidades.habitaciones.habitacion_base import HabitacionBase
from python_hotel.constantes import CAPACIDAD_SIMPLE, TARIFA_BASE_SIMPLE

class HabitacionSimple(HabitacionBase):
    """
    Entidad concreta que representa una Habitacion Simple.
    Utiliza constantes para sus valores por defecto.
    """

    def __init__(self, servicios_basicos: bool = True):
        """
        Inicializa una habitacion simple, usando valores de constantes.py.
        """
        super().__init__(
            capacidad=CAPACIDAD_SIMPLE,
            tarifa_base=TARIFA_BASE_SIMPLE,
            servicios_basicos=servicios_basicos
        )
        # Atributo especifico de esta clase
        self._tamano_cama: str = "Individual"

    def get_tamano_cama(self) -> str:
        """Retorna el tamano de la cama."""
        return self._tamano_cama
    
    def get_tipo_habitacion(self) -> str:
        """Implementacion del metodo abstracto."""
        return "Simple"