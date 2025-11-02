"""
Servicio Base para Habitaciones Estandar (Simple, Doble).
"""

from python_hotel.servicios.habitaciones.habitacion_service import HabitacionService
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_hotel.entidades.habitaciones.habitacion_base import HabitacionBase

class HabitacionBaseService(HabitacionService):
    """
    Servicio intermedio para logica compartida por habitaciones
    estandar (Simple y Doble).
    """
    
    # No necesita __init__, ya que solo pasa la estrategia
    # que recibe de sus clases hijas (SimpleService, DobleService)
    # hacia el padre (HabitacionService).

    def mostrar_datos(self, habitacion: 'HabitacionBase') -> None:
        """
        Muestra datos base (de HabitacionService) y los especificos
        de HabitacionBase.
        """
        super().mostrar_datos(habitacion) # Llama al padre
        print(f"Serv. Basicos: {'Si' if habitacion.tiene_servicios_basicos() else 'No'}")