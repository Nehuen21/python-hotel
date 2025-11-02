"""
Modulo de la Clase Base para Habitaciones Premium (Suites).
"""

from python_hotel.entidades.habitaciones.habitacion import Habitacion

class HabitacionPremium(Habitacion):
    """
    Representa una habitacion premium (Suite o Presidencial).
    Agrega la nocion de amenities (ej. mini-bar, jacuzzi).
    """

    def __init__(self, capacidad: int, tarifa_base: float, amenities: list[str]):
        """
        Inicializa una habitacion premium.

        Args:
            capacidad: Numero maximo de personas.
            tarifa_base: Precio base por noche.
            amenities: Lista de servicios de lujo (ej. ["Jacuzzi", "Mini-bar"]).
        """
        super().__init__(capacidad, tarifa_base)
        self._amenities: list[str] = amenities

    def get_amenities(self) -> list[str]:
        """Retorna una copia de la lista de amenities."""
        return self._amenities.copy() # Retorna copia para evitar mutacion externa