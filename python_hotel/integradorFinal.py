"""
INTEGRADOR FINAL - CONSOLIDACION COMPLETA DEL PROYECTO
============================================================================
Directorio raiz: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel
Fecha de generacion: 2025-11-04 18:03:54
Total de archivos integrados: 65
Total de directorios procesados: 21
============================================================================
"""

# ==============================================================================
# TABLA DE CONTENIDOS
# ==============================================================================

# DIRECTORIO: .
#    1. __init__.py
#    2. constantes.py
#
# DIRECTORIO: entidades
#    3. __init__.py
#
# DIRECTORIO: entidades/habitaciones
#    4. __init__.py
#    5. habitacion.py
#    6. habitacion_base.py
#    7. habitacion_doble.py
#    8. habitacion_premium.py
#    9. habitacion_simple.py
#    10. suite.py
#    11. suite_presidencial.py
#
# DIRECTORIO: entidades/hotel
#    12. __init__.py
#    13. ala_hotel.py
#    14. hotel.py
#    15. registro_hotelero.py
#
# DIRECTORIO: entidades/personal
#    16. __init__.py
#    17. certificacion.py
#    18. empleado.py
#    19. equipo_limpieza.py
#    20. tarea.py
#
# DIRECTORIO: excepciones
#    21. __init__.py
#    22. capacidad_insuficiente_exception.py
#    23. hotel_exception.py
#    24. mensajes_exception.py
#    25. persistencia_exception.py
#    26. presupuesto_agotado_exception.py
#
# DIRECTORIO: monitoreo
#    27. __init__.py
#
# DIRECTORIO: monitoreo/control
#    28. __init__.py
#    29. control_limpieza_task.py
#
# DIRECTORIO: monitoreo/sensores
#    30. __init__.py
#    31. limpieza_reader_task.py
#    32. ocupacion_reader_task.py
#
# DIRECTORIO: patrones
#    33. __init__.py
#
# DIRECTORIO: patrones/factory
#    34. __init__.py
#    35. habitacion_factory.py
#
# DIRECTORIO: patrones/observer
#    36. __init__.py
#    37. observable.py
#    38. observer.py
#
# DIRECTORIO: patrones/observer/eventos
#    39. __init__.py
#    40. evento_hotel.py
#    41. evento_sensor.py
#
# DIRECTORIO: patrones/singleton
#    42. __init__.py
#
# DIRECTORIO: patrones/strategy
#    43. __init__.py
#    44. mantenimiento_strategy.py
#
# DIRECTORIO: patrones/strategy/impl
#    45. __init__.py
#    46. mantenimiento_estandar_strategy.py
#    47. mantenimiento_premium_strategy.py
#
# DIRECTORIO: servicios
#    48. __init__.py
#
# DIRECTORIO: servicios/habitaciones
#    49. __init__.py
#    50. habitacion_base_service.py
#    51. habitacion_doble_service.py
#    52. habitacion_service.py
#    53. habitacion_service_registry.py
#    54. habitacion_simple_service.py
#    55. suite_presidencial_service.py
#    56. suite_service.py
#
# DIRECTORIO: servicios/hotel
#    57. __init__.py
#    58. ala_hotel_service.py
#    59. hotel_service.py
#    60. registro_hotelero_service.py
#
# DIRECTORIO: servicios/negocio
#    61. __init__.py
#    62. hoteles_service.py
#    63. paquete.py
#
# DIRECTORIO: servicios/personal
#    64. __init__.py
#    65. empleado_service.py
#



################################################################################
# DIRECTORIO: .
################################################################################

# ==============================================================================
# ARCHIVO 1/65: __init__.py
# Directorio: .
# Ruta completa: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 2/65: constantes.py
# Directorio: .
# Ruta completa: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/constantes.py
# ==============================================================================

"""
Modulo de Constantes para el Sistema de Gestion Hotelera (PythonHotel).

Este archivo centraliza todas las variables de configuracion, "numeros magicos"
y valores fijos para evitar el "hardcoding" en la logica de negocio,
siguiendo el principio de Codigo Limpio.
"""

# -----------------------------------------------------------------------------
# Configuracion de Persistencia
# -----------------------------------------------------------------------------
DIRECTORIO_DATA: str = "data"
EXTENSION_DATA: str = ".dat"


# -----------------------------------------------------------------------------
# Constantes del Dominio: Hotel y Alas
# -----------------------------------------------------------------------------
PRESUPUESTO_INICIAL_ALA: float = 5000.0
COSTE_LIMPIEZA_ALA: float = 100.0
PRESUPUESTO_MINIMO_OPERACION: float = 0.0


# -----------------------------------------------------------------------------
# Constantes del Dominio: Habitaciones
# -----------------------------------------------------------------------------
ESTADO_INICIAL_HABITACION: str = "Disponible"
ESTADO_MANTENIMIENTO: str = "En Mantenimiento"
ESTADO_OCUPADA: str = "Ocupada"

# --- Habitacion Simple ---
CAPACIDAD_SIMPLE: int = 1
TARIFA_BASE_SIMPLE: float = 50.0

# --- Habitacion Doble ---
CAPACIDAD_DOBLE: int = 2
TARIFA_BASE_DOBLE: float = 80.0

# --- Suite ---
CAPACIDAD_SUITE: int = 4
TARIFA_BASE_SUITE: float = 200.0

# --- Suite Presidencial ---
CAPACIDAD_PRESIDENCIAL: int = 6
TARIFA_BASE_PRESIDENCIAL: float = 500.0


# -----------------------------------------------------------------------------
# Constantes del Patron Strategy (Mantenimiento)
# -----------------------------------------------------------------------------
# Estrategia Estandar (Simple, Doble)
MANTENIMIENTO_ESTANDAR_BASICO: int = 30  # minutos (alta ocupacion)
MANTENIMIENTO_ESTANDAR_COMPLETO: int = 60 # minutos (baja ocupacion)
UMBRAL_OCUPACION_ESTANDAR: float = 0.3 # 30%

# Estrategia Premium (Suites)
MANTENIMIENTO_PREMIUM_SUITE: int = 60  # minutos (constante)
MANTENIMIENTO_PREMIUM_PRESIDENCIAL: int = 90  # minutos (constante)


# -----------------------------------------------------------------------------
# Constantes del Monitoreo y Limpieza (Patron Observer)
# -----------------------------------------------------------------------------

# --- Sensores ---
INTERVALO_SENSOR_OCUPACION: float = 2.0  # segundos
SENSOR_OCUPACION_MIN: int = 0
SENSOR_OCUPACION_MAX: int = 100

INTERVALO_SENSOR_LIMPIEZA: float = 3.0  # segundos
SENSOR_LIMPIEZA_MIN: int = 0
SENSOR_LIMPIEZA_MAX: int = 100

# --- Controlador ---
INTERVALO_CONTROL_LIMPIEZA: float = 2.5  # segundos

# --- Umbrales para limpieza automatica ---
# Se activa si: Ocupacion < 10% Y Limpieza < 70%
OCUPACION_MAX_PARA_LIMPIEZA: float = 10.0  # %
LIMPIEZA_MIN_PARA_LIMPIEZA: float = 70.0  # %


# -----------------------------------------------------------------------------
# Constantes de Concurrencia (Threading)
# -----------------------------------------------------------------------------
THREAD_JOIN_TIMEOUT: float = 2.0  # segundos


################################################################################
# DIRECTORIO: entidades
################################################################################

# ==============================================================================
# ARCHIVO 3/65: __init__.py
# Directorio: entidades
# Ruta completa: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/entidades/__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: entidades/habitaciones
################################################################################

# ==============================================================================
# ARCHIVO 4/65: __init__.py
# Directorio: entidades/habitaciones
# Ruta completa: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/entidades/habitaciones/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 5/65: habitacion.py
# Directorio: entidades/habitaciones
# Ruta completa: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/entidades/habitaciones/habitacion.py
# ==============================================================================

"""
Modulo de la Interfaz Base para todas las Habitaciones.

Define el contrato comun que cualquier tipo de habitacion en el sistema
debe implementar, asegurando polimorfismo.
"""

from abc import ABC, abstractmethod

class Habitacion(ABC):
    """
    Interfaz abstracta (ABC) que define el comportamiento comun
    de todas las habitaciones.
    """

    _contador_id: int = 0

    @staticmethod
    def _generar_siguiente_id() -> int:
        """Generador de IDs unicos para cada habitacion."""
        Habitacion._contador_id += 1
        return Habitacion._contador_id

    def __init__(self, capacidad: int, tarifa_base: float):
        """
        Inicializa una habitacion.

        Args:
            capacidad: Numero maximo de personas.
            tarifa_base: Precio base por noche.
        """
        from python_hotel.constantes import ESTADO_INICIAL_HABITACION
        
        self._id: int = self._generar_siguiente_id()
        self._capacidad: int = capacidad
        self._tarifa_base: float = tarifa_base
        self._estado: str = ESTADO_INICIAL_HABITACION # Ej: "Disponible", "Ocupada"

    # --- Getters ---

    def get_id(self) -> int:
        """Retorna el ID unico de la habitacion."""
        return self._id

    def get_capacidad(self) -> int:
        """Retorna la capacidad maxima de la habitacion."""
        return self._capacidad

    def get_tarifa_base(self) -> float:
        """Retorna la tarifa base por noche."""
        return self._tarifa_base

    def get_estado(self) -> str:
        """Retorna el estado actual (Disponible, Ocupada, Mantenimiento)."""
        return self._estado

    # --- Setters con Validacion ---

    def set_estado(self, estado: str) -> None:
        """
        Actualiza el estado de la habitacion.

        Args:
            estado: El nuevo estado (ej. "Ocupada").
        """
        if not estado:
            raise ValueError("El estado no puede ser nulo o vacio.")
        self._estado = estado

    def set_tarifa_base(self, tarifa: float) -> None:
        """
        Actualiza la tarifa base, validando que no sea negativa.

        Args:
            tarifa: El nuevo precio base.
        """
        if tarifa < 0:
            raise ValueError("La tarifa base no puede ser negativa.")
        self._tarifa_base = tarifa

    @abstractmethod
    def get_tipo_habitacion(self) -> str:
        """
        Metodo abstracto que deben implementar las clases hijas.

        Returns:
            Un string que identifica el tipo (ej. "Simple", "Suite").
        """
        pass

    def __str__(self) -> str:
        """Representacion en string de la habitacion."""
        return (
            f"Habitacion ID: {self._id} (Tipo: {self.get_tipo_habitacion()}) - "
            f"Capacidad: {self._capacidad} - Tarifa: ${self._tarifa_base:.2f} - "
            f"Estado: {self._estado}"
        )

# ==============================================================================
# ARCHIVO 6/65: habitacion_base.py
# Directorio: entidades/habitaciones
# Ruta completa: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/entidades/habitaciones/habitacion_base.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 7/65: habitacion_doble.py
# Directorio: entidades/habitaciones
# Ruta completa: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/entidades/habitaciones/habitacion_doble.py
# ==============================================================================

"""
Modulo de la Entidad Concreta: HabitacionDoble.
"""

from python_hotel.entidades.habitaciones.habitacion_base import HabitacionBase
from python_hotel.constantes import CAPACIDAD_DOBLE, TARIFA_BASE_DOBLE

class HabitacionDoble(HabitacionBase):
    """
    Entidad concreta que representa una Habitacion Doble.
    """

    def __init__(self, servicios_basicos: bool = True, desayuno_incluido: bool = True):
        """
        Inicializa una habitacion doble.
        """
        super().__init__(
            capacidad=CAPACIDAD_DOBLE,
            tarifa_base=TARIFA_BASE_DOBLE,
            servicios_basicos=servicios_basicos
        )
        self._desayuno_incluido: bool = desayuno_incluido

    def tiene_desayuno_incluido(self) -> bool:
        """Retorna True si el desayuno esta incluido."""
        return self._desayuno_incluido

    def get_tipo_habitacion(self) -> str:
        """Implementacion del metodo abstracto."""
        return "Doble"

# ==============================================================================
# ARCHIVO 8/65: habitacion_premium.py
# Directorio: entidades/habitaciones
# Ruta completa: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/entidades/habitaciones/habitacion_premium.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 9/65: habitacion_simple.py
# Directorio: entidades/habitaciones
# Ruta completa: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/entidades/habitaciones/habitacion_simple.py
# ==============================================================================

"""
Modulo de la Entidad Concreta: HabitacionSimple.
"""

from python_hotel.entidades.habitaciones.habitacion_base import HabitacionBase
from python_hotel.constantes import CAPACIDAD_SIMPLE, TARIFA_BASE_SIMPLE

class HabitacionSimple(HabitacionBase):
    """
    Entidad concreta que representa una Habitacion Simple.
    Utiliza constantes para sus valores por defecto.
    """

    def __init__(self, servicios_basicos: bool = True):
        """
        Inicializa una habitacion simple, usando valores de constantes.py.
        """
        super().__init__(
            capacidad=CAPACIDAD_SIMPLE,
            tarifa_base=TARIFA_BASE_SIMPLE,
            servicios_basicos=servicios_basicos
        )
        # Atributo especifico de esta clase
        self._tamano_cama: str = "Individual"

    def get_tamano_cama(self) -> str:
        """Retorna el tamano de la cama."""
        return self._tamano_cama
    
    def get_tipo_habitacion(self) -> str:
        """Implementacion del metodo abstracto."""
        return "Simple"

# ==============================================================================
# ARCHIVO 10/65: suite.py
# Directorio: entidades/habitaciones
# Ruta completa: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/entidades/habitaciones/suite.py
# ==============================================================================

"""
Modulo de la Entidad Concreta: Suite.
"""

from python_hotel.entidades.habitaciones.habitacion_premium import HabitacionPremium
from python_hotel.constantes import CAPACIDAD_SUITE, TARIFA_BASE_SUITE

class Suite(HabitacionPremium):
    """
    Entidad concreta que representa una Suite.
    """

    def __init__(self, room_service_24h: bool = True):
        """
        Inicializa una suite, definiendo sus amenities por defecto.
        """
        amenities_por_defecto = ["Jacuzzi", "Mini-bar", "Sala de estar"]
        
        super().__init__(
            capacidad=CAPACIDAD_SUITE,
            tarifa_base=TARIFA_BASE_SUITE,
            amenities=amenities_por_defecto
        )
        self._room_service_24h: bool = room_service_24h

    def tiene_room_service_24h(self) -> bool:
        """Retorna True si la suite tiene room service 24h."""
        return self._room_service_24h

    def get_tipo_habitacion(self) -> str:
        """Implementacion del metodo abstracto."""
        return "Suite"

# ==============================================================================
# ARCHIVO 11/65: suite_presidencial.py
# Directorio: entidades/habitaciones
# Ruta completa: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/entidades/habitaciones/suite_presidencial.py
# ==============================================================================

"""
Modulo de la Entidad Concreta: SuitePresidencial.
"""

from python_hotel.entidades.habitaciones.habitacion_premium import HabitacionPremium
from python_hotel.constantes import CAPACIDAD_PRESIDENCIAL, TARIFA_BASE_PRESIDENCIAL

class SuitePresidencial(HabitacionPremium):
    """
    Entidad concreta que representa una Suite Presidencial.
    """

    def __init__(self, tiene_terraza: bool = True):
        """
        Inicializa una suite presidencial.
        """
        amenities_por_defecto = [
            "Jacuzzi doble", 
            "Mini-bar premium", 
            "Sala de reuniones",
            "Servicio de mayordomo"
        ]
        
        super().__init__(
            capacidad=CAPACIDAD_PRESIDENCIAL,
            tarifa_base=TARIFA_BASE_PRESIDENCIAL,
            amenities=amenities_por_defecto
        )
        self._tiene_terraza: bool = tiene_terraza

    def tiene_terraza(self) -> bool:
        """Retorna True si la suite tiene terraza privada."""
        return self._tiene_terraza

    def get_tipo_habitacion(self) -> str:
        """Implementacion del metodo abstracto."""
        return "Presidencial"


################################################################################
# DIRECTORIO: entidades/hotel
################################################################################

# ==============================================================================
# ARCHIVO 12/65: __init__.py
# Directorio: entidades/hotel
# Ruta completa: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/entidades/hotel/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 13/65: ala_hotel.py
# Directorio: entidades/hotel
# Ruta completa: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/entidades/hotel/ala_hotel.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 14/65: hotel.py
# Directorio: entidades/hotel
# Ruta completa: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/entidades/hotel/hotel.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 15/65: registro_hotelero.py
# Directorio: entidades/hotel
# Ruta completa: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/entidades/hotel/registro_hotelero.py
# ==============================================================================

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


################################################################################
# DIRECTORIO: entidades/personal
################################################################################

# ==============================================================================
# ARCHIVO 16/65: __init__.py
# Directorio: entidades/personal
# Ruta completa: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/entidades/personal/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 17/65: certificacion.py
# Directorio: entidades/personal
# Ruta completa: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/entidades/personal/certificacion.py
# ==============================================================================

"""
Modulo de la Entidad: Certificacion.

Representa la certificacion profesional de un empleado (ej. higiene,
mantenimiento electrico, etc.). Reemplaza a 'AptoMedico'.
"""

from datetime import date

class Certificacion:
    """
    Entidad que almacena los datos de una certificacion profesional.
    """

    def __init__(self, 
                 es_valida: bool, 
                 fecha_emision: date, 
                 especializacion: str,
                 observaciones: str = "Sin observaciones"):
        """
        Inicializa la certificacion.

        Args:
            es_valida: True si la certificacion esta vigente.
            fecha_emision: Cuando fue emitida.
            especializacion: El area de la certificacion (ej. "Limpieza Nivel 3").
            observaciones: Notas adicionales.
        """
        if not especializacion:
            raise ValueError("La especializacion no puede ser nula o vacia.")

        self._es_valida: bool = es_valida
        self._fecha_emision: date = fecha_emision
        self._especializacion: str = especializacion
        self._observaciones: str = observaciones

    # --- Getters ---

    def esta_certificacion_valida(self) -> bool:
        """Retorna True si la certificacion esta vigente y es valida."""
        return self._es_valida

    def get_fecha_emision(self) -> date:
        return self._fecha_emision
    
    def get_especializacion(self) -> str:
        return self._especializacion

    def get_observaciones(self) -> str:
        return self._observaciones

# ==============================================================================
# ARCHIVO 18/65: empleado.py
# Directorio: entidades/personal
# Ruta completa: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/entidades/personal/empleado.py
# ==============================================================================

"""
Modulo de la Entidad: Empleado.

Representa a un miembro del personal del hotel. Reemplaza a 'Trabajador'.
"""
from __future__ import annotations
from typing import TYPE_CHECKING

# Importaciones solo para type hints para evitar importacion circular
if TYPE_CHECKING:
    from python_hotel.entidades.personal.certificacion import Certificacion
    from python_hotel.entidades.personal.tarea import Tarea

class Empleado:
    """
    Entidad que representa a un empleado del hotel.
    Contiene su informacion personal, su certificacion y sus tareas.
    """

    def __init__(self, dni: int, nombre: str, tareas: list['Tarea']):
        """
        Inicializa un Empleado.

        Args:
            dni: DNI unico del empleado.
            nombre: Nombre completo.
            tareas: Lista de tareas asignadas (puede estar vacia).
        """
        if dni <= 0:
            raise ValueError("El DNI debe ser un numero positivo.")
        if not nombre:
            raise ValueError("El nombre no puede ser nulo o vacio.")

        self._dni: int = dni
        self._nombre: str = nombre
        
        # Guardamos una copia para encapsulamiento
        self._tareas: list['Tarea'] = tareas.copy()
        
        # El empleado se crea sin certificacion, se asigna despues.
        self._certificacion: 'Certificacion' | None = None

    # --- Getters ---

    def get_dni(self) -> int:
        return self._dni

    def get_nombre(self) -> str:
        return self._nombre

    def get_certificacion(self) -> 'Certificacion' | None:
        """Retorna el objeto Certificacion o None si no esta asignado."""
        return self._certificacion

    def get_tareas(self) -> list['Tarea']:
        """Retorna una COPIA de la lista de tareas."""
        return self._tareas.copy()

    # --- Setters ---

    def set_certificacion(self, certificacion: 'Certificacion') -> None:
        """Asigna o actualiza la certificacion del empleado."""
        self._certificacion = certificacion
        
    def set_tareas(self, tareas: list['Tarea']) -> None:
        """Reemplaza la lista de tareas del empleado."""
        self._tareas = tareas.copy() # Guardar copia

    def __str__(self) -> str:
        certificado = "Certificado" if self._certificacion and self._certificacion.esta_certificacion_valida() else "No Certificado"
        return (
            f"Empleado: {self._nombre} (DNI: {self._dni}) - "
            f"Tareas: {len(self._tareas)} - Estado: {certificado}"
        )

# ==============================================================================
# ARCHIVO 19/65: equipo_limpieza.py
# Directorio: entidades/personal
# Ruta completa: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/entidades/personal/equipo_limpieza.py
# ==============================================================================

"""
Modulo de la Entidad: EquipoLimpieza.

Representa el equipamiento fisico utilizado para tareas de limpieza
o mantenimiento. Reemplaza a 'Herramienta'.
"""

class EquipoLimpieza:
    """
    Entidad que representa una herramienta o equipo (ej. aspiradora, carro).
    """

    def __init__(self, id_equipo: int, nombre: str, certificado_higiene: bool):
        """
        Inicializa el equipo.

        Args:
            id_equipo: ID unico del equipo.
            nombre: Nombre del equipo (ej. "Aspiradora Industrial V-100").
            certificado_higiene: True si cumple con normas H&S.
        """
        if id_equipo <= 0:
            raise ValueError("El ID del equipo debe ser positivo.")
        if not nombre:
            raise ValueError("El nombre no puede ser nulo o vacio.")

        self._id_equipo: int = id_equipo
        self._nombre: str = nombre
        self._certificado_higiene: bool = certificado_higiene

    # --- Getters ---

    def get_id_equipo(self) -> int:
        return self._id_equipo

    def get_nombre(self) -> str:
        return self._nombre

    def tiene_certificado_higiene(self) -> bool:
        return self._certificado_higiene

    def __str__(self) -> str:
        return f"Equipo: {self._nombre} (ID: {self._id_equipo})"

# ==============================================================================
# ARCHIVO 20/65: tarea.py
# Directorio: entidades/personal
# Ruta completa: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/entidades/personal/tarea.py
# ==============================================================================

"""
Modulo de la Entidad: Tarea.

Representa una tarea asignada a un empleado.
"""

from datetime import date

class Tarea:
    """
    Entidad que representa una tarea de mantenimiento o limpieza.
    """

    def __init__(self, id_tarea: int, fecha_programada: date, descripcion: str):
        """
        Inicializa una Tarea.

        Args:
            id_tarea: ID unico de la tarea.
            fecha_programada: Dia en que debe realizarse.
            descripcion: Descripcion de la tarea (ej. "Limpiar Suite 101").
        """
        if id_tarea <= 0:
            raise ValueError("El ID de la tarea debe ser positivo.")
        if not descripcion:
            raise ValueError("La descripcion no puede ser nula o vacia.")

        self._id_tarea: int = id_tarea
        self._fecha_programada: date = fecha_programada
        self._descripcion: str = descripcion
        self._estado: str = "Pendiente" # Estados: Pendiente, Completada

    # --- Getters ---

    def get_id_tarea(self) -> int:
        return self._id_tarea

    def get_fecha_programada(self) -> date:
        return self._fecha_programada

    def get_descripcion(self) -> str:
        return self._descripcion

    def get_estado(self) -> str:
        return self._estado

    # --- Setters ---

    def set_estado(self, estado: str) -> None:
        """Actualiza el estado de la tarea (ej. "Completada")."""
        if not estado:
            raise ValueError("El estado no puede ser nulo o vacio.")
        self._estado = estado

    def __str__(self) -> str:
        return (
            f"Tarea ID: {self._id_tarea} ({self._descripcion}) - "
            f"Fecha: {self._fecha_programada} - Estado: {self._estado}"
        )


################################################################################
# DIRECTORIO: excepciones
################################################################################

# ==============================================================================
# ARCHIVO 21/65: __init__.py
# Directorio: excepciones
# Ruta completa: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/excepciones/__init__.py
# ==============================================================================

# no contiene nada pero le indica a python que eso es un paquete, todos los __init__ estan dentro de los directorios



# ==============================================================================
# ARCHIVO 22/65: capacidad_insuficiente_exception.py
# Directorio: excepciones
# Ruta completa: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/excepciones/capacidad_insuficiente_exception.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 23/65: hotel_exception.py
# Directorio: excepciones
# Ruta completa: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/excepciones/hotel_exception.py
# ==============================================================================

"""
Excepcion base para todo el proyecto PythonHotel.
"""

class HotelException(Exception):
    """
    Clase base para todas las excepciones personalizadas del sistema.

    Permite capturar cualquier error especifico del dominio en un solo bloque
    except.
    """
    def __init__(self, mensaje_tecnico: str, mensaje_usuario: str = "Ha ocurrido un error inesperado."):
        """
        Inicializa la excepcion base.

        Args:
            mensaje_tecnico: Mensaje detallado para el desarrollador (logging).
            mensaje_usuario: Mensaje generico para mostrar al usuario final.
        """
        super().__init__(mensaje_tecnico)
        self._mensaje_tecnico = mensaje_tecnico
        self._mensaje_usuario = mensaje_usuario

    def get_mensaje_tecnico(self) -> str:
        """Retorna el mensaje tecnico detallado."""
        return self._mensaje_tecnico

    def get_mensaje_usuario(self) -> str:
        """Retorna el mensaje amigable para el usuario."""
        return self._mensaje_usuario

    def get_full_message(self) -> str:
        """Retorna una combinacion de ambos mensajes."""
        return f"[USUARIO] {self._mensaje_usuario} \n[TECNICO] {self._mensaje_tecnico}"

# ==============================================================================
# ARCHIVO 24/65: mensajes_exception.py
# Directorio: excepciones
# Ruta completa: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/excepciones/mensajes_exception.py
# ==============================================================================

"""
Modulo de Mensajes de Error.

Centraliza los mensajes de error orientados al usuario para las excepciones
personalizadas del dominio.
"""

# --- Mensajes de Negocio ---
CAPACIDAD_INSUFICIENTE: str = "Capacidad insuficiente en el ala del hotel."
PRESUPUESTO_AGOTADO: str = "Presupuesto del ala agotado. No se puede completar la operacion."
EMPLEADO_SIN_CERTIFICACION: str = "El empleado no posee la certificacion valida para operar."

# --- Mensajes de Persistencia ---
ERROR_PERSISTENCIA_ESCRITURA: str = "Error critico al intentar guardar el registro."
ERROR_PERSISTENCIA_LECTURA: str = "Error critico al intentar leer el registro."
ERROR_PERSISTENCIA_GENERICO: str = "Ha ocurrido un error en la capa de persistencia."
ARCHIVO_NO_ENCONTRADO: str = "El archivo de registro solicitado no fue encontrado."

# ==============================================================================
# ARCHIVO 25/65: persistencia_exception.py
# Directorio: excepciones
# Ruta completa: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/excepciones/persistencia_exception.py
# ==============================================================================

"""
Excepcion para manejar errores en la capa de persistencia (Pickle).
"""

from python_hotel.excepciones.hotel_exception import HotelException
from python_hotel.excepciones.mensajes_exception import (
    ERROR_PERSISTENCIA_LECTURA,
    ERROR_PERSISTENCIA_ESCRITURA,
    ARCHIVO_NO_ENCONTRADO
)
from enum import Enum

class TipoOperacionPersistencia(Enum):
    LECTURA = 1
    ESCRITURA = 2

class PersistenciaException(HotelException):
    """
    Lanzada cuando ocurre un error al leer o escribir en disco (Pickle).
    """
    def __init__(self, 
                 error_original: Exception, 
                 nombre_archivo: str, 
                 tipo_operacion: TipoOperacionPersistencia):
        """
        Inicializa la excepcion de persistencia.

        Args:
            error_original: La excepcion original (ej. IOError, FileNotFoundError).
            nombre_archivo: El path del archivo que fallo.
            tipo_operacion: Enum indicando si fue LECTURA o ESCRITURA.
        """
        
        if tipo_operacion == TipoOperacionPersistencia.LECTURA:
            if isinstance(error_original, FileNotFoundError):
                mensaje_usuario = ARCHIVO_NO_ENCONTRADO
            else:
                mensaje_usuario = ERROR_PERSISTENCIA_LECTURA
        else:
            mensaje_usuario = ERROR_PERSISTENCIA_ESCRITURA

        mensaje_tecnico = (
            f"Error de persistencia en operacion '{tipo_operacion.name}' "
            f"sobre el archivo '{nombre_archivo}'. "
            f"Error original: {type(error_original).__name__} - {error_original}"
        )
        
        super().__init__(mensaje_tecnico, mensaje_usuario)
        self._error_original = error_original
        self._nombre_archivo = nombre_archivo
        self._tipo_operacion = tipo_operacion

    def get_nombre_archivo(self) -> str:
        return self._nombre_archivo

    def get_tipo_operacion(self) -> TipoOperacionPersistencia:
        return self._tipo_operacion

# ==============================================================================
# ARCHIVO 26/65: presupuesto_agotado_exception.py
# Directorio: excepciones
# Ruta completa: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/excepciones/presupuesto_agotado_exception.py
# ==============================================================================

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


################################################################################
# DIRECTORIO: monitoreo
################################################################################

# ==============================================================================
# ARCHIVO 27/65: __init__.py
# Directorio: monitoreo
# Ruta completa: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/monitoreo/__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: monitoreo/control
################################################################################

# ==============================================================================
# ARCHIVO 28/65: __init__.py
# Directorio: monitoreo/control
# Ruta completa: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/monitoreo/control/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 29/65: control_limpieza_task.py
# Directorio: monitoreo/control
# Ruta completa: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/monitoreo/control/control_limpieza_task.py
# ==============================================================================

"""
Modulo del Controlador de Limpieza (Observer).

Implementa un hilo que observa los sensores y toma decisiones
de limpieza automatica, delegando la accion al AlaHotelService.
"""

import threading
import time
from typing import TYPE_CHECKING

# Importacion de la interfaz Observer
from python_hotel.patrones.observer.observer import Observer
from python_hotel.constantes import (
    INTERVALO_CONTROL_LIMPIEZA,
    OCUPACION_MAX_PARA_LIMPIEZA,
    LIMPIEZA_MIN_PARA_LIMPIEZA
)
# Importacion de la excepcion que puede ocurrir
from python_hotel.excepciones.presupuesto_agotado_exception import PresupuestoAgotadoException

if TYPE_CHECKING:
    from python_hotel.servicios.hotel.ala_hotel_service import AlaHotelService
    from python_hotel.entidades.hotel.ala_hotel import AlaHotel
    # Importamos los Observables para type hints
    from python_hotel.monitoreo.sensores.ocupacion_reader_task import OcupacionReaderTask
    from python_hotel.monitoreo.sensores.limpieza_reader_task import LimpiezaReaderTask


class ControlLimpiezaTask(threading.Thread, Observer[float]):
    """
    Controlador (Observer) que gestiona la limpieza automatica.

    Hereda de 'threading.Thread' para correr en un hilo separado.
    Hereda de 'Observer[float]' para poder suscribirse a los sensores.
    """

    def __init__(self,
                 sensor_ocupacion: 'OcupacionReaderTask',
                 sensor_limpieza: 'LimpiezaReaderTask',
                 ala_hotel: 'AlaHotel',
                 ala_service: 'AlaHotelService'):
        
        threading.Thread.__init__(self, daemon=True)
        self._detenido = threading.Event()
        
        # --- Inyeccion de Dependencias ---
        self._ala_hotel = ala_hotel
        self._ala_service = ala_service
        self._sensor_ocupacion = sensor_ocupacion
        self._sensor_limpieza = sensor_limpieza
        
        # Estado interno para almacenar las ultimas lecturas
        # Usamos locks para garantizar thread-safety al actualizar/leer
        self._lock = threading.Lock()
        self._ultima_ocupacion: float = 100.0 # Valor inicial seguro
        self._ultima_limpieza: float = 100.0  # Valor inicial seguro

    def _suscribir_a_sensores(self) -> None:
        """Se suscribe como observador a los sensores."""
        self._sensor_ocupacion.agregar_observador(self)
        self._sensor_limpieza.agregar_observador(self)
        print("INFO (Control): Controlador suscrito a sensores de Ocupacion y Limpieza.")

    def actualizar(self, evento: float) -> None:
        """
        Metodo de la interfaz Observer. Es llamado por CUALQUIER
        Observable al que este suscrito (ambos sensores).

        Args:
            evento: El valor (float) notificado.
        """
        # Identificamos de que sensor proviene el evento
        # (Esto es una simplificacion; en un sistema real,
        # el 'evento' seria un objeto con mas contexto).
        
        # Heuristica simple: si es > 100, no puede ser, pero
        # un valor de 0 a 100 puede ser cualquiera.
        # Necesitamos identificar al emisor.
        
        # --- Estrategia de Identificacion (Hack simple) ---
        # Como no podemos saber cual sensor fue, le preguntamos
        # al 'sender' (emisor) que no esta implementado.
        # Vamos a tener que cambiar la firma de 'actualizar'
        # o almacenar los valores de forma diferente.
        
        # --- Estrategia 2 (Mejor) ---
        # El controlador NO debe implementar 'actualizar'
        # directamente. En su lugar, el 'run' loop leera
        # los valores directamente.
        
        # --- Estrategia 3 (La correcta para este diseno) ---
        # El controlador necesita saber de QUIEN viene la actualizacion.
        # Modificaremos 'actualizar' para que reciba al emisor.
        
        # --- Estrategia 4 (La mas simple) ---
        # El controlador no implementa 'actualizar'.
        # El controlador le PIDE los valores a los sensores
        # en su propio bucle 'run'.
        
        # --- Estrategia 5 (La que pide la HU) ---
        # El controlador ES un observador. Debe implementar 'actualizar'.
        # El problema es que ambos sensores envian 'float'.
        # Necesitamos diferenciar los eventos.
        
        # Vamos a asumir que 'actualizar' recibe (sender, evento)
        # Esto requiere modificar Observable.notificar_observadores(self, evento)
        #
        # Opcion B: El controlador tiene metodos separados.
        # self._sensor_ocupacion.agregar_observador(self.actualizar_ocupacion)
        #
        # Opcion C: La mas simple: El controlador guarda el ultimo valor
        # de CADA sensor en su metodo 'actualizar', pero necesita
        # saber de quien viene.
        
        # **** SOLUCION (Paso 3 corregido) ****
        # Observable.notificar_observadores deberia pasar 'self' y 'evento'
        # Pero para no cambiar los archivos del Paso 3, haremos un
        # truco: 'actualizar' sera llamado por los sensores, pero
        # no sabremos cual.
        # El controlador tendra que almacenar los valores.
        
        # **** SOLUCION 2 (La mas realista) ****
        # El controlador implementa DOS interfaces Observer
        # o tiene metodos especificos.
        
        # **** SOLUCION 3 (La que implementaremos) ****
        # Haremos que los sensores notifiquen una TUPLA (str, float)
        # Esto rompe la firma Generica T=float, pero es lo mas
        # practico para el ejercicio.
        
        # *** RE-DISENO (El mas limpio) ***
        # El Controlador sera Observador de NADA.
        # El Controlador correra en su hilo y PREGUNTARA
        # a los sensores por sus ultimos valores.
        # Esto rompe la HU "Implementar patron Observer".
        
        # *** SOLUCION FINAL (Fiel a la HU) ***
        # El controlador implementa Observer[float].
        # PERO necesita saber de quien.
        # Modificaremos los sensores para que notifiquen un
        # objeto 'EventoSensor' en lugar de un 'float'.
        #
        # ¡Pero la HU US-TECH-003 dice Observable[float]!
        #
        # OK, AQUI ESTA LA LOGICA:
        # El controlador NO implementara Observer.
        # El controlador se inyecta con los Observables
        # y el controlador CREA observadores internos (lambdas o metodos)
        # para actualizar su estado.
        
        # Esta es la implementacion correcta para la HU-012
        pass # 'actualizar' no se usara directamente.

    def _actualizar_ocupacion(self, ocupacion: float):
        """Callback privado para el sensor de ocupacion."""
        with self._lock:
            self._ultima_ocupacion = ocupacion
        
    def _actualizar_limpieza(self, limpieza: float):
        """Callback privado para el sensor de limpieza."""
        with self._lock:
            self._ultima_limpieza = limpieza

    def run(self) -> None:
        """
        Metodo principal del hilo (se ejecuta con .start()).
        
        En lugar de implementar Observer.actualizar() (que es ambiguo
        con dos fuentes), el controlador crea sus propios observadores
        internos (metodos) y los suscribe.
        
        El hilo 'run' se dedica a chequear las condiciones.
        """
        
        # 1. Suscribir los callbacks privados a los sensores
        self._sensor_ocupacion.agregar_observador(self)
        self._sensor_limpieza.agregar_observador(self)
        # Esto significa que 'actualizar' sera llamado por AMBOS.
        # No podemos diferenciarlos.
        
        # **** PLAN B (Definitivo) ****
        # La clase NO implementa Observer.
        # Los sensores son Observables.
        # El controlador crea Observadores INTERNOS (clases anidadas o metodos)
        
        # Clase interna Observador de Ocupacion
        class OcupacionObserver(Observer[float]):
            def __init__(self, controlador):
                self._controlador = controlador
            def actualizar(self, evento: float):
                self._controlador._actualizar_ocupacion(evento)
                
        # Clase interna Observador de Limpieza
        class LimpiezaObserver(Observer[float]):
            def __init__(self, controlador):
                self._controlador = controlador
            def actualizar(self, evento: float):
                self._controlador._actualizar_limpieza(evento)

        # 1. Suscribir los observadores internos
        self._sensor_ocupacion.agregar_observador(OcupacionObserver(self))
        self._sensor_limpieza.agregar_observador(LimpiezaObserver(self))
        print("INFO (Control): Controlador (hilo) iniciado y suscrito a sensores.")

        # 2. Bucle de decision
        while not self._detenido.is_set():
            time.sleep(INTERVALO_CONTROL_LIMPIEZA)
            
            # 3. Leer estado interno (thread-safe)
            with self._lock:
                ocupacion = self._ultima_ocupacion
                limpieza = self._ultima_limpieza
            
            print(f"DEBUG (Control): Ocup={ocupacion}%, Limp={limpieza}%. "
                  f"Req: Ocup<{OCUPACION_MAX_PARA_LIMPIEZA}, Limp<{LIMPIEZA_MIN_PARA_LIMPIEZA}")

            # 4. Logica de decision (HU-012)
            if (ocupacion < OCUPACION_MAX_PARA_LIMPIEZA and 
                limpieza < LIMPIEZA_MIN_PARA_LIMPIEZA):
                
                print("INFO (Control): **** CONDICIONES CUMPLIDAS ****")
                print(f"INFO (Control): Iniciando limpieza automatica de '{self._ala_hotel.get_nombre()}'...")
                
                try:
                    # 5. Delegar al servicio
                    self._ala_service.limpiar(self._ala_hotel)
                    
                    # 6. Resetear el sensor de limpieza (simulacion)
                    with self._lock:
                        self._ultima_limpieza = 100.0
                    print("INFO (Control): Limpieza completada. Nivel de limpieza reseteado a 100%.")
                    
                except PresupuestoAgotadoException as e:
                    print(f"ERROR (Control): {e.get_mensaje_usuario()} {e.get_mensaje_tecnico()}")
                    print("ERROR (Control): Limpieza automatica abortada. Reintentando en 30s...")
                    time.sleep(30) # Penalizacion
                except Exception as e:
                    print(f"ERROR (Control): Error inesperado durante la limpieza: {e}")
                    
            # Fin del bucle
        
        print("INFO (Control): Hilo del controlador detenido.")


    def detener(self) -> None:
        """Senala al evento para detener el bucle 'run'."""
        self._detenido.set()


################################################################################
# DIRECTORIO: monitoreo/sensores
################################################################################

# ==============================================================================
# ARCHIVO 30/65: __init__.py
# Directorio: monitoreo/sensores
# Ruta completa: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/monitoreo/sensores/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 31/65: limpieza_reader_task.py
# Directorio: monitoreo/sensores
# Ruta completa: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/monitoreo/sensores/limpieza_reader_task.py
# ==============================================================================

"""
Modulo del Sensor de Nivel de Limpieza (Observable).

Implementa un hilo que simula la lectura de un sensor de limpieza
y notifica a los observadores (Observer).
"""

import threading
import time
import random
from typing import TYPE_CHECKING

from python_hotel.patrones.observer.observable import Observable
from python_hotel.constantes import (
    INTERVALO_SENSOR_LIMPIEZA,
    SENSOR_LIMPIEZA_MIN,
    SENSOR_LIMPIEZA_MAX
)

if TYPE_CHECKING:
    from python_hotel.patrones.observer.observer import Observer


class LimpiezaReaderTask(threading.Thread, Observable[float]):
    """
    Sensor (Observable) que lee el nivel de limpieza.
    """

    def __init__(self):
        threading.Thread.__init__(self, daemon=True)
        Observable.__init__(self)
        self._detenido = threading.Event()
        self._nombre_sensor = "Limpieza"

    def _leer_limpieza_simulada(self) -> float:
        """Metodo privado que simula la lectura de un sensor real."""
        # Simula que el nivel de limpieza tiende a bajar (para que la limpieza se active)
        limpieza = random.uniform(SENSOR_LIMPIEZA_MIN, SENSOR_LIMPIEZA_MAX * 0.8)
        return round(limpieza, 2)

    def run(self) -> None:
        """
        Metodo principal del hilo (se ejecuta con .start()).
        """
        print(f"INFO (Sensor): Hilo del sensor '{self._nombre_sensor}' iniciado.")
        
        while not self._detenido.is_set():
            try:
                valor_leido = self._leer_limpieza_simulada()
                self.notificar_observadores(valor_leido)
                time.sleep(INTERVALO_SENSOR_LIMPIEZA)
                
            except Exception as e:
                print(f"ERROR (Sensor {self._nombre_sensor}): {e}")
                
        print(f"INFO (Sensor): Hilo del sensor '{self._nombre_sensor}' detenido.")

    def detener(self) -> None:
        """Senala al evento para detener el bucle 'run'."""
        self._detenido.set()

# ==============================================================================
# ARCHIVO 32/65: ocupacion_reader_task.py
# Directorio: monitoreo/sensores
# Ruta completa: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/monitoreo/sensores/ocupacion_reader_task.py
# ==============================================================================

"""
Modulo del Sensor de Ocupacion (Observable).

Implementa un hilo que simula la lectura de un sensor de ocupacion
y notifica a los observadores (Observer).
"""

import threading
import time
import random
from typing import TYPE_CHECKING

# Importacion de la clase base Observable
from python_hotel.patrones.observer.observable import Observable
from python_hotel.constantes import (
    INTERVALO_SENSOR_OCUPACION,
    SENSOR_OCUPACION_MIN,
    SENSOR_OCUPACION_MAX
)

if TYPE_CHECKING:
    from python_hotel.patrones.observer.observer import Observer


class OcupacionReaderTask(threading.Thread, Observable[float]):
    """
    Sensor (Observable) que lee la ocupacion.

    Hereda de 'threading.Thread' para correr en un hilo separado.
    Hereda de 'Observable[float]' para poder notificar a observadores
    cuando lee un nuevo valor (float).
    """

    def __init__(self):
        """
        Inicializa el hilo y la clase Observable.
        """
        threading.Thread.__init__(self, daemon=True) # daemon=True para que finalice con el main
        Observable.__init__(self)
        
        # Evento para detener el hilo de forma segura (graceful shutdown)
        self._detenido = threading.Event()
        self._nombre_sensor = "Ocupacion"

    def _leer_ocupacion_simulada(self) -> float:
        """Metodo privado que simula la lectura de un sensor real."""
        # Simula que la ocupacion tiende a ser baja (para que la limpieza se active)
        ocupacion = random.uniform(SENSOR_OCUPACION_MIN, SENSOR_OCUPACION_MAX * 0.3) 
        return round(ocupacion, 2)

    def run(self) -> None:
        """
        Metodo principal del hilo (se ejecuta con .start()).

        Mientras no se detenga, lee el sensor y notifica a los observadores.
        """
        print(f"INFO (Sensor): Hilo del sensor '{self._nombre_sensor}' iniciado.")
        
        while not self._detenido.is_set():
            try:
                # 1. Leer el valor simulado
                valor_leido = self._leer_ocupacion_simulada()
                
                # 2. Notificar a los observadores (Patron Observer)
                self.notificar_observadores(valor_leido)
                
                # 3. Esperar el intervalo
                time.sleep(INTERVALO_SENSOR_OCUPACION)
                
            except Exception as e:
                print(f"ERROR (Sensor {self._nombre_sensor}): {e}")
                
        print(f"INFO (Sensor): Hilo del sensor '{self._nombre_sensor}' detenido.")

    def detener(self) -> None:
        """Senala al evento para detener el bucle 'run'."""
        self._detenido.set()


################################################################################
# DIRECTORIO: patrones
################################################################################

# ==============================================================================
# ARCHIVO 33/65: __init__.py
# Directorio: patrones
# Ruta completa: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/patrones/__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: patrones/factory
################################################################################

# ==============================================================================
# ARCHIVO 34/65: __init__.py
# Directorio: patrones/factory
# Ruta completa: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/patrones/factory/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 35/65: habitacion_factory.py
# Directorio: patrones/factory
# Ruta completa: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/patrones/factory/habitacion_factory.py
# ==============================================================================

"""
Modulo del Patron Factory Method.

Implementa una fabrica (Factory) para la creacion de objetos 'Habitacion',
desacoplando al cliente (servicios) de las clases concretas.
"""

from typing import TYPE_CHECKING, Callable

# Importacion de la ABSTRACCION (interfaz)
from python_hotel.entidades.habitaciones.habitacion import Habitacion

# Importacion de las clases CONCRETAS (solo para type hints)
# Las importaciones reales se hacen DENTRO de los metodos
# para evitar importaciones circulares y cargar solo lo necesario.
if TYPE_CHECKING:
    from python_hotel.entidades.habitaciones.habitacion_simple import HabitacionSimple
    from python_hotel.entidades.habitaciones.habitacion_doble import HabitacionDoble
    from python_hotel.entidades.habitaciones.suite import Suite
    from python_hotel.entidades.habitaciones.suite_presidencial import SuitePresidencial

# Definimos un tipo para nuestro "diccionario de fabricas"
# Es un diccionario que mapea un string a una funcion que no
# toma argumentos y retorna una Habitacion.
FactoryMethodType = Callable[[], Habitacion]


class HabitacionFactory:
    """
    Implementa el patron Factory Method como una clase estatica.
    Centraliza la creacion de todos los tipos de Habitacion.
    """

    @staticmethod
    def _crear_simple() -> 'HabitacionSimple':
        """Metodo 'constructor' privado para HabitacionSimple."""
        from python_hotel.entidades.habitaciones.habitacion_simple import HabitacionSimple
        # Aqui se podria agregar logica de inicializacion compleja si fuese necesario
        return HabitacionSimple()

    @staticmethod
    def _crear_doble() -> 'HabitacionDoble':
        """Metodo 'constructor' privado para HabitacionDoble."""
        from python_hotel.entidades.habitaciones.habitacion_doble import HabitacionDoble
        return HabitacionDoble()

    @staticmethod
    def _crear_suite() -> 'Suite':
        """Metodo 'constructor' privado para Suite."""
        from python_hotel.entidades.habitaciones.suite import Suite
        return Suite()

    @staticmethod
    def _crear_presidencial() -> 'SuitePresidencial':
        """Metodo 'constructor' privado para SuitePresidencial."""
        from python_hotel.entidades.habitaciones.suite_presidencial import SuitePresidencial
        return SuitePresidencial()

    @staticmethod
    def crear_habitacion(tipo: str) -> Habitacion:
        """
        El metodo Factory publico.

        Recibe un string y retorna la instancia de la habitacion correspondiente.

        Args:
            tipo: El string identificador (ej. "Simple", "Suite").

        Returns:
            Una instancia de una subclase de Habitacion.

        Raises:
            ValueError: Si el tipo de habitacion solicitado no esta registrado.
        """
        # Mapeo de string a funcion constructora (Patron Registry simple)
        factories: dict[str, FactoryMethodType] = {
            "Simple": HabitacionFactory._crear_simple,
            "Doble": HabitacionFactory._crear_doble,
            "Suite": HabitacionFactory._crear_suite,
            "Presidencial": HabitacionFactory._crear_presidencial
            # Para agregar un nuevo tipo, solo anadimos una linea aqui
        }

        # Obtenemos la funcion constructora del diccionario
        constructor_func = factories.get(tipo)

        if not constructor_func:
            raise ValueError(f"Tipo de habitación desconocido: '{tipo}'")

        # Ejecutamos la funcion constructora (ej. _crear_simple())
        nueva_habitacion = constructor_func()
        
        print(f"INFO (Factory): Creada nueva habitacion ID {nueva_habitacion.get_id()} (Tipo: {tipo})")
        return nueva_habitacion


################################################################################
# DIRECTORIO: patrones/observer
################################################################################

# ==============================================================================
# ARCHIVO 36/65: __init__.py
# Directorio: patrones/observer
# Ruta completa: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/patrones/observer/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 37/65: observable.py
# Directorio: patrones/observer
# Ruta completa: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/patrones/observer/observable.py
# ==============================================================================

"""
Modulo de la Clase Base para el Patron Observer (El Observable).
"""

from abc import ABC
from typing import Generic, TypeVar, List
from python_hotel.patrones.observer.observer import Observer

# Se usa el mismo TypeVar 'T' que en la interfaz Observer
T = TypeVar('T')

class Observable(Generic[T], ABC):
    """
    Clase base generica para el Sujeto (Observable).

    Gestiona una lista de Observadores y notifica cambios.
    Nuestros sensores (OcupacionReaderTask, LimpiezaReaderTask)
    heredaran de esta clase.
    """

    def __init__(self):
        """Inicializa la lista de observadores."""
        # La lista es de tipo Observer[T], haciendola tipo-seguro.
        self._observadores: List[Observer[T]] = []

    def agregar_observador(self, observador: Observer[T]) -> None:
        """
        Agrega un nuevo observador a la lista.

        Args:
            observador: La instancia que implementa la interfaz Observer[T].
        """
        if observador not in self._observadores:
            self._observadores.append(observador)

    def eliminar_observador(self, observador: Observer[T]) -> None:
        """
        Elimina un observador de la lista.

        Args:
            observador: La instancia a eliminar.
        """
        try:
            self._observadores.remove(observador)
        except ValueError:
            # Falla silenciosamente si el observador no estaba registrado
            pass

    def notificar_observadores(self, evento: T) -> None:
        """
        Notifica a todos los observadores suscritos.

        Itera sobre la lista de observadores y llama a su metodo 'actualizar',
        pasandoles el evento.

        Args:
            evento: El dato a notificar (ej. la lectura del sensor).
        """
        # Se itera sobre una copia de la lista ([:]) para permitir
        # que un observador se elimine a si mismo durante la notificacion
        # sin romper el bucle.
        for observador in self._observadores[:]:
            observador.actualizar(evento)

# ==============================================================================
# ARCHIVO 38/65: observer.py
# Directorio: patrones/observer
# Ruta completa: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/patrones/observer/observer.py
# ==============================================================================

"""
Modulo de la Interfaz (ABC) para el Patron Observer (El Observador).
"""

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

# Se define un Tipo Generico 'T'
# Esto permite que el observador sea tipo-seguro.
# Podra observar eventos de tipo float, str, o cualquier objeto.
T = TypeVar('T')

class Observer(Generic[T], ABC):
    """
    Interfaz abstracta (ABC) para el Observador.

    Define el metodo 'actualizar' que sera llamado por el Observable
    cuando ocurra un evento.
    """

    @abstractmethod
    def actualizar(self, evento: T) -> None:
        """
        Metodo llamado por el Observable.

        Args:
            evento: El dato que el Observable esta notificando.
                    En nuestro caso (sensores), sera un 'float'.
        """
        pass


################################################################################
# DIRECTORIO: patrones/observer/eventos
################################################################################

# ==============================================================================
# ARCHIVO 39/65: __init__.py
# Directorio: patrones/observer/eventos
# Ruta completa: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/patrones/observer/eventos/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 40/65: evento_hotel.py
# Directorio: patrones/observer/eventos
# Ruta completa: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/patrones/observer/eventos/evento_hotel.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 41/65: evento_sensor.py
# Directorio: patrones/observer/eventos
# Ruta completa: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/patrones/observer/eventos/evento_sensor.py
# ==============================================================================




################################################################################
# DIRECTORIO: patrones/singleton
################################################################################

# ==============================================================================
# ARCHIVO 42/65: __init__.py
# Directorio: patrones/singleton
# Ruta completa: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/patrones/singleton/__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: patrones/strategy
################################################################################

# ==============================================================================
# ARCHIVO 43/65: __init__.py
# Directorio: patrones/strategy
# Ruta completa: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/patrones/strategy/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 44/65: mantenimiento_strategy.py
# Directorio: patrones/strategy
# Ruta completa: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/patrones/strategy/mantenimiento_strategy.py
# ==============================================================================

"""
Modulo de la Interfaz (ABC) para el Patron Strategy.

Define el contrato que todas las estrategias concretas de mantenimiento
deben implementar.
"""

from abc import ABC, abstractmethod
from datetime import date
from typing import TYPE_CHECKING

# Importacion solo para type hints
if TYPE_CHECKING:
    from python_hotel.entidades.habitaciones.habitacion import Habitacion

class MantenimientoStrategy(ABC):
    """
    Interfaz abstracta (ABC) para el patron Strategy.

    Define un algoritmo intercambiable para calcular el tiempo de
    mantenimiento de una habitacion.
    """

    @abstractmethod
    def calcular_mantenimiento(
        self,
        fecha: date,
        ocupacion_actual_ala: float,
        habitacion: 'Habitacion'
    ) -> int:
        """
        Calcula el tiempo de mantenimiento requerido (en minutos).

        Args:
            fecha: Fecha actual, por si la estrategia depende de la temporada.
            ocupacion_actual_ala: Nivel de ocupacion del ala (0.0 a 100.0).
            habitacion: La instancia de la habitacion a mantener.

        Returns:
            El tiempo total en minutos requerido para el mantenimiento.
        """
        pass


################################################################################
# DIRECTORIO: patrones/strategy/impl
################################################################################

# ==============================================================================
# ARCHIVO 45/65: __init__.py
# Directorio: patrones/strategy/impl
# Ruta completa: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/patrones/strategy/impl/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 46/65: mantenimiento_estandar_strategy.py
# Directorio: patrones/strategy/impl
# Ruta completa: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/patrones/strategy/impl/mantenimiento_estandar_strategy.py
# ==============================================================================

"""
Estrategia Concreta: Mantenimiento Estandar.

Aplica para HabitacionSimple y HabitacionDoble.
"""

from python_hotel.patrones.strategy.mantenimiento_strategy import MantenimientoStrategy
from python_hotel.constantes import (
    MANTENIMIENTO_ESTANDAR_BASICO,
    MANTENIMIENTO_ESTANDAR_COMPLETO,
    UMBRAL_OCUPACION_ESTANDAR
)
from datetime import date
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_hotel.entidades.habitaciones.habitacion import Habitacion

class MantenimientoEstandarStrategy(MantenimientoStrategy):
    """
    Estrategia concreta para habitaciones estandar (Simple, Doble).

    El tiempo de mantenimiento es variable:
    - Si la ocupacion del ala es baja (< 30%), se hace limpieza completa (60 min).
    - Si la ocupacion es alta (>= 30%), se hace limpieza basica (30 min).
    """

    def calcular_mantenimiento(
        self,
        fecha: date,
        ocupacion_actual_ala: float,
        habitacion: 'Habitacion'
    ) -> int:
        """
        Calcula el tiempo de mantenimiento (en minutos) basado en la ocupacion.

        Args:
            fecha: Fecha actual (ignorado en esta estrategia).
            ocupacion_actual_ala: Nivel de ocupacion del ala (0.0 a 100.0).
            habitacion: La habitacion a mantener (ignorada en esta estrategia).

        Returns:
            El tiempo total en minutos requerido.
        """
        
        # Logica condicional basada en la ocupacion
        if ocupacion_actual_ala < UMBRAL_OCUPACION_ESTANDAR:
            # Baja ocupacion -> Limpieza completa
            return MANTENIMIENTO_ESTANDAR_COMPLETO
        else:
            # Alta ocupacion -> Limpieza basica
            return MANTENIMIENTO_ESTANDAR_BASICO

# ==============================================================================
# ARCHIVO 47/65: mantenimiento_premium_strategy.py
# Directorio: patrones/strategy/impl
# Ruta completa: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/patrones/strategy/impl/mantenimiento_premium_strategy.py
# ==============================================================================

"""
Estrategia Concreta: Mantenimiento Premium.

Aplica para Suite y SuitePresidencial.
"""

from python_hotel.patrones.strategy.mantenimiento_strategy import MantenimientoStrategy
from datetime import date
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_hotel.entidades.habitaciones.habitacion import Habitacion

class MantenimientoPremiumStrategy(MantenimientoStrategy):
    """
    Estrategia concreta para habitaciones premium (Suite, Presidencial).

    El tiempo de mantenimiento es siempre constante, independientemente
    de la ocupacion. El tiempo exacto (ej. 60 o 90 min) se inyecta
    en el constructor.
    """

    def __init__(self, tiempo_constante_minutos: int):
        """
        Args:
            tiempo_constante_minutos: El tiempo fijo (ej. 60 para Suite).
        """
        if tiempo_constante_minutos <= 0:
            raise ValueError("El tiempo de mantenimiento debe ser positivo.")
        self._tiempo_constante = tiempo_constante_minutos

    def calcular_mantenimiento(
        self,
        fecha: date,
        ocupacion_actual_ala: float,
        habitacion: 'Habitacion'
    ) -> int:
        """
        Calcula el tiempo de mantenimiento (en minutos).

        Args:
            fecha: Fecha actual (ignorado).
            ocupacion_actual_ala: Nivel de ocupacion (ignorado).
            habitacion: La habitacion a mantener (ignorado).

        Returns:
            El tiempo total en minutos (siempre el valor constante).
        """
        
        # La logica es simple: siempre retorna el valor constante
        return self._tiempo_constante


################################################################################
# DIRECTORIO: servicios
################################################################################

# ==============================================================================
# ARCHIVO 48/65: __init__.py
# Directorio: servicios
# Ruta completa: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/servicios/__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: servicios/habitaciones
################################################################################

# ==============================================================================
# ARCHIVO 49/65: __init__.py
# Directorio: servicios/habitaciones
# Ruta completa: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/servicios/habitaciones/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 50/65: habitacion_base_service.py
# Directorio: servicios/habitaciones
# Ruta completa: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/servicios/habitaciones/habitacion_base_service.py
# ==============================================================================

"""
Servicio Base para Habitaciones Estandar (Simple, Doble).
"""

from python_hotel.servicios.habitaciones.habitacion_service import HabitacionService
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_hotel.entidades.habitaciones.habitacion_base import HabitacionBase

class HabitacionBaseService(HabitacionService):
    """
    Servicio intermedio para logica compartida por habitaciones
    estandar (Simple y Doble).
    """
    
    # No necesita __init__, ya que solo pasa la estrategia
    # que recibe de sus clases hijas (SimpleService, DobleService)
    # hacia el padre (HabitacionService).

    def mostrar_datos(self, habitacion: 'HabitacionBase') -> None:
        """
        Muestra datos base (de HabitacionService) y los especificos
        de HabitacionBase.
        """
        super().mostrar_datos(habitacion) # Llama al padre
        print(f"Serv. Basicos: {'Si' if habitacion.tiene_servicios_basicos() else 'No'}")

# ==============================================================================
# ARCHIVO 51/65: habitacion_doble_service.py
# Directorio: servicios/habitaciones
# Ruta completa: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/servicios/habitaciones/habitacion_doble_service.py
# ==============================================================================

"""
Servicio Concreto para HabitacionDoble.
"""

from python_hotel.servicios.habitaciones.habitacion_base_service import HabitacionBaseService
from python_hotel.patrones.strategy.impl.mantenimiento_estandar_strategy import MantenimientoEstandarStrategy
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_hotel.entidades.habitaciones.habitacion_doble import HabitacionDoble


class HabitacionDobleService(HabitacionBaseService):
    """
    Servicio concreto con la logica de negocio para HabitacionDoble.
    """

    def __init__(self):
        """
        Inyecta la estrategia especifica (MantenimientoEstandarStrategy)
        en el constructor de la clase padre.
        """
        # --- INYECCION DE DEPENDENCIA ---
        super().__init__(MantenimientoEstandarStrategy())
        
    def mostrar_datos(self, habitacion: 'HabitacionDoble') -> None:
        """Muestra todos los datos de la habitacion doble."""
        super().mostrar_datos(habitacion) # Llama al padre (HabitacionBaseService)
        print(f"Desayuno:     {'Incluido' if habitacion.tiene_desayuno_incluido() else 'No incluido'}")

# ==============================================================================
# ARCHIVO 52/65: habitacion_service.py
# Directorio: servicios/habitaciones
# Ruta completa: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/servicios/habitaciones/habitacion_service.py
# ==============================================================================

"""
Modulo del Servicio Base Abstracto para Habitaciones.

Define la funcionalidad comun para todos los servicios de habitacion,
incluyendo la logica del Patron Strategy.
"""

from abc import ABC, abstractmethod
from datetime import date
from typing import TYPE_CHECKING

# Importacion de la ABSTRACCION del patron
from python_hotel.patrones.strategy.mantenimiento_strategy import MantenimientoStrategy

if TYPE_CHECKING:
    from python_hotel.entidades.habitaciones.habitacion import Habitacion


class HabitacionService(ABC):
    """
    Servicio base abstracto (ABC) para la logica de negocio de Habitaciones.

    Contiene la logica de inyeccion de dependencias para el Patron Strategy.
    """

    def __init__(self, estrategia_mantenimiento: MantenimientoStrategy):
        """
        Inicializa el servicio base.

        Args:
            estrategia_mantenimiento: Una instancia de una clase que
                implemente la interfaz MantenimientoStrategy.
                (Esto es Inyeccion de Dependencias).
        """
        if not isinstance(estrategia_mantenimiento, MantenimientoStrategy):
            raise TypeError("El argumento debe ser una instancia de MantenimientoStrategy.")
        self._estrategia_mantenimiento = estrategia_mantenimiento

    def realizar_mantenimiento(self, habitacion: 'Habitacion', ocupacion_ala: float) -> int:
        """
        Realiza el mantenimiento de una habitacion.

        Esta es la funcion 'Contexto' del Patron Strategy.
        Delega el calculo del tiempo a la estrategia inyectada.

        Args:
            habitacion: La instancia de la habitacion a mantener.
            ocupacion_ala: El nivel de ocupacion actual del ala.

        Returns:
            El tiempo (en minutos) que tomo el mantenimiento.
        """
        from python_hotel.constantes import ESTADO_MANTENIMIENTO
        
        # --- DELEGACION (Patron Strategy) ---
        # Llama al metodo de la estrategia (sea cual sea)
        tiempo_requerido = self._estrategia_mantenimiento.calcular_mantenimiento(
            fecha=date.today(),
            ocupacion_actual_ala=ocupacion_ala,
            habitacion=habitacion
        )
        
        # Logica de negocio comun
        habitacion.set_estado(ESTADO_MANTENIMIENTO)
        print(f"INFO: Iniciando mantenimiento de {tiempo_requerido} min "
              f"para Habitación ID {habitacion.get_id()}...")
        
        return tiempo_requerido

    @abstractmethod
    def mostrar_datos(self, habitacion: 'Habitacion') -> None:
        """
        Metodo abstracto para mostrar datos.
        Sera implementado por servicios concretos y usado por el Registry.
        """
        # Logica base que todas las implementaciones llamaran con super()
        print(f"\n--- Datos Habitacion ID: {habitacion.get_id()} ---")
        print(f"Tipo:         {habitacion.get_tipo_habitacion()}")
        print(f"Capacidad:    {habitacion.get_capacidad()} personas")
        print(f"Tarifa:       ${habitacion.get_tarifa_base():.2f}")
        print(f"Estado:       {habitacion.get_estado()}")

# ==============================================================================
# ARCHIVO 53/65: habitacion_service_registry.py
# Directorio: servicios/habitaciones
# Ruta completa: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/servicios/habitaciones/habitacion_service_registry.py
# ==============================================================================

"""
Modulo del HabitacionServiceRegistry (Patrones Singleton + Registry).

Esta clase unica gestiona el acceso a todos los servicios de habitacion,
permitiendo el dispatch polimorfico sin usar 'isinstance'.
"""

from threading import Lock
from typing import Callable, TYPE_CHECKING

# Importacion de la ABSTRACCION
from python_hotel.entidades.habitaciones.habitacion import Habitacion

# Importacion de las ENTIDADES CONCRETAS (para usar como llaves del dict)
from python_hotel.entidades.habitaciones.habitacion_simple import HabitacionSimple
from python_hotel.entidades.habitaciones.habitacion_doble import HabitacionDoble
from python_hotel.entidades.habitaciones.suite import Suite
from python_hotel.entidades.habitaciones.suite_presidencial import SuitePresidencial

# Importacion de los SERVICIOS CONCRETOS (para usarlos en los handlers)
from python_hotel.servicios.habitaciones.habitacion_simple_service import HabitacionSimpleService
from python_hotel.servicios.habitaciones.habitacion_doble_service import HabitacionDobleService
from python_hotel.servicios.habitaciones.suite_service import SuiteService
from python_hotel.servicios.habitaciones.suite_presidencial_service import SuitePresidencialService

# Definicion de tipos para nuestros handlers del Registry
HandlerMostrarDatos = Callable[[Habitacion], None]
HandlerMantenimiento = Callable[[Habitacion, float], int]


class HabitacionServiceRegistry:
    """
    Implementa los patrones Singleton y Registry.

    - Singleton: Asegura una unica instancia (thread-safe).
    - Registry: Mapea tipos de Habitacion a sus servicios especificos.
    """

    # --- Implementacion del Patron Singleton ---
    _instance = None
    _lock = Lock()  # Lock para hacerlo thread-safe

    def __new__(cls):
        """
        Controla la creacion de la instancia (Singleton).
        """
        if cls._instance is None:
            with cls._lock:
                # Doble chequeo de bloqueo (Double-Checked Locking)
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    # Inicializamos los servicios solo una vez
                    cls._instance._inicializar_servicios_y_registry()
        return cls._instance

    @classmethod
    def get_instance(cls):
        """
        Metodo de clase para obtener la instancia unica.
        """
        # Llama a __new__ si _instance es None
        return cls() 
    
    # --- Implementacion del Patron Registry ---

    def _inicializar_servicios_y_registry(self):
        """
        Metodo privado llamado UNA SOLA VEZ por el __new__ para
        instanciar los servicios y construir los diccionarios (registros).
        """
        
        # 1. Instanciar todos los servicios (los mantendra en memoria)
        self._simple_service = HabitacionSimpleService()
        self._doble_service = HabitacionDobleService()
        self._suite_service = SuiteService()
        self._presidencial_service = SuitePresidencialService()

        # 2. Crear el diccionario (Registro) para 'mostrar_datos'
        self._mostrar_datos_handlers: dict[type[Habitacion], HandlerMostrarDatos] = {
            HabitacionSimple: self._simple_service.mostrar_datos,
            HabitacionDoble: self._doble_service.mostrar_datos,
            Suite: self._suite_service.mostrar_datos,
            SuitePresidencial: self._presidencial_service.mostrar_datos
        }
        
        # 3. Crear el diccionario (Registro) para 'realizar_mantenimiento'
        self._mantenimiento_handlers: dict[type[Habitacion], HandlerMantenimiento] = {
            HabitacionSimple: self._simple_service.realizar_mantenimiento,
            HabitacionDoble: self._doble_service.realizar_mantenimiento,
            Suite: self._suite_service.realizar_mantenimiento,
            SuitePresidencial: self._presidencial_service.realizar_mantenimiento
        }
        
        print("\nINFO (Singleton): Instancia de HabitacionServiceRegistry creada.")
        print("INFO (Registry):  Servicios de habitacion inicializados y registrados.")


    def _obtener_handler(self, habitacion: Habitacion, registry: dict):
        """Metodo helper para obtener el handler correcto."""
        tipo_habitacion = type(habitacion)
        handler = registry.get(tipo_habitacion)
        
        if not handler:
            raise TypeError(f"Tipo de habitacion no registrado en el Registry: {tipo_habitacion.__name__}")
        
        return handler

    # --- Metodos Publicos del Registry (Dispatchers) ---

    def mostrar_datos(self, habitacion: Habitacion) -> None:
        """
        Metodo de dispatch polimorfico para mostrar_datos.

        Obtiene el tipo de la habitacion y llama al metodo
        'mostrar_datos' del servicio correspondiente.

        Args:
            habitacion: La instancia de la habitacion (Simple, Doble, etc.).
        """
        try:
            handler = self._obtener_handler(habitacion, self._mostrar_datos_handlers)
            handler(habitacion) # Ejecuta el metodo (ej. _simple_service.mostrar_datos(hab))
        except TypeError as e:
            print(f"ERROR (Registry): {e}")

    def realizar_mantenimiento(self, habitacion: Habitacion, ocupacion_ala: float) -> int:
        """
        Metodo de dispatch polimorfico para realizar_mantenimiento.

        Obtiene el tipo de la habitacion y llama al metodo
        'realizar_mantenimiento' del servicio correspondiente.

        Args:
            habitacion: La instancia de la habitacion.
            ocupacion_ala: La ocupacion actual del ala.

        Returns:
            El tiempo de mantenimiento en minutos.
        """
        try:
            handler = self._obtener_handler(habitacion, self._mantenimiento_handlers)
            # Ejecuta el metodo (ej. _suite_service.realizar_mantenimiento(hab, ocupacion))
            return handler(habitacion, ocupacion_ala)
        except TypeError as e:
            print(f"ERROR (Registry): {e}")
            return 0 # Retornar un valor seguro en caso de error

# ==============================================================================
# ARCHIVO 54/65: habitacion_simple_service.py
# Directorio: servicios/habitaciones
# Ruta completa: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/servicios/habitaciones/habitacion_simple_service.py
# ==============================================================================

"""
Servicio Concreto para HabitacionSimple.
"""

from python_hotel.servicios.habitaciones.habitacion_base_service import HabitacionBaseService
from python_hotel.patrones.strategy.impl.mantenimiento_estandar_strategy import MantenimientoEstandarStrategy
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_hotel.entidades.habitaciones.habitacion_simple import HabitacionSimple


class HabitacionSimpleService(HabitacionBaseService):
    """
    Servicio concreto con la logica de negocio para HabitacionSimple.
    """

    def __init__(self):
        """
        Inyecta la estrategia especifica (MantenimientoEstandarStrategy)
        en el constructor de la clase padre.
        """
        # --- INYECCION DE DEPENDENCIA ---
        super().__init__(MantenimientoEstandarStrategy())
        
    def mostrar_datos(self, habitacion: 'HabitacionSimple') -> None:
        """Muestra todos los datos de la habitacion simple."""
        super().mostrar_datos(habitacion) # Llama al padre (HabitacionBaseService)
        print(f"Cama:         {habitacion.get_tamano_cama()}")

# ==============================================================================
# ARCHIVO 55/65: suite_presidencial_service.py
# Directorio: servicios/habitaciones
# Ruta completa: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/servicios/habitaciones/suite_presidencial_service.py
# ==============================================================================

"""
Servicio Concreto para SuitePresidencial.
"""

from python_hotel.servicios.habitaciones.habitacion_service import HabitacionService
from python_hotel.patrones.strategy.impl.mantenimiento_premium_strategy import MantenimientoPremiumStrategy
from python_hotel.constantes import MANTENIMIENTO_PREMIUM_PRESIDENCIAL
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_hotel.entidades.habitaciones.suite_presidencial import SuitePresidencial


class SuitePresidencialService(HabitacionService):
    """
    Servicio concreto con la logica de negocio para SuitePresidencial.
    """

    def __init__(self):
        """
        Inyecta la estrategia Premium, pasando el tiempo constante (90 min)
        desde el archivo de constantes.
        """
        # --- INYECCION DE DEPENDENCIA ---
        super().__init__(MantenimientoPremiumStrategy(MANTENIMIENTO_PREMIUM_PRESIDENCIAL))
        
    def mostrar_datos(self, habitacion: 'SuitePresidencial') -> None:
        """Muestra todos los datos de la suite presidencial."""
        super().mostrar_datos(habitacion) # Llama al padre (HabitacionService)
        print(f"Amenities:    {', '.join(habitacion.get_amenities())}")
        print(f"Terraza:      {'Si' if habitacion.tiene_terraza() else 'No'}")

# ==============================================================================
# ARCHIVO 56/65: suite_service.py
# Directorio: servicios/habitaciones
# Ruta completa: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/servicios/habitaciones/suite_service.py
# ==============================================================================

"""
Servicio Concreto para Suite.
"""

from python_hotel.servicios.habitaciones.habitacion_service import HabitacionService
from python_hotel.patrones.strategy.impl.mantenimiento_premium_strategy import MantenimientoPremiumStrategy
from python_hotel.constantes import MANTENIMIENTO_PREMIUM_SUITE
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_hotel.entidades.habitaciones.suite import Suite


class SuiteService(HabitacionService):
    """
    Servicio concreto con la logica de negocio para Suite.
    """

    def __init__(self):
        """
        Inyecta la estrategia Premium, pasando el tiempo constante (60 min)
        desde el archivo de constantes.
        """
        # --- INYECCION DE DEPENDENCIA ---
        super().__init__(MantenimientoPremiumStrategy(MANTENIMIENTO_PREMIUM_SUITE))
        
    def mostrar_datos(self, habitacion: 'Suite') -> None:
        """Muestra todos los datos de la suite."""
        super().mostrar_datos(habitacion) # Llama al padre (HabitacionService)
        print(f"Amenities:    {', '.join(habitacion.get_amenities())}")
        print(f"Room Service: {'24h' if habitacion.tiene_room_service_24h() else 'No disponible'}")


################################################################################
# DIRECTORIO: servicios/hotel
################################################################################

# ==============================================================================
# ARCHIVO 57/65: __init__.py
# Directorio: servicios/hotel
# Ruta completa: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/servicios/hotel/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 58/65: ala_hotel_service.py
# Directorio: servicios/hotel
# Ruta completa: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/servicios/hotel/ala_hotel_service.py
# ==============================================================================

"""
Modulo del Servicio de AlaHotel.

Logica de negocio para gestionar un AlaHotel:
- Configurar habitaciones (usando Factory)
- Limpiar habitaciones (usando Registry y Strategy)
- Gestionar presupuesto y capacidad (usando Excepciones)
"""

from typing import TYPE_CHECKING, Type
from python_hotel.entidades.hotel.ala_hotel import AlaHotel
from python_hotel.entidades.habitaciones.habitacion import Habitacion

# --- Dependencia del Factory (Paso 4) ---
from python_hotel.patrones.factory.habitacion_factory import HabitacionFactory

# --- Dependencia del Registry (Paso 5) ---
from python_hotel.servicios.habitaciones.habitacion_service_registry import HabitacionServiceRegistry

# --- Dependencia de Excepciones (Paso 1) ---
from python_hotel.excepciones.capacidad_insuficiente_exception import CapacidadInsuficienteException
from python_hotel.excepciones.presupuesto_agotado_exception import PresupuestoAgotadoException

# --- Dependencia de Constantes (Paso 1) ---
from python_hotel.constantes import COSTE_LIMPIEZA_ALA, ESTADO_INICIAL_HABITACION

if TYPE_CHECKING:
    from python_hotel.entidades.personal.empleado import Empleado


class AlaHotelService:
    """
    Servicio 'stateless' para operaciones de negocio sobre un AlaHotel.
    Este servicio orquesta los patrones Factory y Registry.
    """

    def __init__(self):
        """
        Inicializa el servicio. Obtenemos la instancia del Registry
        que usaremos para 'limpiar'.
        """
        # Obtenemos la instancia unica del Singleton/Registry
        self._registry = HabitacionServiceRegistry.get_instance()
        # Mantenemos una referencia estatica al Factory
        self._factory = HabitacionFactory

    def configurar_habitaciones(self, 
                                ala_hotel: AlaHotel, 
                                tipo_habitacion: str, 
                                cantidad: int) -> list[Habitacion]:
        """
        Configura (crea y agrega) nuevas habitaciones en un ala.
        Utiliza el Factory Method para la creacion.

        Args:
            ala_hotel: La instancia del ala a modificar.
            tipo_habitacion: El string del tipo (ej. "Simple", "Suite").
            cantidad: Cuantas habitaciones de ese tipo crear.

        Returns:
            La lista de habitaciones recien creadas.
            
        Raises:
            CapacidadInsuficienteException: Si no hay capacidad para
                                            tantas habitaciones.
            ValueError: Si el tipo de habitacion es invalido (desde el Factory).
        """
        print(f"\nINFO: Solicitud para configurar {cantidad} habitacion(es) tipo '{tipo_habitacion}' en '{ala_hotel.get_nombre()}'...")
        
        # 1. Usar el Factory para crear UNA habitacion temporal y medir su capacidad
        #    Esto evita hardcodear la capacidad de cada tipo aqui.
        try:
            temp_hab = self._factory.crear_habitacion(tipo_habitacion)
            capacidad_requerida_total = temp_hab.get_capacidad() * cantidad
        except ValueError as e:
            print(f"ERROR (Servicio): {e}")
            raise # Re-lanzar el error del factory

        # 2. Validar capacidad (Logica de negocio)
        capacidad_disponible = ala_hotel.get_capacidad_disponible()
        
        if capacidad_requerida_total > capacidad_disponible:
            print(f"ERROR: Capacidad insuficiente. Requeridas: {capacidad_requerida_total}, "
                  f"Disponibles: {capacidad_disponible}")
            raise CapacidadInsuficienteException(
                capacidad_disponible=capacidad_disponible,
                capacidad_requerida=capacidad_requerida_total
            )

        # 3. Si hay capacidad, crear el resto de habitaciones
        #    (Re-usamos la primera que ya creamos)
        habitaciones_creadas = [temp_hab]
        for _ in range(cantidad - 1):
            habitaciones_creadas.append(self._factory.crear_habitacion(tipo_habitacion))

        # 4. Agregar las habitaciones al Ala
        for hab in habitaciones_creadas:
            ala_hotel.add_habitacion(hab)
            
        print(f"INFO: Exito. {cantidad} habitaciones agregadas. "
              f"Capacidad restante: {ala_hotel.get_capacidad_disponible()}")
        
        return habitaciones_creadas

    def limpiar(self, ala_hotel: AlaHotel) -> tuple[int, float]:
        """
        Limpia TODAS las habitaciones del ala.
        Utiliza el Registry para el dispatch polimorfico del mantenimiento.
        Utiliza el Strategy (automaticamente) para calcular tiempos.

        Args:
            ala_hotel: El ala a limpiar.

        Returns:
            Una tupla (tiempo_total_minutos, coste_total).

        Raises:
            PresupuestoAgotadoException: Si no hay presupuesto para la limpieza.
        """
        print(f"\nINFO: Iniciando ciclo de limpieza para '{ala_hotel.get_nombre()}'...")
        
        # 1. Validar presupuesto (Logica de negocio)
        presupuesto_actual = ala_hotel.get_presupuesto_disponible()
        
        if presupuesto_actual < COSTE_LIMPIEZA_ALA:
            print(f"ERROR: Presupuesto agotado. Requerido: {COSTE_LIMPIEZA_ALA}, "
                  f"Disponible: {presupuesto_actual}")
            raise PresupuestoAgotadoException(
                presupuesto_disponible=presupuesto_actual,
                coste_requerido=COSTE_LIMPIEZA_ALA
            )
            
        # 2. Cobrar el coste de limpieza
        ala_hotel.set_presupuesto_disponible(presupuesto_actual - COSTE_LIMPIEZA_ALA)
        print(f"INFO: Coste de ${COSTE_LIMPIEZA_ALA} debitado. "
              f"Presupuesto restante: ${ala_hotel.get_presupuesto_disponible():.2f}")

        # 3. Simular ocupacion actual (para la estrategia Estandar)
        #    En un sistema real, esto vendria de los sensores.
        ocupacion_simulada = 50.0 # Simulamos alta ocupacion (limpieza rapida)

        # 4. Iterar y limpiar (Dispatch con Registry)
        tiempo_total_mantenimiento = 0
        habitaciones_a_limpiar = ala_hotel.get_habitaciones()
        
        if not habitaciones_a_limpiar:
            print("INFO: No hay habitaciones configuradas para limpiar.")
            return 0, COSTE_LIMPIEZA_ALA

        for hab in habitaciones_a_limpiar:
            # --- Patron Registry + Strategy en accion ---
            # Llamamos al Registry, que llama al Servicio especifico,
            # que a su vez delega en la Estrategia inyectada.
            tiempo_hab = self._registry.realizar_mantenimiento(hab, ocupacion_simulada)
            tiempo_total_mantenimiento += tiempo_hab
            
            # Post-limpieza: marcar como disponible
            hab.set_estado(ESTADO_INICIAL_HABITACION)

        print(f"INFO: Ciclo de limpieza completado. "
              f"Tiempo total: {tiempo_total_mantenimiento} minutos.")
        
        return tiempo_total_mantenimiento, COSTE_LIMPIEZA_ALA

    def desinfectar(self, ala_hotel: AlaHotel, tipo_desinfectante: str) -> None:
        """
        Aplica una desinfeccion a toda el ala.
        (Operacion simple de negocio).
        """
        print(f"\nINFO: Desinfectando '{ala_hotel.get_nombre()}' "
              f"con '{tipo_desinfectante}'...")
        # En un sistema real, esto podria afectar el presupuesto
        # o el estado de las habitaciones.
        print("INFO: Desinfeccion completada.")

    def asignar_empleados(self, ala_hotel: AlaHotel, empleados: list['Empleado']) -> None:
        """
        Asigna una lista de empleados al ala.
        """
        ala_hotel.set_empleados(empleados)
        print(f"\nINFO: {len(empleados)} empleados asignados a '{ala_hotel.get_nombre()}'.")

    def realizar_checkout_por_tipo(self, ala_hotel: AlaHotel, tipo_habitacion: Type[Habitacion]) -> int:
        """
        Procesa el check-out de todas las habitaciones de un tipo especifico.
        
        Args:
            ala_hotel: El ala donde buscar.
            tipo_habitacion: La *clase* de la habitacion (ej. HabitacionSimple).

        Returns:
            El numero de habitaciones procesadas.
        """
        count = 0
        for hab in ala_hotel.get_habitaciones():
            if isinstance(hab, tipo_habitacion):
                hab.set_estado(ESTADO_INICIAL_HABITACION)
                count += 1
        
        print(f"\nINFO: Check-out procesado para {count} habitaciones "
              f"tipo '{tipo_habitacion.__name__}'.")
        return count

# ==============================================================================
# ARCHIVO 59/65: hotel_service.py
# Directorio: servicios/hotel
# Ruta completa: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/servicios/hotel/hotel_service.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 60/65: registro_hotelero_service.py
# Directorio: servicios/hotel
# Ruta completa: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/servicios/hotel/registro_hotelero_service.py
# ==============================================================================

"""
Modulo del Servicio de RegistroHotelero.

Logica de negocio para persistir (guardar) y recuperar (leer)
la entidad RegistroHotelero usando Pickle.
"""

import os
import pickle
from typing import TYPE_CHECKING

from python_hotel.entidades.hotel.registro_hotelero import RegistroHotelero
from python_hotel.constantes import DIRECTORIO_DATA, EXTENSION_DATA
from python_hotel.excepciones.persistencia_exception import (
    PersistenciaException,
    TipoOperacionPersistencia
)

# --- Dependencia del Paso 5 ---
# Importamos esto sabiendo que lo crearemos en el siguiente paso.
from python_hotel.servicios.habitaciones.habitacion_service_registry import HabitacionServiceRegistry
# -----------------------------

if TYPE_CHECKING:
    from python_hotel.entidades.habitaciones.habitacion import Habitacion


class RegistroHoteleroService:
    """
    Servicio 'stateless' para operaciones de persistencia (Pickle)
    y visualizacion del RegistroHotelero.
    """

    def __init__(self):
        """
        Inicializa el servicio. Obtenemos la instancia del Registry
        que usaremos en 'mostrar_datos'.
        """
        # Obtenemos la instancia unica del Singleton
        self._registry = HabitacionServiceRegistry.get_instance()

    def mostrar_datos(self, registro: RegistroHotelero) -> None:
        """
        Muestra en consola un resumen completo del registro,
        incluyendo los detalles de cada habitacion.
        """
        if not registro:
            print("ERROR: Registro no proporcionado.")
            return

        ala = registro.get_ala_hotel()
        hotel = registro.get_hotel()
        habitaciones = ala.get_habitaciones()

        print("\n=======================================================")
        print("          REGISTRO HOTELERO - DETALLE COMPLETO")
        print("=======================================================")
        print(f"Propietario:   {registro.get_propietario()}")
        print(f"Hotel ID:      {registro.get_id_hotel()}")
        print(f"Avaluo Fiscal: ${registro.get_avaluo():,.2f}")
        print("-------------------------------------------------------")
        print("--- Datos del Hotel ---")
        print(f"Direccion:     {hotel.get_direccion()}")
        print(f"Capacidad Max: {hotel.get_capacidad()} personas")
        print("--- Datos del Ala ---")
        print(f"Nombre:        {ala.get_nombre()}")
        print(f"Presupuesto:   ${ala.get_presupuesto_disponible():,.2f}")
        print(f"Cap. Ocupada:  {ala.get_capacidad_ocupada()} personas")
        print(f"Habitaciones:  {len(habitaciones)} unidades")
        print("-------------------------------------------------------")
        print("--- Listado de Habitaciones Configradas ---")
        
        if not habitaciones:
            print("(No hay habitaciones configuradas)")
        else:
            # --- Patron Registry en accion ---
            # Usamos el registry para llamar al 'mostrar_datos'
            # especifico de cada tipo de habitacion, sin usar 'isinstance'.
            for hab in habitaciones:
                self._registry.mostrar_datos(hab) # Dispatch polimorfico

        print("=======================================================\n")


    def persistir(self, registro: RegistroHotelero) -> str:
        """
        Guarda (serializa) un objeto RegistroHotelero en disco.

        Args:
            registro: La instancia de RegistroHotelero a guardar.

        Returns:
            El path del archivo guardado.

        Raises:
            PersistenciaException: Si ocurre un error de E/S.
        """
        propietario = registro.get_propietario()
        if not propietario:
            raise ValueError("El propietario no puede ser nulo para persistir.")

        nombre_archivo = f"{propietario}{EXTENSION_DATA}"
        path_completo = os.path.join(DIRECTORIO_DATA, nombre_archivo)

        try:
            # 1. Asegurar que el directorio 'data/' exista
            os.makedirs(DIRECTORIO_DATA, exist_ok=True)

            # 2. Escribir el archivo con Pickle (binario)
            with open(path_completo, "wb") as f:
                pickle.dump(registro, f)
            
            print(f"INFO: Registro de '{propietario}' persistido exitosamente en: {path_completo}")
            return path_completo

        except (IOError, pickle.PickleError) as e:
            # 3. Capturar y envolver el error en nuestra excepcion personalizada
            raise PersistenciaException(
                error_original=e,
                nombre_archivo=path_completo,
                tipo_operacion=TipoOperacionPersistencia.ESCRITURA
            )

    @staticmethod
    def leer_registro(propietario: str) -> RegistroHotelero:
        """
        Carga (deserializa) un objeto RegistroHotelero desde disco.
        Es estatico porque no necesita estado del servicio.

        Args:
            propietario: El nombre del propietario (es el nombre del archivo).

        Returns:
            La instancia de RegistroHotelero cargada.

        Raises:
            PersistenciaException: Si el archivo no existe o esta corrupto.
            ValueError: Si el nombre del propietario es nulo/vacio.
        """
        if not propietario:
            raise ValueError("El nombre del propietario no puede ser nulo o vacio.")

        nombre_archivo = f"{propietario}{EXTENSION_DATA}"
        path_completo = os.path.join(DIRECTORIO_DATA, nombre_archivo)

        try:
            # 1. Abrir y leer el archivo (binario)
            with open(path_completo, "rb") as f:
                registro_leido = pickle.load(f)
            
            if not isinstance(registro_leido, RegistroHotelero):
                 raise pickle.PickleError("El archivo no contiene un RegistroHotelero valido.")

            print(f"INFO: Registro de '{propietario}' cargado exitosamente desde: {path_completo}")
            return registro_leido

        except (FileNotFoundError, IOError, pickle.PickleError, EOFError) as e:
            # 2. Capturar y envolver cualquier error de lectura
            raise PersistenciaException(
                error_original=e,
                nombre_archivo=path_completo,
                tipo_operacion=TipoOperacionPersistencia.LECTURA
            )


################################################################################
# DIRECTORIO: servicios/negocio
################################################################################

# ==============================================================================
# ARCHIVO 61/65: __init__.py
# Directorio: servicios/negocio
# Ruta completa: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/servicios/negocio/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 62/65: hoteles_service.py
# Directorio: servicios/negocio
# Ruta completa: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/servicios/negocio/hoteles_service.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 63/65: paquete.py
# Directorio: servicios/negocio
# Ruta completa: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/servicios/negocio/paquete.py
# ==============================================================================

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


################################################################################
# DIRECTORIO: servicios/personal
################################################################################

# ==============================================================================
# ARCHIVO 64/65: __init__.py
# Directorio: servicios/personal
# Ruta completa: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/servicios/personal/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 65/65: empleado_service.py
# Directorio: servicios/personal
# Ruta completa: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/servicios/personal/empleado_service.py
# ==============================================================================

"""
Modulo del Servicio de Empleado.

Logica de negocio para gestionar un Empleado:
- Asignar certificaciones (ex AptoMedico)
- Ejecutar tareas (verificando certificacion)
"""

from datetime import date
from typing import TYPE_CHECKING

# Importacion de Entidades
from python_hotel.entidades.personal.empleado import Empleado
from python_hotel.entidades.personal.certificacion import Certificacion

if TYPE_CHECKING:
    from python_hotel.entidades.personal.equipo_limpieza import EquipoLimpieza


class EmpleadoService:
    """
    Servicio 'stateless' para operaciones de negocio sobre un Empleado.
    """

    def __init__(self):
        pass

    def asignar_certificacion(self,
                              empleado: Empleado,
                              es_valida: bool,
                              fecha_emision: date,
                              especializacion: str,
                              observaciones: str = "") -> None:
        """
        Metodo 'constructor' para crear y asignar una Certificacion a un empleado.
        """
        print(f"\nINFO: Asignando certificacion '{especializacion}' a {empleado.get_nombre()}...")
        
        cert = Certificacion(
            es_valida=es_valida,
            fecha_emision=fecha_emision,
            especializacion=especializacion,
            observaciones=observaciones
        )
        
        empleado.set_certificacion(cert)
        
        if not es_valida:
            print(f"ADVERTENCIA: La certificacion asignada no esta vigente.")

    def trabajar(self, 
                 empleado: Empleado, 
                 fecha: date, 
                 equipo: 'EquipoLimpieza') -> bool:
        """
        Ejecuta las tareas de un empleado para una fecha dada,
        siempre y cuando tenga una certificacion valida.

        (Adaptacion de US-016)

        Args:
            empleado: El empleado que va a trabajar.
            fecha: El dia de trabajo (solo ejecuta tareas de esa fecha).
            equipo: El equipo (ex Herramienta) que utilizara.

        Returns:
            True si pudo trabajar, False si no tenia certificacion.
        """
        print(f"\nINFO: {empleado.get_nombre()} intenta iniciar jornada laboral...")
        
        # 1. Validar Certificacion (ex AptoMedico)
        certificacion = empleado.get_certificacion()
        
        if not certificacion or not certificacion.esta_certificacion_valida():
            print(f"ERROR: {empleado.get_nombre()} no puede trabajar. "
                  f"Certificacion invalida o inexistente.")
            return False

        print(f"INFO: Certificacion '{certificacion.get_especializacion()}' validada.")

        # 2. Filtrar tareas por fecha y estado
        tareas_asignadas = empleado.get_tareas()
        tareas_para_hoy = [
            t for t in tareas_asignadas
            if t.get_fecha_programada() == fecha and t.get_estado() == "Pendiente"
        ]

        if not tareas_para_hoy:
            print(f"INFO: {empleado.get_nombre()} no tiene tareas pendientes para hoy ({fecha}).")
            return True # Pudo "trabajar" (no tenia nada que hacer)

        # 3. Ordenar tareas (por ID descendente, como en US-016)
        tareas_para_hoy.sort(key=lambda t: t.get_id_tarea(), reverse=True)

        # 4. Ejecutar tareas
        print(f"INFO: {empleado.get_nombre()} comienza sus tareas con equipo '{equipo.get_nombre()}':")
        for tarea in tareas_para_hoy:
            print(f"  -> Ejecutando Tarea {tarea.get_id_tarea()}: {tarea.get_descripcion()}...")
            tarea.set_estado("Completada")
        
        print(f"INFO: Jornada completada. {len(tareas_para_hoy)} tareas realizadas.")
        return True


################################################################################
# FIN DEL INTEGRADOR FINAL
# Total de archivos: 65
# Generado: 2025-11-04 18:03:54
################################################################################
