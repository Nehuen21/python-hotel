"""
Modulo del Servicio de RegistroHotelero.

Logica de negocio para persistir (guardar) y recuperar (leer)
la entidad RegistroHotelero usando Pickle.
"""

import os
import pickle
from typing import TYPE_CHECKING

from python_hotel.entidades.hotel.registro_hotelero import RegistroHotelero
from python_hotel.constantes import DIRECTORIO_DATA, EXTENSION_DATA
from python_hotel.excepciones.persistencia_exception import (
    PersistenciaException,
    TipoOperacionPersistencia
)

# --- Dependencia del Paso 5 ---
# Importamos esto sabiendo que lo crearemos en el siguiente paso.
from python_hotel.servicios.habitaciones.habitacion_service_registry import HabitacionServiceRegistry
# -----------------------------

if TYPE_CHECKING:
    from python_hotel.entidades.habitaciones.habitacion import Habitacion


class RegistroHoteleroService:
    """
    Servicio 'stateless' para operaciones de persistencia (Pickle)
    y visualizacion del RegistroHotelero.
    """

    def __init__(self):
        """
        Inicializa el servicio. Obtenemos la instancia del Registry
        que usaremos en 'mostrar_datos'.
        """
        # Obtenemos la instancia unica del Singleton
        self._registry = HabitacionServiceRegistry.get_instance()

    def mostrar_datos(self, registro: RegistroHotelero) -> None:
        """
        Muestra en consola un resumen completo del registro,
        incluyendo los detalles de cada habitacion.
        """
        if not registro:
            print("ERROR: Registro no proporcionado.")
            return

        ala = registro.get_ala_hotel()
        hotel = registro.get_hotel()
        habitaciones = ala.get_habitaciones()

        print("\n=======================================================")
        print("          REGISTRO HOTELERO - DETALLE COMPLETO")
        print("=======================================================")
        print(f"Propietario:   {registro.get_propietario()}")
        print(f"Hotel ID:      {registro.get_id_hotel()}")
        print(f"Avaluo Fiscal: ${registro.get_avaluo():,.2f}")
        print("-------------------------------------------------------")
        print("--- Datos del Hotel ---")
        print(f"Direccion:     {hotel.get_direccion()}")
        print(f"Capacidad Max: {hotel.get_capacidad()} personas")
        print("--- Datos del Ala ---")
        print(f"Nombre:        {ala.get_nombre()}")
        print(f"Presupuesto:   ${ala.get_presupuesto_disponible():,.2f}")
        print(f"Cap. Ocupada:  {ala.get_capacidad_ocupada()} personas")
        print(f"Habitaciones:  {len(habitaciones)} unidades")
        print("-------------------------------------------------------")
        print("--- Listado de Habitaciones Configradas ---")
        
        if not habitaciones:
            print("(No hay habitaciones configuradas)")
        else:
            # --- Patron Registry en accion ---
            # Usamos el registry para llamar al 'mostrar_datos'
            # especifico de cada tipo de habitacion, sin usar 'isinstance'.
            for hab in habitaciones:
                self._registry.mostrar_datos(hab) # Dispatch polimorfico

        print("=======================================================\n")


    def persistir(self, registro: RegistroHotelero) -> str:
        """
        Guarda (serializa) un objeto RegistroHotelero en disco.

        Args:
            registro: La instancia de RegistroHotelero a guardar.

        Returns:
            El path del archivo guardado.

        Raises:
            PersistenciaException: Si ocurre un error de E/S.
        """
        propietario = registro.get_propietario()
        if not propietario:
            raise ValueError("El propietario no puede ser nulo para persistir.")

        nombre_archivo = f"{propietario}{EXTENSION_DATA}"
        path_completo = os.path.join(DIRECTORIO_DATA, nombre_archivo)

        try:
            # 1. Asegurar que el directorio 'data/' exista
            os.makedirs(DIRECTORIO_DATA, exist_ok=True)

            # 2. Escribir el archivo con Pickle (binario)
            with open(path_completo, "wb") as f:
                pickle.dump(registro, f)
            
            print(f"INFO: Registro de '{propietario}' persistido exitosamente en: {path_completo}")
            return path_completo

        except (IOError, pickle.PickleError) as e:
            # 3. Capturar y envolver el error en nuestra excepcion personalizada
            raise PersistenciaException(
                error_original=e,
                nombre_archivo=path_completo,
                tipo_operacion=TipoOperacionPersistencia.ESCRITURA
            )

    @staticmethod
    def leer_registro(propietario: str) -> RegistroHotelero:
        """
        Carga (deserializa) un objeto RegistroHotelero desde disco.
        Es estatico porque no necesita estado del servicio.

        Args:
            propietario: El nombre del propietario (es el nombre del archivo).

        Returns:
            La instancia de RegistroHotelero cargada.

        Raises:
            PersistenciaException: Si el archivo no existe o esta corrupto.
            ValueError: Si el nombre del propietario es nulo/vacio.
        """
        if not propietario:
            raise ValueError("El nombre del propietario no puede ser nulo o vacio.")

        nombre_archivo = f"{propietario}{EXTENSION_DATA}"
        path_completo = os.path.join(DIRECTORIO_DATA, nombre_archivo)

        try:
            # 1. Abrir y leer el archivo (binario)
            with open(path_completo, "rb") as f:
                registro_leido = pickle.load(f)
            
            if not isinstance(registro_leido, RegistroHotelero):
                 raise pickle.PickleError("El archivo no contiene un RegistroHotelero valido.")

            print(f"INFO: Registro de '{propietario}' cargado exitosamente desde: {path_completo}")
            return registro_leido

        except (FileNotFoundError, IOError, pickle.PickleError, EOFError) as e:
            # 2. Capturar y envolver cualquier error de lectura
            raise PersistenciaException(
                error_original=e,
                nombre_archivo=path_completo,
                tipo_operacion=TipoOperacionPersistencia.LECTURA
            )