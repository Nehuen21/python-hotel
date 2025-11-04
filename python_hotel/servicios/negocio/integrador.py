"""
Archivo integrador generado automaticamente
Directorio: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/servicios/negocio
Fecha: 2025-11-04 18:03:54
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/servicios/negocio/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: hoteles_service.py
# Ruta: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/servicios/negocio/hoteles_service.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 3/3: paquete.py
# Ruta: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/servicios/negocio/paquete.py
# ================================================================================

"""
Modulo de la clase generica Paquete[T].

Utilizada para empaquetar resultados de operaciones de negocio
de forma tipo-segura. (Adaptacion de US-020).
"""

from typing import Generic, TypeVar, List

# Define el tipo generico 'T'
T = TypeVar('T')

class Paquete(Generic[T]):
    """
    Clase generica (tipo-segura) para almacenar colecciones de
    resultados (ej. listas de habitaciones post-checkout).
    """
    
    # Contador estatico para IDs unicos de paquete
    _contador_id: int = 0

    @staticmethod
    def _generar_siguiente_id() -> int:
        Paquete._contador_id += 1
        return Paquete._contador_id

    def __init__(self, tipo_contenido: str, contenido: List[T]):
        """
        Args:
            tipo_contenido: Un string descriptivo (ej. "HabitacionSimple").
            contenido: La lista de objetos (ej. [hab1, hab2, ...]).
        """
        self._id_paquete: int = self._generar_siguiente_id()
        self._tipo_contenido: str = tipo_contenido
        self._items: List[T] = contenido

    def get_items(self) -> List[T]:
        """Retorna una copia de los items."""
        return self._items.copy()

    def mostrar_contenido_paquete(self) -> None:
        """Imprime un resumen del paquete en consola."""
        print("\n--- Contenido del Paquete ---")
        print(f"ID Paquete: {self._id_paquete}")
        print(f"Tipo:       {self._tipo_contenido}")
        print(f"Cantidad:   {len(self._items)} unidades")
        print("-----------------------------")

