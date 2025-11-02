"""
Modulo de Mensajes de Error.

Centraliza los mensajes de error orientados al usuario para las excepciones
personalizadas del dominio.
"""

# --- Mensajes de Negocio ---
CAPACIDAD_INSUFICIENTE: str = "Capacidad insuficiente en el ala del hotel."
PRESUPUESTO_AGOTADO: str = "Presupuesto del ala agotado. No se puede completar la operacion."
EMPLEADO_SIN_CERTIFICACION: str = "El empleado no posee la certificacion valida para operar."

# --- Mensajes de Persistencia ---
ERROR_PERSISTENCIA_ESCRITURA: str = "Error critico al intentar guardar el registro."
ERROR_PERSISTENCIA_LECTURA: str = "Error critico al intentar leer el registro."
ERROR_PERSISTENCIA_GENERICO: str = "Ha ocurrido un error en la capa de persistencia."
ARCHIVO_NO_ENCONTRADO: str = "El archivo de registro solicitado no fue encontrado."