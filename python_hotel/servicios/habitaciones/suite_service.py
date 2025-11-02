"""
Servicio Concreto para Suite.
"""

from python_hotel.servicios.habitaciones.habitacion_service import HabitacionService
from python_hotel.patrones.strategy.impl.mantenimiento_premium_strategy import MantenimientoPremiumStrategy
from python_hotel.constantes import MANTENIMIENTO_PREMIUM_SUITE
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_hotel.entidades.habitaciones.suite import Suite


class SuiteService(HabitacionService):
    """
    Servicio concreto con la logica de negocio para Suite.
    """

    def __init__(self):
        """
        Inyecta la estrategia Premium, pasando el tiempo constante (60 min)
        desde el archivo de constantes.
        """
        # --- INYECCION DE DEPENDENCIA ---
        super().__init__(MantenimientoPremiumStrategy(MANTENIMIENTO_PREMIUM_SUITE))
        
    def mostrar_datos(self, habitacion: 'Suite') -> None:
        """Muestra todos los datos de la suite."""
        super().mostrar_datos(habitacion) # Llama al padre (HabitacionService)
        print(f"Amenities:    {', '.join(habitacion.get_amenities())}")
        print(f"Room Service: {'24h' if habitacion.tiene_room_service_24h() else 'No disponible'}")