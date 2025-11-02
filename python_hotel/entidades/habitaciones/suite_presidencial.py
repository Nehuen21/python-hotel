"""
Modulo de la Entidad Concreta: SuitePresidencial.
"""

from python_hotel.entidades.habitaciones.habitacion_premium import HabitacionPremium
from python_hotel.constantes import CAPACIDAD_PRESIDENCIAL, TARIFA_BASE_PRESIDENCIAL

class SuitePresidencial(HabitacionPremium):
    """
    Entidad concreta que representa una Suite Presidencial.
    """

    def __init__(self, tiene_terraza: bool = True):
        """
        Inicializa una suite presidencial.
        """
        amenities_por_defecto = [
            "Jacuzzi doble", 
            "Mini-bar premium", 
            "Sala de reuniones",
            "Servicio de mayordomo"
        ]
        
        super().__init__(
            capacidad=CAPACIDAD_PRESIDENCIAL,
            tarifa_base=TARIFA_BASE_PRESIDENCIAL,
            amenities=amenities_por_defecto
        )
        self._tiene_terraza: bool = tiene_terraza

    def tiene_terraza(self) -> bool:
        """Retorna True si la suite tiene terraza privada."""
        return self._tiene_terraza

    def get_tipo_habitacion(self) -> str:
        """Implementacion del metodo abstracto."""
        return "Presidencial"