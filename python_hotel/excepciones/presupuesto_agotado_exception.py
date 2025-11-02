"""
Excepcion para manejar errores de presupuesto en las Alas del Hotel.
"""

from python_hotel.excepciones.hotel_exception import HotelException
from python_hotel.excepciones.mensajes_exception import PRESUPUESTO_AGOTADO

class PresupuestoAgotadoException(HotelException):
    """
    Lanzada cuando se intenta realizar una operacion (ej. limpieza)
    sin suficiente presupuesto en el Ala.
    """
    def __init__(self, presupuesto_disponible: float, coste_requerido: float):
        """
        Inicializa la excepcion.

        Args:
            presupuesto_disponible: Presupuesto actual restante en el ala.
            coste_requerido: Costo de la operacion que se intento ejecutar.
        """
        mensaje_tecnico = (
            f"Fallo de validacion de presupuesto. "
            f"Disponible: {presupuesto_disponible}, "
            f"Requerido: {coste_requerido}"
        )
        mensaje_usuario = PRESUPUESTO_AGOTADO

        super().__init__(mensaje_tecnico, mensaje_usuario)
        self._presupuesto_disponible = presupuesto_disponible
        self._coste_requerido = coste_requerido

    def get_presupuesto_disponible(self) -> float:
        return self._presupuesto_disponible

    def get_coste_requerido(self) -> float:
        return self._coste_requerido