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