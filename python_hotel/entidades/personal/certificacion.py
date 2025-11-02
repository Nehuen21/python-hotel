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