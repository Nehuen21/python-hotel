"""
Modulo de la Entidad Concreta: HabitacionDoble.
"""

from python_hotel.entidades.habitaciones.habitacion_base import HabitacionBase
from python_hotel.constantes import CAPACIDAD_DOBLE, TARIFA_BASE_DOBLE

class HabitacionDoble(HabitacionBase):
    """
    Entidad concreta que representa una Habitacion Doble.
    """

    def __init__(self, servicios_basicos: bool = True, desayuno_incluido: bool = True):
        """
        Inicializa una habitacion doble.
        """
        super().__init__(
            capacidad=CAPACIDAD_DOBLE,
            tarifa_base=TARIFA_BASE_DOBLE,
            servicios_basicos=servicios_basicos
        )
        self._desayuno_incluido: bool = desayuno_incluido

    def tiene_desayuno_incluido(self) -> bool:
        """Retorna True si el desayuno esta incluido."""
        return self._desayuno_incluido

    def get_tipo_habitacion(self) -> str:
        """Implementacion del metodo abstracto."""
        return "Doble"