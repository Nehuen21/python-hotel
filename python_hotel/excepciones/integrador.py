"""
Archivo integrador generado automaticamente
Directorio: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/excepciones
Fecha: 2025-11-04 18:03:54
Total de archivos integrados: 6
"""

# ================================================================================
# ARCHIVO 1/6: __init__.py
# Ruta: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/excepciones/__init__.py
# ================================================================================

# no contiene nada pero le indica a python que eso es un paquete, todos los __init__ estan dentro de los directorios



# ================================================================================
# ARCHIVO 2/6: capacidad_insuficiente_exception.py
# Ruta: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/excepciones/capacidad_insuficiente_exception.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 3/6: hotel_exception.py
# Ruta: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/excepciones/hotel_exception.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 4/6: mensajes_exception.py
# Ruta: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/excepciones/mensajes_exception.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 5/6: persistencia_exception.py
# Ruta: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/excepciones/persistencia_exception.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 6/6: presupuesto_agotado_exception.py
# Ruta: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/excepciones/presupuesto_agotado_exception.py
# ================================================================================

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

