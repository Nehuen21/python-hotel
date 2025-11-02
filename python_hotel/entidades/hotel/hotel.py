"""
Modulo de la Entidad: Hotel.

Representa el edificio principal o la propiedad hotelera, con sus
datos catastrales y capacidad total.
"""

# Usamos TYPE_CHECKING para evitar importaciones circulares en tiempo de ejecucion
# El type hint 'AlaHotel' solo es necesario para el chequeo de tipos.
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from python_hotel.entidades.hotel.ala_hotel import AlaHotel


class Hotel:
    """
    Entidad que representa el hotel como un todo.
    Contiene la informacion de identificacion y capacidad.
    """

    def __init__(self, id_hotel: int, capacidad: int, direccion: str):
        """
        Inicializa la entidad Hotel.

        Args:
            id_hotel: ID unico del hotel (ej. padron catastral).
            capacidad: Capacidad total (en personas) que el hotel puede albergar.
            direccion: Direccion fisica del hotel.
        """
        if id_hotel <= 0:
            raise ValueError("El ID del hotel debe ser un numero positivo.")
        if capacidad <= 0:
            raise ValueError("La capacidad debe ser mayor a cero.")
        if not direccion:
            raise ValueError("La direccion no puede ser nula o vacia.")

        self._id_hotel: int = id_hotel
        self._capacidad: int = capacidad
        self._direccion: str = direccion
        
        # Referencia a el/las ala(s) que contiene.
        # Para este proyecto, simplificamos a una sola ala por hotel.
        self._ala: 'AlaHotel' | None = None

    # --- Getters ---

    def get_id_hotel(self) -> int:
        """Retorna el ID unico del hotel."""
        return self._id_hotel

    def get_capacidad(self) -> int:
        """Retorna la capacidad total de personas del hotel."""
        return self._capacidad

    def get_direccion(self) -> str:
        """Retorna la direccion fisica del hotel."""
        return self._direccion

    def get_ala(self) -> 'AlaHotel':
        """Retorna la instancia del Ala asociada a este hotel."""
        if self._ala is None:
            raise ValueError("El hotel no tiene un ala asignada aun.")
        return self._ala

    # --- Setters con Validacion ---

    def set_capacidad(self, capacidad: int) -> None:
        """Actualiza la capacidad total del hotel."""
        if capacidad <= 0:
            raise ValueError("La capacidad debe ser mayor a cero.")
        self._capacidad = capacidad

    def set_direccion(self, direccion: str) -> None:
        """Actualiza la direccion fisica del hotel."""
        if not direccion:
            raise ValueError("La direccion no puede ser nula o vacia.")
        self._direccion = direccion

    def set_ala(self, ala: 'AlaHotel') -> None:
        """Asocia un Ala (piso o seccion) a este hotel."""
        self._ala = ala

    def __str__(self) -> str:
        return (
            f"Hotel ID: {self._id_hotel} (Capacidad: {self._capacidad}) - "
            f"Direccion: {self._direccion}"
        )