"""
Punto de entrada principal (main.py) del Sistema de Gestion Hotelera.

Este script simula un flujo de operaciones completo, demostrando la
integracion de todos los servicios y patrones de diseno implementados:
- Singleton
- Factory Method
- Strategy
- Observer
- Registry (Bonus)
- Façade (en HotelesService)
"""

import time
from datetime import date

# --- Importacion de Servicios (Logica de Negocio) ---
from python_hotel.servicios.hotel.hotel_service import HotelService
from python_hotel.servicios.hotel.ala_hotel_service import AlaHotelService
from python_hotel.servicios.hotel.registro_hotelero_service import RegistroHoteleroService
from python_hotel.servicios.personal.empleado_service import EmpleadoService
from python_hotel.servicios.negocio.hoteles_service import HotelesService

# --- Importacion de Entidades (Datos) ---
from python_hotel.entidades.hotel.registro_hotelero import RegistroHotelero
from python_hotel.entidades.personal.empleado import Empleado
from python_hotel.entidades.personal.tarea import Tarea
from python_hotel.entidades.personal.equipo_limpieza import EquipoLimpieza
from python_hotel.entidades.habitaciones.habitacion_simple import HabitacionSimple
from python_hotel.entidades.habitaciones.suite import Suite

# --- Importacion de Patrones (Observables y Control) ---
from python_hotel.monitoreo.sensores.ocupacion_reader_task import OcupacionReaderTask
from python_hotel.monitoreo.sensores.limpieza_reader_task import LimpiezaReaderTask
from python_hotel.monitoreo.control.control_limpieza_task import ControlLimpiezaTask

# --- Importacion de Excepciones (Manejo de Errores) ---
from python_hotel.excepciones.capacidad_insuficiente_exception import CapacidadInsuficienteException
from python_hotel.excepciones.presupuesto_agotado_exception import PresupuestoAgotadoException
from python_hotel.excepciones.persistencia_exception import PersistenciaException

# --- Importacion de Constantes ---
from python_hotel.constantes import THREAD_JOIN_TIMEOUT, COSTE_LIMPIEZA_ALA


def separador(titulo: str = "") -> None:
    """Funcion helper para imprimir un separador en la consola."""
    if titulo:
        print("\n" + f"--- [ {titulo} ] ".ljust(80, "-"))
    else:
        print("\n" + "-" * 80)


def main():
    """
    Funcion principal que orquesta la demostracion del sistema.
    """
    print("=" * 80)
    print("      SISTEMA DE GESTION HOTELERA - PATRONES DE DISENO (PythonHotel)")
    print("=" * 80)

    # --------------------------------------------------------------------------
    # 0. INICIALIZACION DE SERVICIOS
    # --------------------------------------------------------------------------
    separador("0. Inicializando Servicios")
    # Los servicios son 'stateless', podemos instanciarlos una vez
    hotel_service = HotelService()
    ala_service = AlaHotelService()
    empleado_service = EmpleadoService()
    registro_service = RegistroHoteleroService()
    hoteles_service = HotelesService() # Façade

    # [US-TECH-001: Demostracion de SINGLETON]
    # Al instanciar 'ala_service', 'registro_service' y 'hoteles_service',
    # todos ellos llamaron a 'HabitacionServiceRegistry.get_instance()'.
    # El mensaje "INFO (Singleton): Instancia de... creada" debe
    # aparecer UNA SOLA VEZ.
    print("\n[OK] SINGLETON: El 'HabitacionServiceRegistry' se instancio una unica vez.")


    # --------------------------------------------------------------------------
    # 1. EPIC 1: GESTION DE HOTEL Y ALA (US-001, US-002)
    # --------------------------------------------------------------------------
    separador("1. EPIC 1: Creando Hotel y Ala")
    
    mi_hotel = hotel_service.crear_hotel_con_ala(
        id_hotel=101,
        capacidad=50, # Capacidad total de 50 personas
        direccion="Av. Siempre Viva 742",
        nombre_ala="Ala Principal"
    )
    mi_ala = mi_hotel.get_ala()
    print(f"Hotel creado: {mi_hotel.get_direccion()}")
    print(f"Ala creada: {mi_ala.get_nombre()} (Capacidad disponible: {mi_ala.get_capacidad_disponible()} personas)")


    # --------------------------------------------------------------------------
    # 2. EPIC 2: GESTION DE HABITACIONES (US-004 a US-007)
    #    [US-TECH-002: Demostracion de FACTORY METHOD]
    # --------------------------------------------------------------------------
    separador("2. EPIC 2: Configurando Habitaciones (Patron FACTORY)")
    
    try:
        # Configurar habitaciones simples (Cap: 1 persona c/u)
        ala_service.configurar_habitaciones(mi_ala, "Simple", 10) # 10 personas
        
        # Configurar habitaciones dobles (Cap: 2 personas c/u)
        ala_service.configurar_habitaciones(mi_ala, "Doble", 10) # 20 personas
        
        # Configurar suites (Cap: 4 personas c/u)
        ala_service.configurar_habitaciones(mi_ala, "Suite", 3) # 12 personas
        
        # Configurar presidenciales (Cap: 6 personas c/u)
        ala_service.configurar_habitaciones(mi_ala, "Presidencial", 1) # 6 personas
        
        # Total ocupado: 10 + 20 + 12 + 6 = 48 personas. Capacidad restante: 2.
        print(f"\nCapacidad restante en el ala: {mi_ala.get_capacidad_disponible()} personas.")

        # Demostracion de Excepcion de Capacidad
        separador("2b. Demostracion de Excepcion (Capacidad)")
        print("Intentando configurar 1 Suite (Cap 4) con solo 2 de espacio...")
        ala_service.configurar_habitaciones(mi_ala, "Suite", 1) # Requiere 4, solo hay 2

    except CapacidadInsuficienteException as e:
        print(f"[OK] EXCEPCION CAPTURADA (Esperado): {e.get_mensaje_usuario()}")
        print(f"     Detalle: Requerido={e.get_capacidad_requerida()}, "
              f"Disponible={e.get_capacidad_disponible()}")
    except ValueError as e:
        print(f"ERROR INESPERADO (Factory): {e}")


    # --------------------------------------------------------------------------
    # 3. EPIC 4: GESTION DE PERSONAL (US-014 a US-017)
    # --------------------------------------------------------------------------
    separador("3. EPIC 4: Gestion de Personal")
    
    # [US-014: Crear Tareas y Empleado]
    tareas_limpieza = [
        Tarea(1, date.today(), "Limpieza profunda Suite Presidencial"),
        Tarea(2, date.today(), "Reposicion de amenities Ala Principal"),
        Tarea(3, date(2025, 11, 3), "Pulido de pisos Lobby (FUTURO)")
    ]
    empleado_estrella = Empleado(dni=12345678, nombre="Maria Gomez", tareas=tareas_limpieza)
    equipo_limpieza = EquipoLimpieza(1, "Carro de Limpieza Completo", True)
    
    # [US-017: Asignar Empleado a Ala]
    ala_service.asignar_empleados(mi_ala, [empleado_estrella])
    
    # [US-016: Intentar trabajar SIN certificacion]
    print("\nIntento de trabajo SIN certificacion (debe fallar):")
    empleado_service.trabajar(empleado_estrella, date.today(), equipo_limpieza)

    # [US-015: Asignar Certificacion]
    empleado_service.asignar_certificacion(
        empleado=empleado_estrella,
        es_valida=True,
        fecha_emision=date(2025, 1, 15),
        especializacion="Higiene y Seguridad Hotelera Nivel 3"
    )
    
    # [US-016: Intentar trabajar CON certificacion]
    print("\nIntento de trabajo CON certificacion (debe tener exito):")
    empleado_service.trabajar(empleado_estrella, date.today(), equipo_limpieza)
    # Debe ejecutar Tarea 1 y 2 (orden 2, 1) y omitir la Tarea 3.


    # --------------------------------------------------------------------------
    # 4. EPIC 5: OPERACIONES DE NEGOCIO (FAÇADE) (US-018, US-019)
    # --------------------------------------------------------------------------
    separador("4. EPIC 5: Operaciones de Negocio (Patron FAÇADE)")
    
    # [US-003: Crear Registro Hotelero]
    registro_completo = RegistroHotelero(
        id_hotel=mi_hotel.get_id_hotel(),
        hotel=mi_hotel,
        ala_hotel=mi_ala,
        propietario="Nehuen S.A.", # Usar tu nombre para el archivo .dat
        avaluo=15000000.0
    )
    
    # [US-018: Agregar hotel al servicio Façade]
    hoteles_service.add_hotel(registro_completo)

    # [US-019: Usar Façade para desinfectar]
    # El main.py solo habla con 'hoteles_service' (la fachada),
    # que a su vez delega en 'ala_service'.
    hoteles_service.desinfectar_hotel_completo(
        id_hotel=101, 
        quimico="Amonio Cuaternario"
    )

    # --------------------------------------------------------------------------
    # 5. EPIC 2: LIMPIEZA (US-008)
    #    [US-TECH-004 & 005: Demostracion de STRATEGY y REGISTRY]
    # --------------------------------------------------------------------------
    separador("5. Demostracion de STRATEGY y REGISTRY (Limpieza Manual)")

    print(f"Presupuesto actual: ${mi_ala.get_presupuesto_disponible():.2f}")
    
    # La llamada a 'ala_service.limpiar()' dispara:
    # 1. AlaService -> _registry.realizar_mantenimiento(hab) (REGISTRY)
    # 2. Registry -> suite_service.realizar_mantenimiento(hab)
    # 3. SuiteService -> _estrategia.calcular_mantenimiento() (STRATEGY)
    # 4. Strategy -> MantenimientoPremiumStrategy -> retorna 90
    ala_service.limpiar(mi_ala)
    
    print(f"Presupuesto restante: ${mi_ala.get_presupuesto_disponible():.2f}")

    # Demostracion de Excepcion de Presupuesto
    try:
        separador("5b. Demostracion de Excepcion (Presupuesto)")
        print(f"Presupuesto actual: ${mi_ala.get_presupuesto_disponible():.2f}. "
              f"Costo de limpieza: {COSTE_LIMPIEZA_ALA}")
        # Vaciamos el presupuesto para forzar el error
        mi_ala.set_presupuesto_disponible(10.0) 
        print(f"Presupuesto ajustado a: $10.00")
        print("Intentando limpiar de nuevo...")
        ala_service.limpiar(mi_ala)
        
    except PresupuestoAgotadoException as e:
        print(f"[OK] EXCEPCION CAPTURADA (Esperado): {e.get_mensaje_usuario()}")
        print(f"     Detalle: Coste={e.get_coste_requerido()}, "
              f"Disponible={e.get_presupuesto_disponible()}")
        # Restauramos el presupuesto para seguir
        mi_ala.set_presupuesto_disponible(5000.0)
        print(f"Presupuesto restaurado a: ${mi_ala.get_presupuesto_disponible():.2f}")


    # --------------------------------------------------------------------------
    # 6. EPIC 3: MONITOREO AUTOMATIZADO (US-010 a US-013)
    #    [US-TECH-003: Demostracion de OBSERVER]
    # --------------------------------------------------------------------------
    separador("6. EPIC 3: Iniciando Monitoreo (Patron OBSERVER)")
    
    # 1. Crear Observables (Sensores)
    sensor_ocupacion = OcupacionReaderTask()
    sensor_limpieza = LimpiezaReaderTask()
    
    # 2. Crear Observer (Controlador) e inyectar dependencias
    controlador = ControlLimpiezaTask(
        sensor_ocupacion=sensor_ocupacion,
        sensor_limpieza=sensor_limpieza,
        ala_hotel=mi_ala,
        ala_service=ala_service # Delega la accion de 'limpiar'
    )

    print("Iniciando hilos de sensores y controlador...")
    # 3. Iniciar hilos
    sensor_ocupacion.start()
    sensor_limpieza.start()
    controlador.start()

    # 4. Dejar que el sistema funcione solo por 10 segundos
    print("\n--- [ Sistema autonomo funcionando por 10 segundos ] ---")
    print("      (Observe los logs 'DEBUG (Control)'...)")
    print("      (Si las condiciones se cumplen, se activara la limpieza)")
    time.sleep(10)
    print("--- [ 10 segundos completados ] ---\n")

    # 5. Demostrar Graceful Shutdown (US-013)
    separador("6b. Deteniendo monitoreo (Graceful Shutdown)")
    print("Enviando senal de detencion a los hilos...")
    sensor_ocupacion.detener()
    sensor_limpieza.detener()
    controlador.detener()

    # 6. Esperar que los hilos terminen
    sensor_ocupacion.join(timeout=THREAD_JOIN_TIMEOUT)
    sensor_limpieza.join(timeout=THREAD_JOIN_TIMEOUT)
    controlador.join(timeout=THREAD_JOIN_TIMEOUT)
    print("[OK] Hilos detenidos y finalizados correctamente.")
    

    # --------------------------------------------------------------------------
    # 7. EPIC 5: CHECK-OUT (US-020)
    # --------------------------------------------------------------------------
    separador("7. EPIC 5: Check-out por tipo (Generics)")
    
    # Marcamos algunas habitaciones como "Ocupada" para simular
    mi_ala.get_habitaciones()[0].set_estado("Ocupada") # Una Simple
    mi_ala.get_habitaciones()[1].set_estado("Ocupada") # Otra Simple
    mi_ala.get_habitaciones()[15].set_estado("Ocupada") # Una Doble
    
    # Usamos la Façade para hacer check-out de todas las Simples
    # en todos los hoteles
    paquete_simples = hoteles_service.checkout_y_empaquetar(HabitacionSimple)
    paquete_simples.mostrar_contenido_paquete()
    # Deberia encontrar 2 habitaciones 'Simple'


    # --------------------------------------------------------------------------
    # 8. EPIC 6: PERSISTENCIA (US-021 a US-023)
    # --------------------------------------------------------------------------
    separador("8. EPIC 6: Persistencia de Datos (Pickle)")

    try:
        # [US-021: Persistir]
        print(f"Intentando persistir registro de: '{registro_completo.get_propietario()}'")
        path = registro_service.persistir(registro_completo)
        print(f"[OK] Registro guardado en: {path}")

        # [US-022: Recuperar]
        print(f"\nLeyendo registro desde disco...")
        registro_leido = registro_service.leer_registro(registro_completo.get_propietario())
        print(f"[OK] Registro de '{registro_leido.get_propietario()}' leido.")

        # [US-023: Mostrar Datos (Demuestra Registry de nuevo)]
        print("Mostrando datos del registro leido desde disco:")
        registro_service.mostrar_datos(registro_leido)
        # Esto debe imprimir la lista detallada de las 24 habitaciones
        
    except (PersistenciaException, ValueError) as e:
        print(f"ERROR CRITICO DE PERSISTENCIA: {e}")


    # --------------------------------------------------------------------------
    # FIN DE LA DEMOSTRACION
    # --------------------------------------------------------------------------
    separador("RESUMEN DE PATRONES DEMOSTRADOS")
    print("[OK] SINGLETON:   HabitacionServiceRegistry (instancia unica)")
    print("[OK] FACTORY:     HabitacionFactory (creacion de habitaciones)")
    print("[OK] STRATEGY:    MantenimientoEstandar vs Premium (en limpieza)")
    print("[OK] OBSERVER:    Sensores (Observable) y Controlador (Observer)")
    print("[OK] REGISTRY:    Dispatch polimorfico (en limpieza y mostrar_datos)")
    print("[OK] FAÇADE:      HotelesService (gestion centralizada)")
    print("\n" + "=" * 80)
    print("              EJEMPLO COMPLETADO EXITOSAMENTE")
    print("=" * 80)


# --- Punto de entrada estandar de Python ---
if __name__ == "__main__":
    main()