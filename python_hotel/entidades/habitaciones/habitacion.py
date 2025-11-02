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