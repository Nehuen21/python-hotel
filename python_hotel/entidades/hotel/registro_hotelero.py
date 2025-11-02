"""
Modulo de la Entidad: RegistroHotelero.

Representa el registro legal y completo de la propiedad, vinculando
el hotel, el ala, el propietario y su valuacion.
"""

from typing import TYPE_CHECKING

# Importaciones solo para type hints
if TYPE_CHECKING:
    from python_hotel.entidades.hotel.hotel import Hotel
    from python_hotel.entidades.hotel.ala_hotel import AlaHotel

class RegistroHotelero:
    """
    Entidad principal que agrupa toda la informacion del hotel.
    Esta es la clase que sera serializada (persistida) con Pickle.
    """

    def __init__(self,
                 id_hotel: int,
                 hotel: 'Hotel',
                 ala_hotel: 'AlaHotel',
                 propietario: str,
                 avaluo: float):
        """
        Inicializa el Registro Hotelero.

        Args:
            id_hotel: ID unico del hotel (coincide con Hotel.id_hotel).
            hotel: La instancia de la entidad Hotel.
            ala_hotel: La instancia de la entidad AlaHotel.
            propietario: Nombre del propietario legal.
            avaluo: Valuacion fiscal de la propiedad.
        """
        if not propietario:
            raise ValueError("El propietario no puede ser nulo o vacio.")
        if avaluo <= 0:
            raise ValueError("El avaluo debe ser un numero positivo.")

        self._id_hotel: int = id_hotel
        self._hotel: 'Hotel' = hotel
        self._ala_hotel: 'AlaHotel' = ala_hotel
        self._propietario: str = propietario
        self._avaluo: float = avaluo

    # --- Getters ---

    def get_id_hotel(self) -> int:
        return self._id_hotel

    def get_hotel(self) -> 'Hotel':
        return self._hotel

    def get_ala_hotel(self) -> 'AlaHotel':
        return self._ala_hotel

    def get_propietario(self) -> str:
        return self._propietario

    def get_avaluo(self) -> float:
        return self._avaluo