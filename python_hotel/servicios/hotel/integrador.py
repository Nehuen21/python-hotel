"""
Archivo integrador generado automaticamente
Directorio: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/servicios/hotel
Fecha: 2025-11-04 18:03:54
Total de archivos integrados: 4
"""

# ================================================================================
# ARCHIVO 1/4: __init__.py
# Ruta: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/servicios/hotel/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/4: ala_hotel_service.py
# Ruta: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/servicios/hotel/ala_hotel_service.py
# ================================================================================

"""
Modulo del Servicio de AlaHotel.

Logica de negocio para gestionar un AlaHotel:
- Configurar habitaciones (usando Factory)
- Limpiar habitaciones (usando Registry y Strategy)
- Gestionar presupuesto y capacidad (usando Excepciones)
"""

from typing import TYPE_CHECKING, Type
from python_hotel.entidades.hotel.ala_hotel import AlaHotel
from python_hotel.entidades.habitaciones.habitacion import Habitacion

# --- Dependencia del Factory (Paso 4) ---
from python_hotel.patrones.factory.habitacion_factory import HabitacionFactory

# --- Dependencia del Registry (Paso 5) ---
from python_hotel.servicios.habitaciones.habitacion_service_registry import HabitacionServiceRegistry

# --- Dependencia de Excepciones (Paso 1) ---
from python_hotel.excepciones.capacidad_insuficiente_exception import CapacidadInsuficienteException
from python_hotel.excepciones.presupuesto_agotado_exception import PresupuestoAgotadoException

# --- Dependencia de Constantes (Paso 1) ---
from python_hotel.constantes import COSTE_LIMPIEZA_ALA, ESTADO_INICIAL_HABITACION

if TYPE_CHECKING:
    from python_hotel.entidades.personal.empleado import Empleado


class AlaHotelService:
    """
    Servicio 'stateless' para operaciones de negocio sobre un AlaHotel.
    Este servicio orquesta los patrones Factory y Registry.
    """

    def __init__(self):
        """
        Inicializa el servicio. Obtenemos la instancia del Registry
        que usaremos para 'limpiar'.
        """
        # Obtenemos la instancia unica del Singleton/Registry
        self._registry = HabitacionServiceRegistry.get_instance()
        # Mantenemos una referencia estatica al Factory
        self._factory = HabitacionFactory

    def configurar_habitaciones(self, 
                                ala_hotel: AlaHotel, 
                                tipo_habitacion: str, 
                                cantidad: int) -> list[Habitacion]:
        """
        Configura (crea y agrega) nuevas habitaciones en un ala.
        Utiliza el Factory Method para la creacion.

        Args:
            ala_hotel: La instancia del ala a modificar.
            tipo_habitacion: El string del tipo (ej. "Simple", "Suite").
            cantidad: Cuantas habitaciones de ese tipo crear.

        Returns:
            La lista de habitaciones recien creadas.
            
        Raises:
            CapacidadInsuficienteException: Si no hay capacidad para
                                            tantas habitaciones.
            ValueError: Si el tipo de habitacion es invalido (desde el Factory).
        """
        print(f"\nINFO: Solicitud para configurar {cantidad} habitacion(es) tipo '{tipo_habitacion}' en '{ala_hotel.get_nombre()}'...")
        
        # 1. Usar el Factory para crear UNA habitacion temporal y medir su capacidad
        #    Esto evita hardcodear la capacidad de cada tipo aqui.
        try:
            temp_hab = self._factory.crear_habitacion(tipo_habitacion)
            capacidad_requerida_total = temp_hab.get_capacidad() * cantidad
        except ValueError as e:
            print(f"ERROR (Servicio): {e}")
            raise # Re-lanzar el error del factory

        # 2. Validar capacidad (Logica de negocio)
        capacidad_disponible = ala_hotel.get_capacidad_disponible()
        
        if capacidad_requerida_total > capacidad_disponible:
            print(f"ERROR: Capacidad insuficiente. Requeridas: {capacidad_requerida_total}, "
                  f"Disponibles: {capacidad_disponible}")
            raise CapacidadInsuficienteException(
                capacidad_disponible=capacidad_disponible,
                capacidad_requerida=capacidad_requerida_total
            )

        # 3. Si hay capacidad, crear el resto de habitaciones
        #    (Re-usamos la primera que ya creamos)
        habitaciones_creadas = [temp_hab]
        for _ in range(cantidad - 1):
            habitaciones_creadas.append(self._factory.crear_habitacion(tipo_habitacion))

        # 4. Agregar las habitaciones al Ala
        for hab in habitaciones_creadas:
            ala_hotel.add_habitacion(hab)
            
        print(f"INFO: Exito. {cantidad} habitaciones agregadas. "
              f"Capacidad restante: {ala_hotel.get_capacidad_disponible()}")
        
        return habitaciones_creadas

    def limpiar(self, ala_hotel: AlaHotel) -> tuple[int, float]:
        """
        Limpia TODAS las habitaciones del ala.
        Utiliza el Registry para el dispatch polimorfico del mantenimiento.
        Utiliza el Strategy (automaticamente) para calcular tiempos.

        Args:
            ala_hotel: El ala a limpiar.

        Returns:
            Una tupla (tiempo_total_minutos, coste_total).

        Raises:
            PresupuestoAgotadoException: Si no hay presupuesto para la limpieza.
        """
        print(f"\nINFO: Iniciando ciclo de limpieza para '{ala_hotel.get_nombre()}'...")
        
        # 1. Validar presupuesto (Logica de negocio)
        presupuesto_actual = ala_hotel.get_presupuesto_disponible()
        
        if presupuesto_actual < COSTE_LIMPIEZA_ALA:
            print(f"ERROR: Presupuesto agotado. Requerido: {COSTE_LIMPIEZA_ALA}, "
                  f"Disponible: {presupuesto_actual}")
            raise PresupuestoAgotadoException(
                presupuesto_disponible=presupuesto_actual,
                coste_requerido=COSTE_LIMPIEZA_ALA
            )
            
        # 2. Cobrar el coste de limpieza
        ala_hotel.set_presupuesto_disponible(presupuesto_actual - COSTE_LIMPIEZA_ALA)
        print(f"INFO: Coste de ${COSTE_LIMPIEZA_ALA} debitado. "
              f"Presupuesto restante: ${ala_hotel.get_presupuesto_disponible():.2f}")

        # 3. Simular ocupacion actual (para la estrategia Estandar)
        #    En un sistema real, esto vendria de los sensores.
        ocupacion_simulada = 50.0 # Simulamos alta ocupacion (limpieza rapida)

        # 4. Iterar y limpiar (Dispatch con Registry)
        tiempo_total_mantenimiento = 0
        habitaciones_a_limpiar = ala_hotel.get_habitaciones()
        
        if not habitaciones_a_limpiar:
            print("INFO: No hay habitaciones configuradas para limpiar.")
            return 0, COSTE_LIMPIEZA_ALA

        for hab in habitaciones_a_limpiar:
            # --- Patron Registry + Strategy en accion ---
            # Llamamos al Registry, que llama al Servicio especifico,
            # que a su vez delega en la Estrategia inyectada.
            tiempo_hab = self._registry.realizar_mantenimiento(hab, ocupacion_simulada)
            tiempo_total_mantenimiento += tiempo_hab
            
            # Post-limpieza: marcar como disponible
            hab.set_estado(ESTADO_INICIAL_HABITACION)

        print(f"INFO: Ciclo de limpieza completado. "
              f"Tiempo total: {tiempo_total_mantenimiento} minutos.")
        
        return tiempo_total_mantenimiento, COSTE_LIMPIEZA_ALA

    def desinfectar(self, ala_hotel: AlaHotel, tipo_desinfectante: str) -> None:
        """
        Aplica una desinfeccion a toda el ala.
        (Operacion simple de negocio).
        """
        print(f"\nINFO: Desinfectando '{ala_hotel.get_nombre()}' "
              f"con '{tipo_desinfectante}'...")
        # En un sistema real, esto podria afectar el presupuesto
        # o el estado de las habitaciones.
        print("INFO: Desinfeccion completada.")

    def asignar_empleados(self, ala_hotel: AlaHotel, empleados: list['Empleado']) -> None:
        """
        Asigna una lista de empleados al ala.
        """
        ala_hotel.set_empleados(empleados)
        print(f"\nINFO: {len(empleados)} empleados asignados a '{ala_hotel.get_nombre()}'.")

    def realizar_checkout_por_tipo(self, ala_hotel: AlaHotel, tipo_habitacion: Type[Habitacion]) -> int:
        """
        Procesa el check-out de todas las habitaciones de un tipo especifico.
        
        Args:
            ala_hotel: El ala donde buscar.
            tipo_habitacion: La *clase* de la habitacion (ej. HabitacionSimple).

        Returns:
            El numero de habitaciones procesadas.
        """
        count = 0
        for hab in ala_hotel.get_habitaciones():
            if isinstance(hab, tipo_habitacion):
                hab.set_estado(ESTADO_INICIAL_HABITACION)
                count += 1
        
        print(f"\nINFO: Check-out procesado para {count} habitaciones "
              f"tipo '{tipo_habitacion.__name__}'.")
        return count

# ================================================================================
# ARCHIVO 3/4: hotel_service.py
# Ruta: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/servicios/hotel/hotel_service.py
# ================================================================================

"""
Modulo del Servicio de Hotel.

Logica de negocio de alto nivel para la creacion y gestion de la
entidad Hotel.
"""

from python_hotel.entidades.hotel.hotel import Hotel
from python_hotel.entidades.hotel.ala_hotel import AlaHotel

class HotelService:
    """
    Servicio 'stateless' para operaciones relacionadas con la entidad Hotel.
    """

    def __init__(self):
        """
        Inicializa el servicio. En este caso, no tiene estado.
        """
        pass

    def crear_hotel_con_ala(self,
                             id_hotel: int,
                             capacidad: int,
                             direccion: str,
                             nombre_ala: str) -> Hotel:
        """
        Metodo de conveniencia (Fachada) para crear un Hotel y
        su Ala principal de una sola vez.

        Args:
            id_hotel: ID unico del hotel.
            capacidad: Capacidad total (en personas) del hotel.
            direccion: Direccion fisica.
            nombre_ala: Nombre del ala principal (ej. "Ala Norte").

        Returns:
            La instancia del Hotel, ya vinculada a su Ala.
        """
        
        # 1. Crear el Hotel
        try:
            hotel = Hotel(
                id_hotel=id_hotel,
                capacidad=capacidad,
                direccion=direccion
            )
            
            # 2. Crear el Ala
            # El ala hereda la capacidad maxima del hotel
            ala = AlaHotel(
                nombre=nombre_ala,
                capacidad=capacidad 
            )
            
            # 3. Vincularlos
            hotel.set_ala(ala)
            
            print(f"INFO: Hotel '{id_hotel}' y Ala '{nombre_ala}' creados exitosamente.")
            return hotel
            
        except ValueError as e:
            print(f"ERROR al crear hotel: {e}")
            raise  # Re-lanzamos la excepcion para que el main.py la maneje

# ================================================================================
# ARCHIVO 4/4: registro_hotelero_service.py
# Ruta: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/servicios/hotel/registro_hotelero_service.py
# ================================================================================

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

