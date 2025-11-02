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