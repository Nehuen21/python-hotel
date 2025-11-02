"""
Modulo de Constantes para el Sistema de Gestion Hotelera (PythonHotel).

Este archivo centraliza todas las variables de configuracion, "numeros magicos"
y valores fijos para evitar el "hardcoding" en la logica de negocio,
siguiendo el principio de Codigo Limpio.
"""

# -----------------------------------------------------------------------------
# Configuracion de Persistencia
# -----------------------------------------------------------------------------
DIRECTORIO_DATA: str = "data"
EXTENSION_DATA: str = ".dat"


# -----------------------------------------------------------------------------
# Constantes del Dominio: Hotel y Alas
# -----------------------------------------------------------------------------
PRESUPUESTO_INICIAL_ALA: float = 5000.0
COSTE_LIMPIEZA_ALA: float = 100.0
PRESUPUESTO_MINIMO_OPERACION: float = 0.0


# -----------------------------------------------------------------------------
# Constantes del Dominio: Habitaciones
# -----------------------------------------------------------------------------
ESTADO_INICIAL_HABITACION: str = "Disponible"
ESTADO_MANTENIMIENTO: str = "En Mantenimiento"
ESTADO_OCUPADA: str = "Ocupada"

# --- Habitacion Simple ---
CAPACIDAD_SIMPLE: int = 1
TARIFA_BASE_SIMPLE: float = 50.0

# --- Habitacion Doble ---
CAPACIDAD_DOBLE: int = 2
TARIFA_BASE_DOBLE: float = 80.0

# --- Suite ---
CAPACIDAD_SUITE: int = 4
TARIFA_BASE_SUITE: float = 200.0

# --- Suite Presidencial ---
CAPACIDAD_PRESIDENCIAL: int = 6
TARIFA_BASE_PRESIDENCIAL: float = 500.0


# -----------------------------------------------------------------------------
# Constantes del Patron Strategy (Mantenimiento)
# -----------------------------------------------------------------------------
# Estrategia Estandar (Simple, Doble)
MANTENIMIENTO_ESTANDAR_BASICO: int = 30  # minutos (alta ocupacion)
MANTENIMIENTO_ESTANDAR_COMPLETO: int = 60 # minutos (baja ocupacion)
UMBRAL_OCUPACION_ESTANDAR: float = 0.3 # 30%

# Estrategia Premium (Suites)
MANTENIMIENTO_PREMIUM_SUITE: int = 60  # minutos (constante)
MANTENIMIENTO_PREMIUM_PRESIDENCIAL: int = 90  # minutos (constante)


# -----------------------------------------------------------------------------
# Constantes del Monitoreo y Limpieza (Patron Observer)
# -----------------------------------------------------------------------------

# --- Sensores ---
INTERVALO_SENSOR_OCUPACION: float = 2.0  # segundos
SENSOR_OCUPACION_MIN: int = 0
SENSOR_OCUPACION_MAX: int = 100

INTERVALO_SENSOR_LIMPIEZA: float = 3.0  # segundos
SENSOR_LIMPIEZA_MIN: int = 0
SENSOR_LIMPIEZA_MAX: int = 100

# --- Controlador ---
INTERVALO_CONTROL_LIMPIEZA: float = 2.5  # segundos

# --- Umbrales para limpieza automatica ---
# Se activa si: Ocupacion < 10% Y Limpieza < 70%
OCUPACION_MAX_PARA_LIMPIEZA: float = 10.0  # %
LIMPIEZA_MIN_PARA_LIMPIEZA: float = 70.0  # %


# -----------------------------------------------------------------------------
# Constantes de Concurrencia (Threading)
# -----------------------------------------------------------------------------
THREAD_JOIN_TIMEOUT: float = 2.0  # segundos