"""
Modulo del Sensor de Nivel de Limpieza (Observable).

Implementa un hilo que simula la lectura de un sensor de limpieza
y notifica a los observadores (Observer).
"""

import threading
import time
import random
from typing import TYPE_CHECKING

from python_hotel.patrones.observer.observable import Observable
from python_hotel.constantes import (
    INTERVALO_SENSOR_LIMPIEZA,
    SENSOR_LIMPIEZA_MIN,
    SENSOR_LIMPIEZA_MAX
)

if TYPE_CHECKING:
    from python_hotel.patrones.observer.observer import Observer


class LimpiezaReaderTask(threading.Thread, Observable[float]):
    """
    Sensor (Observable) que lee el nivel de limpieza.
    """

    def __init__(self):
        threading.Thread.__init__(self, daemon=True)
        Observable.__init__(self)
        self._detenido = threading.Event()
        self._nombre_sensor = "Limpieza"

    def _leer_limpieza_simulada(self) -> float:
        """Metodo privado que simula la lectura de un sensor real."""
        # Simula que el nivel de limpieza tiende a bajar (para que la limpieza se active)
        limpieza = random.uniform(SENSOR_LIMPIEZA_MIN, SENSOR_LIMPIEZA_MAX * 0.8)
        return round(limpieza, 2)

    def run(self) -> None:
        """
        Metodo principal del hilo (se ejecuta con .start()).
        """
        print(f"INFO (Sensor): Hilo del sensor '{self._nombre_sensor}' iniciado.")
        
        while not self._detenido.is_set():
            try:
                valor_leido = self._leer_limpieza_simulada()
                self.notificar_observadores(valor_leido)
                time.sleep(INTERVALO_SENSOR_LIMPIEZA)
                
            except Exception as e:
                print(f"ERROR (Sensor {self._nombre_sensor}): {e}")
                
        print(f"INFO (Sensor): Hilo del sensor '{self._nombre_sensor}' detenido.")

    def detener(self) -> None:
        """Senala al evento para detener el bucle 'run'."""
        self._detenido.set()