"""
Archivo integrador generado automaticamente
Directorio: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/entidades/hotel
Fecha: 2025-11-04 18:03:54
Total de archivos integrados: 4
"""

# ================================================================================
# ARCHIVO 1/4: __init__.py
# Ruta: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/entidades/hotel/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/4: ala_hotel.py
# Ruta: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/entidades/hotel/ala_hotel.py
# ================================================================================

"""
Modulo de la Entidad: AlaHotel.

Representa una seccion, ala o piso del hotel, que contiene las habitaciones
y gestiona un presupuesto.
"""

from python_hotel.constantes import PRESUPUESTO_INICIAL_ALA, PRESUPUESTO_MINIMO_OPERACION
from typing import TYPE_CHECKING

# Importaciones solo para type hints para evitar importacion circular
if TYPE_CHECKING:
    from python_hotel.entidades.habitaciones.habitacion import Habitacion
    from python_hotel.entidades.personal.empleado import Empleado


class AlaHotel:
    """
    Entidad que representa un ala o piso del hotel.
    Es responsable de gestionar la lista de habitaciones, empleados
    y el presupuesto para operaciones (ej. limpieza).
    """

    def __init__(self, nombre: str, capacidad: int, presupuesto: float = PRESUPUESTO_INICIAL_ALA):
        """
        Inicializa un Ala del Hotel.

        Args:
            nombre: Nombre identificatorio (ej. "Ala Norte", "Piso 5").
            capacidad: Capacidad maxima (en personas) de esta ala.
            presupuesto: Presupuesto inicial para operaciones.
        """
        if not nombre:
            raise ValueError("El nombre del ala no puede ser nulo o vacio.")
        if capacidad <= 0:
            raise ValueError("La capacidad debe ser mayor a cero.")

        self._nombre: str = nombre
        self._capacidad_maxima: int = capacidad
        self._presupuesto_disponible: float = presupuesto
        
        # Listas de entidades contenidas
        self._habitaciones: list['Habitacion'] = []
        self._empleados: list['Empleado'] = []

    # --- Getters ---

    def get_nombre(self) -> str:
        """Retorna el nombre del ala."""
        return self._nombre

    def get_capacidad_maxima(self) -> int:
        """Retorna la capacidad maxima total (en personas) del ala."""
        return self._capacidad_maxima

    def get_presupuesto_disponible(self) -> float:
        """Retorna el presupuesto actual del ala."""
        return self._presupuesto_disponible

    def get_habitaciones(self) -> list['Habitacion']:
        """Retorna una COPIA de la lista de habitaciones."""
        return self._habitaciones.copy()

    def get_empleados(self) -> list['Empleado']:
        """Retorna una COPIA de la lista de empleados."""
        return self._empleados.copy()

    def get_capacidad_ocupada(self) -> int:
        """
        Calcula y retorna la capacidad total (en personas)
        de las habitaciones ya configuradas.
        """
        return sum(h.get_capacidad() for h in self._habitaciones)

    def get_capacidad_disponible(self) -> int:
        """
        Calcula y retorna la capacidad (en personas) aun disponible
        para configurar nuevas habitaciones.
        """
        return self._capacidad_maxima - self.get_capacidad_ocupada()

    # --- Setters y Modificadores ---

    def set_presupuesto_disponible(self, monto: float) -> None:
        """Actualiza el presupuesto, validando que no sea negativo."""
        if monto < PRESUPUESTO_MINIMO_OPERACION:
            # Permitimos 0, pero no negativo
            raise ValueError("El presupuesto no puede ser negativo.")
        self._presupuesto_disponible = monto

    def add_habitacion(self, habitacion: 'Habitacion') -> None:
        """Agrega una habitacion a la lista del ala."""
        # La logica de negocio (validacion de capacidad)
        # ira en el AlaHotelService.
        self._habitaciones.append(habitacion)

    def set_empleados(self, empleados: list['Empleado']) -> None:
        """Reemplaza la lista de empleados asignados a esta ala."""
        # Se asigna una copia para evitar que modificaciones externas
        # afecten la lista interna.
        self._empleados = empleados.copy()

    def __str__(self) -> str:
        return (
            f"Ala: {self._nombre} (Capacidad: {self.get_capacidad_ocupada()}/{self._capacidad_maxima}) - "
            f"Presupuesto: ${self._presupuesto_disponible:.2f} - "
            f"{len(self._habitaciones)} habitaciones."
        )

# ================================================================================
# ARCHIVO 3/4: hotel.py
# Ruta: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/entidades/hotel/hotel.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 4/4: registro_hotelero.py
# Ruta: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/entidades/hotel/registro_hotelero.py
# ================================================================================

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

