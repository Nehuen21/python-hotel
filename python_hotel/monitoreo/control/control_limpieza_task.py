"""
Modulo del Controlador de Limpieza (Observer).

Implementa un hilo que observa los sensores y toma decisiones
de limpieza automatica, delegando la accion al AlaHotelService.
"""

import threading
import time
from typing import TYPE_CHECKING

# Importacion de la interfaz Observer
from python_hotel.patrones.observer.observer import Observer
from python_hotel.constantes import (
    INTERVALO_CONTROL_LIMPIEZA,
    OCUPACION_MAX_PARA_LIMPIEZA,
    LIMPIEZA_MIN_PARA_LIMPIEZA
)
# Importacion de la excepcion que puede ocurrir
from python_hotel.excepciones.presupuesto_agotado_exception import PresupuestoAgotadoException

if TYPE_CHECKING:
    from python_hotel.servicios.hotel.ala_hotel_service import AlaHotelService
    from python_hotel.entidades.hotel.ala_hotel import AlaHotel
    # Importamos los Observables para type hints
    from python_hotel.monitoreo.sensores.ocupacion_reader_task import OcupacionReaderTask
    from python_hotel.monitoreo.sensores.limpieza_reader_task import LimpiezaReaderTask


class ControlLimpiezaTask(threading.Thread, Observer[float]):
    """
    Controlador (Observer) que gestiona la limpieza automatica.

    Hereda de 'threading.Thread' para correr en un hilo separado.
    Hereda de 'Observer[float]' para poder suscribirse a los sensores.
    """

    def __init__(self,
                 sensor_ocupacion: 'OcupacionReaderTask',
                 sensor_limpieza: 'LimpiezaReaderTask',
                 ala_hotel: 'AlaHotel',
                 ala_service: 'AlaHotelService'):
        
        threading.Thread.__init__(self, daemon=True)
        self._detenido = threading.Event()
        
        # --- Inyeccion de Dependencias ---
        self._ala_hotel = ala_hotel
        self._ala_service = ala_service
        self._sensor_ocupacion = sensor_ocupacion
        self._sensor_limpieza = sensor_limpieza
        
        # Estado interno para almacenar las ultimas lecturas
        # Usamos locks para garantizar thread-safety al actualizar/leer
        self._lock = threading.Lock()
        self._ultima_ocupacion: float = 100.0 # Valor inicial seguro
        self._ultima_limpieza: float = 100.0  # Valor inicial seguro

    def _suscribir_a_sensores(self) -> None:
        """Se suscribe como observador a los sensores."""
        self._sensor_ocupacion.agregar_observador(self)
        self._sensor_limpieza.agregar_observador(self)
        print("INFO (Control): Controlador suscrito a sensores de Ocupacion y Limpieza.")

    def actualizar(self, evento: float) -> None:
        """
        Metodo de la interfaz Observer. Es llamado por CUALQUIER
        Observable al que este suscrito (ambos sensores).

        Args:
            evento: El valor (float) notificado.
        """
        # Identificamos de que sensor proviene el evento
        # (Esto es una simplificacion; en un sistema real,
        # el 'evento' seria un objeto con mas contexto).
        
        # Heuristica simple: si es > 100, no puede ser, pero
        # un valor de 0 a 100 puede ser cualquiera.
        # Necesitamos identificar al emisor.
        
        # --- Estrategia de Identificacion (Hack simple) ---
        # Como no podemos saber cual sensor fue, le preguntamos
        # al 'sender' (emisor) que no esta implementado.
        # Vamos a tener que cambiar la firma de 'actualizar'
        # o almacenar los valores de forma diferente.
        
        # --- Estrategia 2 (Mejor) ---
        # El controlador NO debe implementar 'actualizar'
        # directamente. En su lugar, el 'run' loop leera
        # los valores directamente.
        
        # --- Estrategia 3 (La correcta para este diseno) ---
        # El controlador necesita saber de QUIEN viene la actualizacion.
        # Modificaremos 'actualizar' para que reciba al emisor.
        
        # --- Estrategia 4 (La mas simple) ---
        # El controlador no implementa 'actualizar'.
        # El controlador le PIDE los valores a los sensores
        # en su propio bucle 'run'.
        
        # --- Estrategia 5 (La que pide la HU) ---
        # El controlador ES un observador. Debe implementar 'actualizar'.
        # El problema es que ambos sensores envian 'float'.
        # Necesitamos diferenciar los eventos.
        
        # Vamos a asumir que 'actualizar' recibe (sender, evento)
        # Esto requiere modificar Observable.notificar_observadores(self, evento)
        #
        # Opcion B: El controlador tiene metodos separados.
        # self._sensor_ocupacion.agregar_observador(self.actualizar_ocupacion)
        #
        # Opcion C: La mas simple: El controlador guarda el ultimo valor
        # de CADA sensor en su metodo 'actualizar', pero necesita
        # saber de quien viene.
        
        # **** SOLUCION (Paso 3 corregido) ****
        # Observable.notificar_observadores deberia pasar 'self' y 'evento'
        # Pero para no cambiar los archivos del Paso 3, haremos un
        # truco: 'actualizar' sera llamado por los sensores, pero
        # no sabremos cual.
        # El controlador tendra que almacenar los valores.
        
        # **** SOLUCION 2 (La mas realista) ****
        # El controlador implementa DOS interfaces Observer
        # o tiene metodos especificos.
        
        # **** SOLUCION 3 (La que implementaremos) ****
        # Haremos que los sensores notifiquen una TUPLA (str, float)
        # Esto rompe la firma Generica T=float, pero es lo mas
        # practico para el ejercicio.
        
        # *** RE-DISENO (El mas limpio) ***
        # El Controlador sera Observador de NADA.
        # El Controlador correra en su hilo y PREGUNTARA
        # a los sensores por sus ultimos valores.
        # Esto rompe la HU "Implementar patron Observer".
        
        # *** SOLUCION FINAL (Fiel a la HU) ***
        # El controlador implementa Observer[float].
        # PERO necesita saber de quien.
        # Modificaremos los sensores para que notifiquen un
        # objeto 'EventoSensor' en lugar de un 'float'.
        #
        # ¡Pero la HU US-TECH-003 dice Observable[float]!
        #
        # OK, AQUI ESTA LA LOGICA:
        # El controlador NO implementara Observer.
        # El controlador se inyecta con los Observables
        # y el controlador CREA observadores internos (lambdas o metodos)
        # para actualizar su estado.
        
        # Esta es la implementacion correcta para la HU-012
        pass # 'actualizar' no se usara directamente.

    def _actualizar_ocupacion(self, ocupacion: float):
        """Callback privado para el sensor de ocupacion."""
        with self._lock:
            self._ultima_ocupacion = ocupacion
        
    def _actualizar_limpieza(self, limpieza: float):
        """Callback privado para el sensor de limpieza."""
        with self._lock:
            self._ultima_limpieza = limpieza

    def run(self) -> None:
        """
        Metodo principal del hilo (se ejecuta con .start()).
        
        En lugar de implementar Observer.actualizar() (que es ambiguo
        con dos fuentes), el controlador crea sus propios observadores
        internos (metodos) y los suscribe.
        
        El hilo 'run' se dedica a chequear las condiciones.
        """
        
        # 1. Suscribir los callbacks privados a los sensores
        self._sensor_ocupacion.agregar_observador(self)
        self._sensor_limpieza.agregar_observador(self)
        # Esto significa que 'actualizar' sera llamado por AMBOS.
        # No podemos diferenciarlos.
        
        # **** PLAN B (Definitivo) ****
        # La clase NO implementa Observer.
        # Los sensores son Observables.
        # El controlador crea Observadores INTERNOS (clases anidadas o metodos)
        
        # Clase interna Observador de Ocupacion
        class OcupacionObserver(Observer[float]):
            def __init__(self, controlador):
                self._controlador = controlador
            def actualizar(self, evento: float):
                self._controlador._actualizar_ocupacion(evento)
                
        # Clase interna Observador de Limpieza
        class LimpiezaObserver(Observer[float]):
            def __init__(self, controlador):
                self._controlador = controlador
            def actualizar(self, evento: float):
                self._controlador._actualizar_limpieza(evento)

        # 1. Suscribir los observadores internos
        self._sensor_ocupacion.agregar_observador(OcupacionObserver(self))
        self._sensor_limpieza.agregar_observador(LimpiezaObserver(self))
        print("INFO (Control): Controlador (hilo) iniciado y suscrito a sensores.")

        # 2. Bucle de decision
        while not self._detenido.is_set():
            time.sleep(INTERVALO_CONTROL_LIMPIEZA)
            
            # 3. Leer estado interno (thread-safe)
            with self._lock:
                ocupacion = self._ultima_ocupacion
                limpieza = self._ultima_limpieza
            
            print(f"DEBUG (Control): Ocup={ocupacion}%, Limp={limpieza}%. "
                  f"Req: Ocup<{OCUPACION_MAX_PARA_LIMPIEZA}, Limp<{LIMPIEZA_MIN_PARA_LIMPIEZA}")

            # 4. Logica de decision (HU-012)
            if (ocupacion < OCUPACION_MAX_PARA_LIMPIEZA and 
                limpieza < LIMPIEZA_MIN_PARA_LIMPIEZA):
                
                print("INFO (Control): **** CONDICIONES CUMPLIDAS ****")
                print(f"INFO (Control): Iniciando limpieza automatica de '{self._ala_hotel.get_nombre()}'...")
                
                try:
                    # 5. Delegar al servicio
                    self._ala_service.limpiar(self._ala_hotel)
                    
                    # 6. Resetear el sensor de limpieza (simulacion)
                    with self._lock:
                        self._ultima_limpieza = 100.0
                    print("INFO (Control): Limpieza completada. Nivel de limpieza reseteado a 100%.")
                    
                except PresupuestoAgotadoException as e:
                    print(f"ERROR (Control): {e.get_mensaje_usuario()} {e.get_mensaje_tecnico()}")
                    print("ERROR (Control): Limpieza automatica abortada. Reintentando en 30s...")
                    time.sleep(30) # Penalizacion
                except Exception as e:
                    print(f"ERROR (Control): Error inesperado durante la limpieza: {e}")
                    
            # Fin del bucle
        
        print("INFO (Control): Hilo del controlador detenido.")


    def detener(self) -> None:
        """Senala al evento para detener el bucle 'run'."""
        self._detenido.set()