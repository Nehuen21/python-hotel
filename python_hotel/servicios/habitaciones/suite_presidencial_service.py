"""
Servicio Concreto para SuitePresidencial.
"""

from python_hotel.servicios.habitaciones.habitacion_service import HabitacionService
from python_hotel.patrones.strategy.impl.mantenimiento_premium_strategy import MantenimientoPremiumStrategy
from python_hotel.constantes import MANTENIMIENTO_PREMIUM_PRESIDENCIAL
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_hotel.entidades.habitaciones.suite_presidencial import SuitePresidencial


class SuitePresidencialService(HabitacionService):
    """
    Servicio concreto con la logica de negocio para SuitePresidencial.
    """

    def __init__(self):
        """
        Inyecta la estrategia Premium, pasando el tiempo constante (90 min)
        desde el archivo de constantes.
        """
        # --- INYECCION DE DEPENDENCIA ---
        super().__init__(MantenimientoPremiumStrategy(MANTENIMIENTO_PREMIUM_PRESIDENCIAL))
        
    def mostrar_datos(self, habitacion: 'SuitePresidencial') -> None:
        """Muestra todos los datos de la suite presidencial."""
        super().mostrar_datos(habitacion) # Llama al padre (HabitacionService)
        print(f"Amenities:    {', '.join(habitacion.get_amenities())}")
        print(f"Terraza:      {'Si' if habitacion.tiene_terraza() else 'No'}")