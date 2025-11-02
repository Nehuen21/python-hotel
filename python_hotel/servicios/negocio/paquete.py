"""
Modulo de la clase generica Paquete[T].

Utilizada para empaquetar resultados de operaciones de negocio
de forma tipo-segura. (Adaptacion de US-020).
"""

from typing import Generic, TypeVar, List

# Define el tipo generico 'T'
T = TypeVar('T')

class Paquete(Generic[T]):
    """
    Clase generica (tipo-segura) para almacenar colecciones de
    resultados (ej. listas de habitaciones post-checkout).
    """
    
    # Contador estatico para IDs unicos de paquete
    _contador_id: int = 0

    @staticmethod
    def _generar_siguiente_id() -> int:
        Paquete._contador_id += 1
        return Paquete._contador_id

    def __init__(self, tipo_contenido: str, contenido: List[T]):
        """
        Args:
            tipo_contenido: Un string descriptivo (ej. "HabitacionSimple").
            contenido: La lista de objetos (ej. [hab1, hab2, ...]).
        """
        self._id_paquete: int = self._generar_siguiente_id()
        self._tipo_contenido: str = tipo_contenido
        self._items: List[T] = contenido

    def get_items(self) -> List[T]:
        """Retorna una copia de los items."""
        return self._items.copy()

    def mostrar_contenido_paquete(self) -> None:
        """Imprime un resumen del paquete en consola."""
        print("\n--- Contenido del Paquete ---")
        print(f"ID Paquete: {self._id_paquete}")
        print(f"Tipo:       {self._tipo_contenido}")
        print(f"Cantidad:   {len(self._items)} unidades")
        print("-----------------------------")