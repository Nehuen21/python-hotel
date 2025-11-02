"""
Modulo de la Clase Base para Habitaciones Estandar (no premium).
"""

from python_hotel.entidades.habitaciones.habitacion import Habitacion

class HabitacionBase(Habitacion):
    """
    Representa una habitacion estandar (Simple o Doble).
    Agrega la nocion de servicios basicos.
    """

    def __init__(self, capacidad: int, tarifa_base: float, servicios_basicos: bool = True):
        """
        Inicializa una habitacion base.

        Args:
            capacidad: Numero maximo de personas.
            tarifa_base: Precio base por noche.
            servicios_basicos: Define si incluye TV y Wi-Fi (por defecto True).
        """
        super().__init__(capacidad, tarifa_base)
        self._servicios_basicos_incluidos: bool = servicios_basicos

    def tiene_servicios_basicos(self) -> bool:
        """Retorna True si la habitacion incluye servicios basicos."""
        return self._servicios_basicos_incluidos