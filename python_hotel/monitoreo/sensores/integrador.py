"""
Archivo integrador generado automaticamente
Directorio: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/monitoreo/sensores
Fecha: 2025-11-04 18:03:54
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/monitoreo/sensores/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: limpieza_reader_task.py
# Ruta: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/monitoreo/sensores/limpieza_reader_task.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 3/3: ocupacion_reader_task.py
# Ruta: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/monitoreo/sensores/ocupacion_reader_task.py
# ================================================================================

"""
Modulo del Sensor de Ocupacion (Observable).

Implementa un hilo que simula la lectura de un sensor de ocupacion
y notifica a los observadores (Observer).
"""

import threading
import time
import random
from typing import TYPE_CHECKING

# Importacion de la clase base Observable
from python_hotel.patrones.observer.observable import Observable
from python_hotel.constantes import (
    INTERVALO_SENSOR_OCUPACION,
    SENSOR_OCUPACION_MIN,
    SENSOR_OCUPACION_MAX
)

if TYPE_CHECKING:
    from python_hotel.patrones.observer.observer import Observer


class OcupacionReaderTask(threading.Thread, Observable[float]):
    """
    Sensor (Observable) que lee la ocupacion.

    Hereda de 'threading.Thread' para correr en un hilo separado.
    Hereda de 'Observable[float]' para poder notificar a observadores
    cuando lee un nuevo valor (float).
    """

    def __init__(self):
        """
        Inicializa el hilo y la clase Observable.
        """
        threading.Thread.__init__(self, daemon=True) # daemon=True para que finalice con el main
        Observable.__init__(self)
        
        # Evento para detener el hilo de forma segura (graceful shutdown)
        self._detenido = threading.Event()
        self._nombre_sensor = "Ocupacion"

    def _leer_ocupacion_simulada(self) -> float:
        """Metodo privado que simula la lectura de un sensor real."""
        # Simula que la ocupacion tiende a ser baja (para que la limpieza se active)
        ocupacion = random.uniform(SENSOR_OCUPACION_MIN, SENSOR_OCUPACION_MAX * 0.3) 
        return round(ocupacion, 2)

    def run(self) -> None:
        """
        Metodo principal del hilo (se ejecuta con .start()).

        Mientras no se detenga, lee el sensor y notifica a los observadores.
        """
        print(f"INFO (Sensor): Hilo del sensor '{self._nombre_sensor}' iniciado.")
        
        while not self._detenido.is_set():
            try:
                # 1. Leer el valor simulado
                valor_leido = self._leer_ocupacion_simulada()
                
                # 2. Notificar a los observadores (Patron Observer)
                self.notificar_observadores(valor_leido)
                
                # 3. Esperar el intervalo
                time.sleep(INTERVALO_SENSOR_OCUPACION)
                
            except Exception as e:
                print(f"ERROR (Sensor {self._nombre_sensor}): {e}")
                
        print(f"INFO (Sensor): Hilo del sensor '{self._nombre_sensor}' detenido.")

    def detener(self) -> None:
        """Senala al evento para detener el bucle 'run'."""
        self._detenido.set()

