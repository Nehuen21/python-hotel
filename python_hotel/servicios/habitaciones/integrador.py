"""
Archivo integrador generado automaticamente
Directorio: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/servicios/habitaciones
Fecha: 2025-11-04 18:03:54
Total de archivos integrados: 8
"""

# ================================================================================
# ARCHIVO 1/8: __init__.py
# Ruta: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/servicios/habitaciones/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/8: habitacion_base_service.py
# Ruta: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/servicios/habitaciones/habitacion_base_service.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 3/8: habitacion_doble_service.py
# Ruta: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/servicios/habitaciones/habitacion_doble_service.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 4/8: habitacion_service.py
# Ruta: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/servicios/habitaciones/habitacion_service.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 5/8: habitacion_service_registry.py
# Ruta: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/servicios/habitaciones/habitacion_service_registry.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 6/8: habitacion_simple_service.py
# Ruta: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/servicios/habitaciones/habitacion_simple_service.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 7/8: suite_presidencial_service.py
# Ruta: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/servicios/habitaciones/suite_presidencial_service.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 8/8: suite_service.py
# Ruta: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/servicios/habitaciones/suite_service.py
# ================================================================================

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

