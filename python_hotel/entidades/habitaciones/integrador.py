"""
Archivo integrador generado automaticamente
Directorio: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/entidades/habitaciones
Fecha: 2025-11-04 18:03:54
Total de archivos integrados: 8
"""

# ================================================================================
# ARCHIVO 1/8: __init__.py
# Ruta: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/entidades/habitaciones/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/8: habitacion.py
# Ruta: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/entidades/habitaciones/habitacion.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 3/8: habitacion_base.py
# Ruta: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/entidades/habitaciones/habitacion_base.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 4/8: habitacion_doble.py
# Ruta: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/entidades/habitaciones/habitacion_doble.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 5/8: habitacion_premium.py
# Ruta: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/entidades/habitaciones/habitacion_premium.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 6/8: habitacion_simple.py
# Ruta: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/entidades/habitaciones/habitacion_simple.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 7/8: suite.py
# Ruta: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/entidades/habitaciones/suite.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 8/8: suite_presidencial.py
# Ruta: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/entidades/habitaciones/suite_presidencial.py
# ================================================================================

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

