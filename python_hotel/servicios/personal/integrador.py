"""
Archivo integrador generado automaticamente
Directorio: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/servicios/personal
Fecha: 2025-11-04 18:03:54
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/servicios/personal/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: empleado_service.py
# Ruta: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/servicios/personal/empleado_service.py
# ================================================================================

"""
Modulo del Servicio de Empleado.

Logica de negocio para gestionar un Empleado:
- Asignar certificaciones (ex AptoMedico)
- Ejecutar tareas (verificando certificacion)
"""

from datetime import date
from typing import TYPE_CHECKING

# Importacion de Entidades
from python_hotel.entidades.personal.empleado import Empleado
from python_hotel.entidades.personal.certificacion import Certificacion

if TYPE_CHECKING:
    from python_hotel.entidades.personal.equipo_limpieza import EquipoLimpieza


class EmpleadoService:
    """
    Servicio 'stateless' para operaciones de negocio sobre un Empleado.
    """

    def __init__(self):
        pass

    def asignar_certificacion(self,
                              empleado: Empleado,
                              es_valida: bool,
                              fecha_emision: date,
                              especializacion: str,
                              observaciones: str = "") -> None:
        """
        Metodo 'constructor' para crear y asignar una Certificacion a un empleado.
        """
        print(f"\nINFO: Asignando certificacion '{especializacion}' a {empleado.get_nombre()}...")
        
        cert = Certificacion(
            es_valida=es_valida,
            fecha_emision=fecha_emision,
            especializacion=especializacion,
            observaciones=observaciones
        )
        
        empleado.set_certificacion(cert)
        
        if not es_valida:
            print(f"ADVERTENCIA: La certificacion asignada no esta vigente.")

    def trabajar(self, 
                 empleado: Empleado, 
                 fecha: date, 
                 equipo: 'EquipoLimpieza') -> bool:
        """
        Ejecuta las tareas de un empleado para una fecha dada,
        siempre y cuando tenga una certificacion valida.

        (Adaptacion de US-016)

        Args:
            empleado: El empleado que va a trabajar.
            fecha: El dia de trabajo (solo ejecuta tareas de esa fecha).
            equipo: El equipo (ex Herramienta) que utilizara.

        Returns:
            True si pudo trabajar, False si no tenia certificacion.
        """
        print(f"\nINFO: {empleado.get_nombre()} intenta iniciar jornada laboral...")
        
        # 1. Validar Certificacion (ex AptoMedico)
        certificacion = empleado.get_certificacion()
        
        if not certificacion or not certificacion.esta_certificacion_valida():
            print(f"ERROR: {empleado.get_nombre()} no puede trabajar. "
                  f"Certificacion invalida o inexistente.")
            return False

        print(f"INFO: Certificacion '{certificacion.get_especializacion()}' validada.")

        # 2. Filtrar tareas por fecha y estado
        tareas_asignadas = empleado.get_tareas()
        tareas_para_hoy = [
            t for t in tareas_asignadas
            if t.get_fecha_programada() == fecha and t.get_estado() == "Pendiente"
        ]

        if not tareas_para_hoy:
            print(f"INFO: {empleado.get_nombre()} no tiene tareas pendientes para hoy ({fecha}).")
            return True # Pudo "trabajar" (no tenia nada que hacer)

        # 3. Ordenar tareas (por ID descendente, como en US-016)
        tareas_para_hoy.sort(key=lambda t: t.get_id_tarea(), reverse=True)

        # 4. Ejecutar tareas
        print(f"INFO: {empleado.get_nombre()} comienza sus tareas con equipo '{equipo.get_nombre()}':")
        for tarea in tareas_para_hoy:
            print(f"  -> Ejecutando Tarea {tarea.get_id_tarea()}: {tarea.get_descripcion()}...")
            tarea.set_estado("Completada")
        
        print(f"INFO: Jornada completada. {len(tareas_para_hoy)} tareas realizadas.")
        return True

