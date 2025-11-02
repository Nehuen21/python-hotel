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