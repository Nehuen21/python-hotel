"""
Servicio Concreto para HabitacionDoble.
"""

from python_hotel.servicios.habitaciones.habitacion_base_service import HabitacionBaseService
from python_hotel.patrones.strategy.impl.mantenimiento_estandar_strategy import MantenimientoEstandarStrategy
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_hotel.entidades.habitaciones.habitacion_doble import HabitacionDoble


class HabitacionDobleService(HabitacionBaseService):
    """
    Servicio concreto con la logica de negocio para HabitacionDoble.
    """

    def __init__(self):
        """
        Inyecta la estrategia especifica (MantenimientoEstandarStrategy)
        en el constructor de la clase padre.
        """
        # --- INYECCION DE DEPENDENCIA ---
        super().__init__(MantenimientoEstandarStrategy())
        
    def mostrar_datos(self, habitacion: 'HabitacionDoble') -> None:
        """Muestra todos los datos de la habitacion doble."""
        super().mostrar_datos(habitacion) # Llama al padre (HabitacionBaseService)
        print(f"Desayuno:     {'Incluido' if habitacion.tiene_desayuno_incluido() else 'No incluido'}")