"""
Modulo de la Entidad: EquipoLimpieza.

Representa el equipamiento fisico utilizado para tareas de limpieza
o mantenimiento. Reemplaza a 'Herramienta'.
"""

class EquipoLimpieza:
    """
    Entidad que representa una herramienta o equipo (ej. aspiradora, carro).
    """

    def __init__(self, id_equipo: int, nombre: str, certificado_higiene: bool):
        """
        Inicializa el equipo.

        Args:
            id_equipo: ID unico del equipo.
            nombre: Nombre del equipo (ej. "Aspiradora Industrial V-100").
            certificado_higiene: True si cumple con normas H&S.
        """
        if id_equipo <= 0:
            raise ValueError("El ID del equipo debe ser positivo.")
        if not nombre:
            raise ValueError("El nombre no puede ser nulo o vacio.")

        self._id_equipo: int = id_equipo
        self._nombre: str = nombre
        self._certificado_higiene: bool = certificado_higiene

    # --- Getters ---

    def get_id_equipo(self) -> int:
        return self._id_equipo

    def get_nombre(self) -> str:
        return self._nombre

    def tiene_certificado_higiene(self) -> bool:
        return self._certificado_higiene

    def __str__(self) -> str:
        return f"Equipo: {self._nombre} (ID: {self._id_equipo})"