"""
Modulo del Servicio de Hotel.

Logica de negocio de alto nivel para la creacion y gestion de la
entidad Hotel.
"""

from python_hotel.entidades.hotel.hotel import Hotel
from python_hotel.entidades.hotel.ala_hotel import AlaHotel

class HotelService:
    """
    Servicio 'stateless' para operaciones relacionadas con la entidad Hotel.
    """

    def __init__(self):
        """
        Inicializa el servicio. En este caso, no tiene estado.
        """
        pass

    def crear_hotel_con_ala(self,
                             id_hotel: int,
                             capacidad: int,
                             direccion: str,
                             nombre_ala: str) -> Hotel:
        """
        Metodo de conveniencia (Fachada) para crear un Hotel y
        su Ala principal de una sola vez.

        Args:
            id_hotel: ID unico del hotel.
            capacidad: Capacidad total (en personas) del hotel.
            direccion: Direccion fisica.
            nombre_ala: Nombre del ala principal (ej. "Ala Norte").

        Returns:
            La instancia del Hotel, ya vinculada a su Ala.
        """
        
        # 1. Crear el Hotel
        try:
            hotel = Hotel(
                id_hotel=id_hotel,
                capacidad=capacidad,
                direccion=direccion
            )
            
            # 2. Crear el Ala
            # El ala hereda la capacidad maxima del hotel
            ala = AlaHotel(
                nombre=nombre_ala,
                capacidad=capacidad 
            )
            
            # 3. Vincularlos
            hotel.set_ala(ala)
            
            print(f"INFO: Hotel '{id_hotel}' y Ala '{nombre_ala}' creados exitosamente.")
            return hotel
            
        except ValueError as e:
            print(f"ERROR al crear hotel: {e}")
            raise  # Re-lanzamos la excepcion para que el main.py la maneje