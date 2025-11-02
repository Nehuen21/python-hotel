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