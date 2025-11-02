"""
Modulo de la Entidad Concreta: Suite.
"""

from python_hotel.entidades.habitaciones.habitacion_premium import HabitacionPremium
from python_hotel.constantes import CAPACIDAD_SUITE, TARIFA_BASE_SUITE

class Suite(HabitacionPremium):
    """
    Entidad concreta que representa una Suite.
    """

    def __init__(self, room_service_24h: bool = True):
        """
        Inicializa una suite, definiendo sus amenities por defecto.
        """
        amenities_por_defecto = ["Jacuzzi", "Mini-bar", "Sala de estar"]
        
        super().__init__(
            capacidad=CAPACIDAD_SUITE,
            tarifa_base=TARIFA_BASE_SUITE,
            amenities=amenities_por_defecto
        )
        self._room_service_24h: bool = room_service_24h

    def tiene_room_service_24h(self) -> bool:
        """Retorna True si la suite tiene room service 24h."""
        return self._room_service_24h

    def get_tipo_habitacion(self) -> str:
        """Implementacion del metodo abstracto."""
        return "Suite"