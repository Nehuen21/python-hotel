"""
Modulo del Servicio de Negocio: HotelesService.

Implementa el patron Façade para orquestar operaciones de alto nivel
que involucran multiples hoteles o servicios. (Adaptacion de US-018).
"""

from typing import Type
from python_hotel.entidades.hotel.registro_hotelero import RegistroHotelero
from python_hotel.entidades.hotel.ala_hotel import AlaHotel
from python_hotel.entidades.habitaciones.habitacion import Habitacion
from python_hotel.servicios.hotel.ala_hotel_service import AlaHotelService
from python_hotel.servicios.negocio.paquete import Paquete


class HotelesService:
    """
    Servicio de alto nivel (Façade) para gestionar el holding de hoteles.
    
    Mantiene un registro de todos los hoteles (RegistroHotelero)
    y delega operaciones especificas a otros servicios.
    """

    def __init__(self):
        """
        Inicializa el servicio. Mantiene un 'registro' en memoria
        de todos los hoteles gestionados.
        """
        # Registro de hoteles: Mapea id_hotel -> RegistroHotelero
        self._registros_hoteleros: dict[int, RegistroHotelero] = {}
        
        # Este servicio depende de AlaHotelService para delegar tareas
        self._ala_service = AlaHotelService()
        
        print("INFO (Negocio): Servicio 'HotelesService' (Façade) inicializado.")

    def add_hotel(self, registro: RegistroHotelero) -> None:
        """Agrega un nuevo hotel al servicio de gestion."""
        id_hotel = registro.get_id_hotel()
        if id_hotel in self._registros_hoteleros:
            print(f"ADVERTENCIA: Hotel ID {id_hotel} ya estaba registrado. Sobrescribiendo.")
        self._registros_hoteleros[id_hotel] = registro
        print(f"INFO (Negocio): Hotel '{registro.get_propietario()}' (ID: {id_hotel}) "
              "agregado al servicio.")

    def buscar_ala_por_id_hotel(self, id_hotel: int) -> AlaHotel:
        """Encuentra un hotel por ID y retorna su Ala principal."""
        if id_hotel not in self._registros_hoteleros:
            raise ValueError(f"Hotel con ID {id_hotel} no encontrado en el servicio.")
        
        return self._registros_hoteleros[id_hotel].get_ala_hotel()

    def desinfectar_hotel_completo(self, id_hotel: int, quimico: str) -> None:
        """
        Operacion de negocio (Façade) que busca un hotel y delega
        su desinfeccion al servicio correspondiente. (Adaptacion US-019).
        """
        try:
            print(f"\nINFO (Negocio): Solicitud de desinfeccion para Hotel ID {id_hotel}...")
            ala_a_desinfectar = self.buscar_ala_por_id_hotel(id_hotel)
            
            # --- DELEGACION ---
            # Este servicio no sabe COMO desinfectar, solo sabe
            # a QUIEN (AlaHotelService) pedírselo.
            self._ala_service.desinfectar(ala_a_desinfectar, quimico)
            
        except ValueError as e:
            print(f"ERROR (Negocio): {e}")

    def checkout_y_empaquetar(self, tipo_habitacion: Type[Habitacion]) -> Paquete[Habitacion]:
        """
        Procesa el check-out de TODAS las habitaciones de un tipo
        en TODOS los hoteles gestionados, y las "empaqueta"
        en un Paquete generico. (Adaptacion US-020).
        """
        print(f"\nINFO (Negocio): Iniciando check-out masivo "
              f"para tipo '{tipo_habitacion.__name__}'...")
        
        habitaciones_procesadas: list[Habitacion] = []

        # Itera sobre todos los hoteles registrados
        for registro in self._registros_hoteleros.values():
            ala = registro.get_ala_hotel()
            
            # Busca y procesa habitaciones en esta ala
            for hab in ala.get_habitaciones():
                # Si es del tipo correcto y NO esta disponible
                if isinstance(hab, tipo_habitacion) and hab.get_estado() != "Disponible":
                    hab.set_estado("Disponible") # Procesa el check-out
                    habitaciones_procesadas.append(hab)

        print(f"INFO (Negocio): {len(habitaciones_procesadas)} habitaciones procesadas.")
        
        # Empaqueta el resultado usando la clase generica
        paquete_resultado = Paquete(tipo_habitacion.__name__, habitaciones_procesadas)
        return paquete_resultado