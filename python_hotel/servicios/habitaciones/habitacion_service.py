"""
Modulo del Servicio Base Abstracto para Habitaciones.

Define la funcionalidad comun para todos los servicios de habitacion,
incluyendo la logica del Patron Strategy.
"""

from abc import ABC, abstractmethod
from datetime import date
from typing import TYPE_CHECKING

# Importacion de la ABSTRACCION del patron
from python_hotel.patrones.strategy.mantenimiento_strategy import MantenimientoStrategy

if TYPE_CHECKING:
    from python_hotel.entidades.habitaciones.habitacion import Habitacion


class HabitacionService(ABC):
    """
    Servicio base abstracto (ABC) para la logica de negocio de Habitaciones.

    Contiene la logica de inyeccion de dependencias para el Patron Strategy.
    """

    def __init__(self, estrategia_mantenimiento: MantenimientoStrategy):
        """
        Inicializa el servicio base.

        Args:
            estrategia_mantenimiento: Una instancia de una clase que
                implemente la interfaz MantenimientoStrategy.
                (Esto es Inyeccion de Dependencias).
        """
        if not isinstance(estrategia_mantenimiento, MantenimientoStrategy):
            raise TypeError("El argumento debe ser una instancia de MantenimientoStrategy.")
        self._estrategia_mantenimiento = estrategia_mantenimiento

    def realizar_mantenimiento(self, habitacion: 'Habitacion', ocupacion_ala: float) -> int:
        """
        Realiza el mantenimiento de una habitacion.

        Esta es la funcion 'Contexto' del Patron Strategy.
        Delega el calculo del tiempo a la estrategia inyectada.

        Args:
            habitacion: La instancia de la habitacion a mantener.
            ocupacion_ala: El nivel de ocupacion actual del ala.

        Returns:
            El tiempo (en minutos) que tomo el mantenimiento.
        """
        from python_hotel.constantes import ESTADO_MANTENIMIENTO
        
        # --- DELEGACION (Patron Strategy) ---
        # Llama al metodo de la estrategia (sea cual sea)
        tiempo_requerido = self._estrategia_mantenimiento.calcular_mantenimiento(
            fecha=date.today(),
            ocupacion_actual_ala=ocupacion_ala,
            habitacion=habitacion
        )
        
        # Logica de negocio comun
        habitacion.set_estado(ESTADO_MANTENIMIENTO)
        print(f"INFO: Iniciando mantenimiento de {tiempo_requerido} min "
              f"para Habitación ID {habitacion.get_id()}...")
        
        return tiempo_requerido

    @abstractmethod
    def mostrar_datos(self, habitacion: 'Habitacion') -> None:
        """
        Metodo abstracto para mostrar datos.
        Sera implementado por servicios concretos y usado por el Registry.
        """
        # Logica base que todas las implementaciones llamaran con super()
        print(f"\n--- Datos Habitacion ID: {habitacion.get_id()} ---")
        print(f"Tipo:         {habitacion.get_tipo_habitacion()}")
        print(f"Capacidad:    {habitacion.get_capacidad()} personas")
        print(f"Tarifa:       ${habitacion.get_tarifa_base():.2f}")
        print(f"Estado:       {habitacion.get_estado()}")