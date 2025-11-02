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