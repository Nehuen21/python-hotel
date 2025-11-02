"""
Excepcion para manejar errores de capacidad en las Alas del Hotel.
"""

from python_hotel.excepciones.hotel_exception import HotelException
from python_hotel.excepciones.mensajes_exception import CAPACIDAD_INSUFICIENTE

class CapacidadInsuficienteException(HotelException):
    """
    Lanzada cuando se intenta configurar mas habitaciones de las permitidas
    por la capacidad del Ala.
    """
    def __init__(self, capacidad_disponible: int, capacidad_requerida: int):
        """
        Inicializa la excepcion.

        Args:
            capacidad_disponible: Capacidad actual restante en el ala.
            capacidad_requerida: Capacidad que se intento ocupar.
        """
        mensaje_tecnico = (
            f"Fallo de validacion de capacidad. "
            f"Disponible: {capacidad_disponible}, "
            f"Requerida: {capacidad_requerida}"
        )
        mensaje_usuario = CAPACIDAD_INSUFICIENTE

        super().__init__(mensaje_tecnico, mensaje_usuario)
        self._capacidad_disponible = capacidad_disponible
        self._capacidad_requerida = capacidad_requerida

    def get_capacidad_disponible(self) -> int:
        return self._capacidad_disponible

    def get_capacidad_requerida(self) -> int:
        return self._capacidad_requerida