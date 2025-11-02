"""
Servicio Concreto para HabitacionSimple.
"""

from python_hotel.servicios.habitaciones.habitacion_base_service import HabitacionBaseService
from python_hotel.patrones.strategy.impl.mantenimiento_estandar_strategy import MantenimientoEstandarStrategy
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_hotel.entidades.habitaciones.habitacion_simple import HabitacionSimple


class HabitacionSimpleService(HabitacionBaseService):
    """
    Servicio concreto con la logica de negocio para HabitacionSimple.
    """

    def __init__(self):
        """
        Inyecta la estrategia especifica (MantenimientoEstandarStrategy)
        en el constructor de la clase padre.
        """
        # --- INYECCION DE DEPENDENCIA ---
        super().__init__(MantenimientoEstandarStrategy())
        
    def mostrar_datos(self, habitacion: 'HabitacionSimple') -> None:
        """Muestra todos los datos de la habitacion simple."""
        super().mostrar_datos(habitacion) # Llama al padre (HabitacionBaseService)
        print(f"Cama:         {habitacion.get_tamano_cama()}")