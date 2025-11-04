"""
Archivo integrador generado automaticamente
Directorio: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/patrones/observer
Fecha: 2025-11-04 18:03:54
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/patrones/observer/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: observable.py
# Ruta: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/patrones/observer/observable.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 3/3: observer.py
# Ruta: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/patrones/observer/observer.py
# ================================================================================

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

