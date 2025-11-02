# Historias de Usuario - Sistema de Gestion Hotelera

**Proyecto**: PythonHotel
**Version**: 1.0.0
**Fecha**: Octubre 2025
**Metodologia**: User Story Mapping

---

## Indice

1. [Epic 1: Gestion de Hoteles y alas ](#epic-1-gestion-de-Hoteles-y-Alas)
2. [Epic 2: Gestion de Habitaciones](#epic-2-gestion-de-habitaciones)
3. [Epic 3: Sistema de Limpieza Automatizado](#epic-3-sistema-de-limpieza-automatizado)
4. [Epic 4: Gestion de Personal](#epic-4-gestion-de-personal)
5. [Epic 5: Operaciones de Negocio](#epic-5-operaciones-de-negocio)
6. [Epic 6: Persistencia y Auditoria](#epic-6-persistencia-y-auditoria)
7. [Historias Tecnicas (Patrones de Diseno)](#historias-tecnicas-patrones-de-diseno)

---

## Epic 1: Gestion de Hoteles y Alas

### US-001: Registrar Hotel

**Como** gerente de hotel
**Quiero** registrar un hotel con su identificación única y capacidad
**Para** tener un control oficial de mis propiedades hoteleras

#### Criterios de Aceptacion

- [x] El sistema debe permitir crear un hotel con:
  - Padron catastral unico (numero entero positivo)
  - Capacidad total en habitaciones (número positivo)
  - Dirección de ubicación (cadena de texto)
- [x] La capacidad debe ser mayor a 0, si no lanzar `ValueError`
- [x] El hotel debe poder modificarse posteriormente
- [x] El sistema debe validar que los datos sean consistentes

#### Detalles Tecnicos

**Clase**: `hotel` (`python_hotel/entidades/hotel/hotel.py`)
**Servicio**: `HotelService` (`python_hotel/servicios/hotel/hotel_service.py`)

**Codigo de ejemplo**:
```python
from python_hotel.servicios.hotel.hotel_service import HotelService

hotel_service = HotelService()
hotel = hotel_service.crear_hotel_con_ala(
    id_hotel=1,
    capacidad=100,
    direccion="Av. Principal 123, Ciudad",
    nombre_ala="Ala Norte"
)
```

**Validaciones**:
```python
# Capacidad válida
hotel.set_capacidad(150)  # OK

# Capacidad inválida
hotel.set_capacidad(-50)  # ValueError: capacidad debe ser mayor a cero
hotel.set_capacidad(0)    # ValueError: capacidad debe ser mayor a cero
```

**Trazabilidad**: `main.py` lineas 111-116

---

### US-002: Crear Ala en Hotel

**Como** administrador de hotel
**Quiero** crear un ala asociada a un hotel
**Para** organizar las habitaciones en áreas identificables

#### Criterios de Aceptacion

- [x] Un ala debe tener:
  - Nombre identificatorio unico
  - Capacidad máxima (heredada del hotel)
  - Presupuesto disponible inicial (5000 por defecto)
  - Lista de habitaciones (vacía al inicio)
  - Lista de empleados (vacía al inicio)
- [x] El ala debe estar asociada a un hotel válido
- [x] El presupuesto no puede ser negativo
- [x] El sistema debe controlar la capacidad ocupada vs disponible
#### Detalles Tecnicos

**Clase**: `AlaHotel` (`python_hotel/entidades/hotel/ala_hotel.py`)
**Servicio**: `AlaHotelService` (`python_hotel/servicios/hotel/ala_hotel_service.py`)

**Codigo de ejemplo**:
```python
from python_hotel.entidades.hotel.ala_hotel import AlaHotel

ala_hotel = AlaHotel(
    nombre="Ala Norte",
    capacidad=100,
    presupuesto=5000
)

# Obtener desde hotel
ala_hotel = hotel.get_ala()
```

**Validaciones**:
```python
# Presupuesto válido
ala_hotel.set_presupuesto_disponible(10000)  # OK

# Presupuesto inválido
ala_hotel.set_presupuesto_disponible(-1000)  # ValueError: presupuesto no puede ser negativo
```

**Trazabilidad**: `main.py` linea 117, `tierra_service.py` lineas 21-54

---

### US-003: Crear Registro hotelero Completo

**Como** auditor hotelero
**Quiero** ccrear un registro hotelero que vincule hotel, ala, propietario y avalúo
**Para** tener documentación oficial completa

#### Criterios de Aceptacion

- [x] Un registro hotelero debe contener:
  - ID de hotel (número único)
  - Referencia a Hotel
  - Referencia a AlaHotel
  - Nombre del propietario
  - Avaluo fiscal (numero decimal positivo)
- [x] Todos los campos son obligatorios
- [x] El registro debe poder persistirse y recuperarse
- [x] El registro debe poder mostrarse en consola con formato

#### Detalles Tecnicos

**Clase**: `RegistroHotelero` (`python_hotel/entidades/hotel/registro_hotelero.py`)
**Servicio**: `RegistroHoteleroService` (`python_hotel/servicios/hotel/registro_hotelero_service.py`)

**Codigo de ejemplo**:
```python
from python_hotel.entidades.hotel.registro_hotelero import RegistroHotelero

registro = RegistroHotelero(
    id_hotel=1,
    hotel=hotel,
    ala_hotel=ala_hotel,
    propietario="Carlos Rodríguez",
    avaluo=15000000.75
)
```

**Salida de mostracion**:
```
REGISTRO HOTELERO
=================
Hotel ID:      1
Propietario:   Carlos Rodríguez
Avalúo:        15000000.75
Dirección:     Av. Principal 123, Ciudad
Capacidad:     100
Cantidad de habitaciones configuradas: 26
```

**Trazabilidad**: `main.py` lineas 123-129

---

## Epic 2: Gestion de Habitaciones

### US-004: Configurar Habitaciones Simples en Ala

**Como** administrador de hotel
**Quiero** configurar habitaciones simples
**Para** frecer alojamiento económico individual

#### Criterios de Aceptacion

- [x] Debe poder configurar múltiples habitaciones simples simultáneamente
- [x] Cada habitación simple debe tener:
  - Tipo: Simple
  - Capacidad: 1 persona
  - Tarifa base: 50.0
  - Estado: Disponible
- [x] El sistema debe verificar capacidad disponible
- [x] Si no hay capacidad, lanzar `CapacidadInsuficienteException`
- [x] Las habitaciones deben crearse via Factory Method (no instanciación directa)

#### Detalles Tecnicos

**Clase**: `HabitacionSimple` (`python_hotel/entidades/habitaciones/habitacion_simple.py`)
**Servicio**: `HabitacionSimpleService` (`python_hotel/servicios/habitaciones/habitacion_simple_service.py`)
**Factory**: `HabitacionFactory` (`python_hotel/patrones/factory/habitacion_factory.py`)

**Codigo de ejemplo**:
```python
from python_hotel.servicios.hotel.ala_hotel_service import AlaHotelService

ala_hotel_service = AlaHotelService()

# Configurar 5 habitaciones simples (usa Factory Method internamente)
ala_hotel_service.configurar(ala_hotel, "Simple", 5)

# Capacidad requerida: 5 * 1 = 5 personas
# Capacidad ocupada aumenta automáticamente
```

**Constantes utilizadas**:
```python
CAPACIDAD_SIMPLE = 1  # persona
TARIFA_BASE_SIMPLE = 50.0  # dólares
ESTADO_INICIAL = "Disponible"
```

**Trazabilidad**: `main.py` linea 141

---

### US-005: Configurar Habitaciones Dobles con Servicios

**Como** administrador de hotel
**Quiero** configurar habitaciones dobles especificando servicios incluidos
**Para** ofrecer alojamiento para dos personas


#### Criterios de Aceptacion

- [x] Debe poder configurar múltiples habitaciones dobles simultáneamente
- [x] Cada habitación doble debe tener:
  - Tipo: Doble
  - Capacidad: 2 personas
  - Tarifa base: 80.0
  - Servicios: Desayuno incluido (True/False)
  - Estado: Disponible
- [x] El sistema debe verificar capacidad disponible
- [x] Las habitaciones deben crearse via Factory Method

#### Detalles Tecnicos

**Clase**: `HabitacionDoble` (`python_hotel/entidades/habitaciones/habitacion_doble.py`)
**servicio**: `HabitacionDobleService` (`python_hotel/servicios/habitaciones/habitacion_doble_service.py`)

**Codigo de ejemplo**:
```python
# Configurar 3 habitaciones dobles (servicios se asignan por defecto)
ala_hotel_service.configurar(ala_hotel, "Doble", 3)

# Capacidad requerida: 3 * 2 = 6 personas
```

**servicios disponibles**:
```python
# Por defecto incluye desayuno
habitacion_doble.get_servicios()  # Retorna lista de servicios
```

**Constantes utilizadas**:
```python
CAPACIDAD_DOBLE = 2  # personas
TARIFA_BASE_DOBLE = 80.0  # dólares
```

**Trazabilidad**: `main.py` linea 142

---

### US-006: Configurar Suites con Amenities
**Como** administrador de hotel
**Quiero** configurar suites con amenities premium
**Para** ofrecer alojamiento de lujo

#### Criterios de Aceptacion

- [x]Debe poder configurar múltiples suites simultáneamente
- [x] Cada suite debe tener:
  - Tipo: Suite
  - Capacidad: 4 personas
  - Tarifa base: 200.0
  - Amenities: Jacuzzi, Mini-bar, Room service
  - Estado: Disponible
- [x] Las suites ocupan más capacidad que habitaciones estándar
- [x] El sistema debe verificar capacidad disponible

#### Detalles Tecnicos

**Clase**: `Suite` (`python_hotel/entidades/habitaciones/suite.py`)
**Servicio**: `SuiteService` (`python_hotel/servicios/habitaciones/suite_service.py`)

**Codigo de ejemplo**:
```python
# Configurar 2 suites
ala_hotel_service.configurar(ala_hotel, "Suite", 2)

# Capacidad requerida: 2 * 4 = 8 personas
```

**Constantes utilizadas**:
```python
CAPACIDAD_SUITE = 4  # personas
TARIFA_BASE_SUITE = 200.0  # dólares
```

**Trazabilidad**: `main.py` linea 143

---

### US-007:Configurar Suites Presidenciales (Con y Sin Terraza)

**Como** administrador de hotel
**Quiero** configurar suites presidenciales normales o con terraza
**Para** diversificar la oferta de lujo

#### Criterios de Aceptacion

- [x] Debe poder configurar múltiples suites presidenciales simultáneamente
- [x] Cada suite presidencial debe tener:
  - Tipo: Presidencial
  - Capacidad: 6 personas
  - Tarifa base: 500.0
  - Terraza: True/False
  - Estado: Disponible
- [x] Las suites presidenciales requieren más capacidad
- [x] El sistema debe verificar capacidad disponible

#### Detalles Tecnicos

**Clase**: `SuitePresidencial` (`python_hotel/entidades/habitaciones/suite_presidencial.py`)
**Servicio**: `SuitePresidencialService` (`python_hotel/servicios/habitaciones/suite_presidencial_service.py`)

**Codigo de ejemplo**:
```python
# Configurar 1 suite presidencial
ala_hotel_service.configurar(ala_hotel, "Presidencial", 1)

# Capacidad requerida: 1 * 6 = 6 personas
```

**Constantes utilizadas**:
```python
CAPACIDAD_PRESIDENCIAL = 6  # personas
TARIFA_BASE_PRESIDENCIAL = 500.0  # dólares
```

**Verificar tipo**:
```python
suite_presidencial = habitaciones[0]
if suite_presidencial.tiene_terraza():
    print("Suite presidencial con terraza")
else:
    print("Suite presidencial estándar")
```

**Trazabilidad**: `main.py` linea 144

---

### US-008: Limpiar Todas las Habitaciones de un Ala

**Como** sistema automatizado de limpieza
**Quiero** limpiar todas las habitaciones de un ala
**Para** mantener el nivel de higiene necesario

#### Criterios de Aceptacion

- [x] La limpieza debe:
  - Consumir presupuesto del ala (100 por limpieza)
  - Realizar mantenimiento en todas las habitaciones
  - Cada habitación recibe mantenimiento según su estrategia
  - Habitaciones estándar (Simple, Doble): Mantenimiento básico (30 min)
  - Suites premium (Suite, Presidencial): Mantenimiento completo (60-90 min)
- [x] Si no hay suficiente presupuesto, lanzar `PresupuestoAgotadoException`
- [x] Las habitaciones deben actualizar estado después del mantenimiento
- [x] El sistema debe usar el patrón Strategy para mantenimiento

#### Detalles Tecnicos

**Servicio**: `AlaHotelService.limpiar()`
**Estrategias**:
- `MantenimientoEstandarStrategy` (habitaciones estándar)
- `MantenimientoPremiumStrategy` (suites)

**Codigo de ejemplo**:
```python
# Limpiar ala
ala_hotel_service.limpiar(ala_hotel)

# Proceso:
# 1. Verifica presupuesto disponible >= 100
# 2. Consume 100 del presupuesto del ala
# 3. Cada habitación recibe mantenimiento según su estrategia
# 4. Habitaciones actualizan estado
```

**mantenimiento por tipo**:
```python
# Simple y Doble (estándar)
# - Baja ocupación: 60 min
# - Alta ocupación: 30 min

# Suite (premium)
# - Siempre: 60 min

# Presidencial (premium)
# - Siempre: 90 min
```

**Actualizacion de estado**:
```python
# Después del mantenimiento, estado cambia a "Lista"
habitacion.set_estado("Lista")
```

**Trazabilidad**: `hotel_service.py` lineas 82-129 # puede que esta linea este mal

---

### US-009: Mostrar Datos de Habitaciones por Tipo

**Como** administrador de hotel
**Quiero** ver los datos de cada habitación de forma específica
**Para** conocer el estado actual de mi hotel

#### Criterios de Aceptacion

- [x]El sistema debe mostrar datos específicos por tipo:
  - **Simple**:  Habitación, Capacidad, Tarifa, ID, Estado
  - **Doble**: Habitación, Capacidad, Tarifa, Servicios incluidos
  - **Suite**: Habitación, Capacidad, Tarifa, Amenities
  - **Presidencial**:  Habitación, Capacidad, Tarifa, Con terraza
- [x] Usar el patron Registry para dispatch polimorfico
- [x] NO usar cascadas de isinstance()

#### Detalles Tecnicos

**Registry**: `HabitacionServiceRegistry.mostrar_datos()`

**Codigo de ejemplo**:
```python
from python_hotel.servicios.habitaciones.habitacion_service_registry import HabitacionServiceRegistry

registry = HabitacionServiceRegistry.get_instance()

for habitacion in ala_hotel.get_habitaciones():
    registry.mostrar_datos(habitacion)
    # Despacho automático al servicio correcto
```

**Salida ejemplo (Pino)**:
```
Habitación: Simple
Capacidad: 1 persona
Tarifa base: 50.0 USD
ID: 1
Estado: Disponible
```


---

## Epic 3:  Sistema de Limpieza Automatizado

### US-010: Monitorear Ocupación en Tiempo Real

**Como**  sistema de limpieza automatizado
**Quiero** leer la ocupación ambiental cada 2 segundos
**Para** tomar decisiones de limpieza basadas en condiciones reales
#### Criterios de Aceptacion

- [x] El sensor debe:
  - Ejecutarse en un thread daemon separado
  - Leer ocupación cada 2 segundos (configurable)
  - Generar lecturas aleatorias entre 0% y 100%
  - Notificar a observadores cada vez que lee
  - Soportar detencion graceful con timeout
- [x] Implementar patron Observer (Observable)
- [x] Usar Generics para tipo-seguridad: `Observable[float]`

#### Detalles Tecnicos

**Clase**: `OcupacionReaderTask` (`python_hotel/monitoreo/sensores/ocupacion_reader_task.py`)
**Patron**: Observer (Observable[float])

**Codigo de ejemplo**:
```python
from python_hotel.monitoreo.sensores.ocupacion_reader_task import OcupacionReaderTask

# Crear sensor (thread daemon)
sensor_ocupacion = OcupacionReaderTask()

# Iniciar lectura continua
sensor_ocupacion.start()

# Detener cuando sea necesario
sensor_ocupacion.detener()
sensor_ocupacion.join(timeout=2.0)
```

**Constantes**:
```python
INTERVALO_SENSOR_OCUPACION = 2.0  # segundos
SENSOR_OCUPACION_MIN = 0  # %
SENSOR_OCUPACION_MAX = 100  # %
```

**Eventos generados**:
```python
# Cada lectura notifica valor float a observadores
ocupacion: float = 45.5
self.notificar_observadores(ocupacion)
```

**Trazabilidad**: `main.py` lineas 158-166

---

### US-011:  Monitorear Nivel de Limpieza en Tiempo Real

**Como**  sistema de limpieza automatizado
**Quiero** leer el nivel de limpieza cada 3 segundos
**Para** complementar datos de ocupación en decisiones de limpieza

#### Criterios de Aceptacion

- [x] El sensor debe:
  - Ejecutarse en un thread daemon separado
  - Leer limpieza cada 3 segundos (configurable)
  - Generar lecturas aleatorias entre 0% y 100%
  - Notificar a observadores cada vez que lee
  - Soportar detencion graceful con timeout
- [x] Implementar patron Observer (Observable)
- [x] Usar Generics para tipo-seguridad: `Observable[float]`

#### Detalles Tecnicos

**Clase**: `LimpiezaReaderTask` (`python_hotel/monitoreo/sensores/limpieza_reader_task.py`)
**Patron**: Observer (Observable[float])

**Codigo de ejemplo**:
```python
from python_hotel.monitoreo.sensores.limpieza_reader_task import LimpiezaReaderTask

# Crear sensor (thread daemon)
sensor_limpieza = LimpiezaReaderTask()

# Iniciar lectura continua
sensor_limpieza.start()

# Detener cuando sea necesario
sensor_limpieza.detener()
sensor_limpieza.join(timeout=2.0)
```

**Constantes**:
```python
INTERVALO_SENSOR_LIMPIEZA = 3.0  # segundos
SENSOR_LIMPIEZA_MIN = 0  # %
SENSOR_LIMPIEZA_MAX = 100  # %
```

**Trazabilidad**: `main.py` lineas 158-166

---

### US-012: Control Automático de Limpieza Basado en Sensores

**Como** sistema de limpieza automatizado
**Quiero** r limpiar automáticamente cuando se cumplan condiciones ambientales
**Para**  optimizar el uso de recursos según necesidades reales

#### Criterios de Aceptacion

- [x] El controlador debe:
  - Ejecutarse en un thread daemon separado
  - Evaluar condiciones cada 2.5 segundos
  - OObservar sensores de ocupación y limpieza
  - Limpiar cuando:
    - Ocupación menor a 10%, Y
    - Nivel de limpieza menor a 70%
  - NO limpiar si condiciones no se cumplen
  - Manejar excepción si no hay presupuesto disponible
- [x] Implementar patron Observer (Observer[float])
- [x] Recibir sensores via inyeccion de dependencias

#### Detalles Tecnicos

**Clase**: `ControlLimpiezaTask` (`python_hotel/monitoreo/control/control_limpieza_task.py`)
**Patron**: Observer (observa sensores)

**Codigo de ejemplo**:
```python
from python_hotel.monitoreo.control.control_limpieza_task import ControlLimpiezaTask

# Inyectar dependencias
control_limpieza = ControlLimpiezaTask(
    sensor_ocupacion=sensor_ocupacion,
    sensor_limpieza=sensor_limpieza,
    ala_hotel=ala_hotel,
    ala_hotel_service=ala_hotel_service
)

# Iniciar control automático
control_limpieza.start()

# Detener cuando sea necesario
control_limpieza.detener()
control_limpieza.join(timeout=2.0)
```

**Logica de decision**:
```python
if (ocupacion < OCUPACION_MAX_LIMPIEZA) and (limpieza < LIMPIEZA_MIN_REQUERIDA):
    # LIMPIAR
    ala_hotel_service.limpiar(ala_hotel)
else:
    # NO LIMPIAR
    pass
```

**Constantes de riego**:
```python
OCUPACION_MAX_LIMPIEZA = 10  # %
LIMPIEZA_MIN_REQUERIDA = 70  # %
INTERVALO_CONTROL_LIMPIEZA = 2.5  # segundos
```

**Trazabilidad**: `main.py` lineas 160-166

---

### US-013:  Detener Sistema de Limpieza de Forma Segura

**Como** administrador del sistema
**Quiero** detener el sistema de limpieza de forma controlada
**Para**  evitar corrupción de datos o procesos incompletos

#### Criterios de Aceptacion

- [x] El sistema debe:
  - Detener todos los threads con `threading.Event`
  - Esperar finalizacion con timeout configurable (2s)
  - NO forzar terminacion abrupta
  - Permitir que threads completen operacion actual
- [x] Threads deben ser daemon (finalizan con main)
- [x] Usar timeout de `constantes.py`

#### Detalles Tecnicos

**Codigo de ejemplo**:
```python
from python_hotel.constantes import THREAD_JOIN_TIMEOUT

# Detener sensores y control
sensor_ocupacion.detener()
sensor_limpieza.detener()
control_limpieza.detener()

# Esperar finalización con timeout
sensor_ocupacion.join(timeout=THREAD_JOIN_TIMEOUT)  # 2s
sensor_limpieza.join(timeout=THREAD_JOIN_TIMEOUT)
control_limpieza.join(timeout=THREAD_JOIN_TIMEOUT)

# Si timeout expira, threads daemon finalizan automáticamente
```

**Constantes**:
```python
THREAD_JOIN_TIMEOUT = 2.0  # segundos
```

**Trazabilidad**: `main.py` lineas 256-263

---

## Epic 4: Gestion de Personal

### US-014: Registrar Empleado con Tareas Asignadas
**Como** jefe de personal
**Quiero** registrar empleados con sus tareas asignadas
**Para** organizar el trabajo hotelero

#### Criterios de Aceptacion

- [x] Un empleado debe tener:
  - DNI único (número entero)
  - Nombre completo
  - Lista de tareas asignadas (puede estar vacia)
  - Certificación (inicialmente sin certificación)
- [x] Las tareas deben tener:
  - ID unico
  - Fecha programada
  - Descripcion de la tarea
  - Estado (pendiente/completada)
- [x] Un empleado puede tener múltiples tareas
- [x]Lista de empleados es inmutable (defensive copy)

#### Detalles Tecnicos

**Clases**:
- `Empleado` (`python_hotel/entidades/personal/empleado.py`)
- `Tarea` (`python_hotel/entidades/personal/tarea.py`)

**Codigo de ejemplo**:
```python
ffrom python_hotel.entidades.personal.empleado import Empleado
from python_hotel.entidades.personal.tarea import Tarea
from datetime import date

# Crear tareas
tareas = [
    Tarea(1, date.today(), "Limpiar habitaciones 101-110"),
    Tarea(2, date.today(), "Reabastecer amenities"),
    Tarea(3, date.today(), "Revisar sistema de climatización")
]

# Crear empleado
empleado = Empleado(
    dni=43888734,
    nombre="María González",
    tareas=tareas
)
```

**Trazabilidad**: `main.py` lineas 176-185

---

### US-015: Asignar Certificación a Empleado

**Como** gerente de recursos humanos
**Quiero** asignar una certificación a un empleado
**Para** certificar que está calificado para trabajar

#### Criterios de Aceptacion

- [x] Una certificación debe tener:
  - Estado de certificación (True/False)
  - Fecha de emision
  - Observaciones profesionales (opcional)
- [x] El sistema debe verificar certificación antes de trabajar
- [x] Si no tiene certificación válida, no puede ejecutar tareas
- [x] El servicio debe permitir asignar/actualizar certificación

#### Detalles Tecnicos

**Clase**: `Certificacion` (`python_hotel/entidades/personal/certificacion.py`)
**Servicio**: `EmpleadoService.asignar_certificacion()`

**Codigo de ejemplo**:
```python
ffrom python_hotel.servicios.personal.empleado_service import EmpleadoService
from datetime import date

empleado_service = EmpleadoService()

# Asignar certificación
empleado_service.asignar_certificacion(
    empleado=empleado,
    certificada=True,
    fecha_emision=date.today(),
    observaciones="Certificación en limpieza hotelera avanzada"
)

# Verificar certificación
if empleado.get_certificacion().esta_certificada():
    print("Empleado certificado para trabajar")
else:
    print("Empleado NO certificado")
```

**Trazabilidad**: `main.py` lineas 191-196

---

### US-016:  Ejecutar Tareas Asignadas a Empleado

**Como** empleado de limpieza
**Quiero** ejecutar las tareas que me fueron asignadas
**Para** completar mi jornada laboral

#### Criterios de Aceptacion

- [x] El empleado debe:
  - Tener certificación válida
  - Ejecutar solo tareas de la fecha especificada
  - Usar un equipo de limpieza asignado
  - Marcar tareas como completadas
- [x] Las tareas deben ejecutarse en orden ID descendente
- [x] Si no tiene certificación, retornar False (no ejecuta)
- [x] Si tiene certificación, retornar True (ejecuta)
#### Detalles Tecnicos

**Servicio**: `EmpleadoService.trabajar()`
**Clase**: `EquipoLimpieza` (`python_hotel/entidades/personal/equipo_limpieza.py`)

**Codigo de ejemplo**:
```python
from python_hotel.entidades.personal.equipo_limpieza import EquipoLimpieza

# Crear equipo
equipo = EquipoLimpieza(
    id_equipo=1,
    nombre="Carro de limpieza premium",
    certificado_higiene=True
)

# Ejecutar tareas
resultado = empleado_service.trabajar(
    empleado=empleado,
    fecha=date.today(),
    equipo=equipo
)

if resultado:
    print("Tareas ejecutadas exitosamente")
else:
    print("No puede trabajar - sin certificación válida")
```

**Salida esperada**:
```
El empleado María González realizó la tarea 3 Revisar sistema de climatización con equipo: Carro de limpieza premium
El empleado María González realizó la tarea 2 Reabastecer amenities con equipo: Carro de limpieza premium
El empleado María González realizó la tarea 1 Limpiar habitaciones 101-110 con equipo: Carro de limpieza premium
```

**Ordenamiento**:
```python
## Tareas se ordenan por ID descendente (3, 2, 1)
# Usa método estático _obtener_id_tarea() en lugar de lambda
```

**Trazabilidad**: `main.py` lineas 199-204, `empleado_service.py` lineas 34-72

---

### US-017:  Asignar Empleados a Ala Hotel
**Como** jefe de personal
**Quiero** asignar empleados a un ala específica
**Para** organizar el personal por área

#### Criterios de Aceptacion

- [x] Un ala debe poder tener múltiples empleados
- [x] La lista de empleados debe ser inmutable (defensive copy)
- [x] Debe poder obtener lista de empleados
- [x] Debe poder reemplazar lista completa de empleados

#### Detalles Tecnicos

**Clase**: `AlaHotel.set_empleados()`

**Codigo de ejemplo**:
```python
empleados = [
    Empleado(43888734, "María González", tareas.copy()),
    Empleado(40222333, "Carlos López", tareas.copy())
]

# Asignar empleados al ala
ala_hotel.set_empleados(empleados)

# Obtener empleados (copia inmutable)
lista_empleados = ala_hotel.get_empleados()
```

**Trazabilidad**: `main.py` linea 187

---

## Epic 5: Operaciones de Negocio

### US-018:  Gestionar Múltiples Hoteles

**Como**  propietario de múltiples hoteles
**Quiero**  gestionar varios hoteles desde un servicio centralizado
**Para**  tener control unificado de todas mis propiedades

#### Criterios de Aceptacion

- [x] El servicio debe permitir:
  - Agregar hoteles (RegistroHotelero)
  - Buscar hotel por ID
  - Desinfectar un hotel específico
  - Realizar check-out y empaquetar por tipo de habitación
- [x] Debe manejar múltiples hoteles simultáneamente
- [x] Debe usar diccionario interno para almacenar hoteles

#### Detalles Tecnicos

**Servicio**: `HotelesService` (`python_hotel/servicios/negocio/hoteles_service.py`)

**Codigo de ejemplo**:
```python
from python_hotel.servicios.negocio.hoteles_service import HotelesService

hoteles_service = HotelesService()

# Agregar hotel
hoteles_service.add_hotel(registro)

# Buscar hotel por ID
hotel = hoteles_service.buscar_hotel(1)
```

**Trazabilidad**: `main.py` linea 225

---

### US-019: Desinfectar Ala Completa

**Como**  supervisor de mantenimiento
**Quiero** desinfectar toda un ala con un desinfectante específico
**Para** controlar gérmenes y garantizar higiene

#### Criterios de Aceptacion

- [x] Debe permitir especificar:
  - ID del hotel a desinfectar
  - Tipo de desinfectante a aplicar
- [x] Debe desinfectar todas las habitaciones del ala
- [x] Debe mostrar mensaje de confirmación
- [x] Si hotel no existe, manejar error apropiadamente

#### Detalles Tecnicos

**Servicio**: `HotelesService.desinfectar()`

**Codigo de ejemplo**:
```python
# Desinfectar hotel ID 1 con desinfectante
hoteles_service.desinfectar(
    id_hotel=1,
    desinfectante="desinfectante orgánico"
)
```

**Salida esperada**:
```
Desinfectando ala con: desinfectante orgánico
```

**Trazabilidad**: `main.py` linea 228

---

### US-020: Realizar Check-out y Empaquetar Habitaciones por Tipo

**Como** encargado de recepción
**Quiero** realizar check-out de todas las habitaciones de un tipo específico y empaquetarlas
**Para**  preparar registros para auditoría

#### Criterios de Aceptacion

- [x] Debe permitir check-out por tipo de habitación (Class type)
- [x] Debe:
  - Buscar todas las habitaciones del tipo especificado
  - Removerlas de todas las alas
  - Empaquetarlas en un Paquete genérico tipo-seguro
  - Mostrar cantidad procesada
- [x] Usar Generics para tipo-seguridad: `Paquete[T]`
- [x] Permitir mostrar contenido de la caja

#### Detalles Tecnicos

**Servicio**: `HotelesService.realizar_checkout_y_empaquetar()`
**Clase**: `Paquete[T]` (`python_hotel/servicios/negocio/paquete.py`)

**Codigo de ejemplo**:
```python
from python_hotel.entidades.habitaciones.habitacion_simple import HabitacionSimple
from python_hotel.entidades.habitaciones.suite import Suite

# Realizar check-out de todas las habitaciones simples
paquete_simples = hoteles_service.realizar_checkout_y_empaquetar(HabitacionSimple)
paquete_simples.mostrar_contenido_caja()

# Realizar check-out de todas las suites
paquete_suites = hoteles_service.realizar_checkout_y_empaquetar(Suite)
paquete_suites.mostrar_contenido_caja()
```

**Salida esperada**:
```
REALIZANDO CHECK-OUT de 5 unidades de <class 'python_hotel.entidades.habitaciones.habitacion_simple.HabitacionSimple'>

Contenido del paquete:
  Tipo: HabitacionSimple
  Cantidad: 5
  ID Paquete: 1

REALIZANDO CHECK-OUT de 2 unidades de <class 'python_hotel.entidades.habitaciones.suite.Suite'>

Contenido del paquete:
  Tipo: Suite
  Cantidad: 2
  ID Paquete: 2
```

**Tipo-seguridad**:
```python
# Paquete es genérico tipo-seguro
paquete_simples: Paquete[HabitacionSimple] = ...
paquete_suites: Paquete[Suite] = ...
```

**Trazabilidad**: `main.py` lineas 232-236

---

## Epic 6: Persistencia y Auditoria

### US-021:  Persistir Registro Hotelero en Disco

**Como** administrador del sistema
**Quiero** guardar registros hoteleros en disco
**Para** mantener datos permanentes entre ejecuciones

#### Criterios de Aceptacion

- [x] El sistema debe:
  - Serializar RegistroHotelero completo con Pickle
  - Guardar en directorio `data/`
  - Nombre de archivo: `{propietario}.dat`
  - Crear directorio si no existe
  - Mostrar mensaje de confirmacion
- [x] Si ocurre error, lanzar `PersistenciaException`
- [x] Cerrar recursos apropiadamente en bloque finally

#### Detalles Tecnicos

**Servicio**: `RegistroHoteleroService.persistir()`

**Codigo de ejemplo**:
```python
from python_hotel.servicios.hotel.registro_hotelero_service import RegistroHoteleroService

registro_service = RegistroHoteleroService()

# Persistir registro
registro_service.persistir(registro)
# Crea: data/Carlos Rodríguez.dat
```

**Salida esperada**:
```
Registro de Carlos Rodríguez persistido exitosamente en data/Carlos Rodríguez.dat
```

**Constantes**:
```python
DIRECTORIO_DATA = "data"
EXTENSION_DATA = ".dat"
```

**Manejo de errores**:
```python
try:
    registro_service.persistir(registro)
except PersistenciaException as e:
    print(e.get_user_message())
    print(f"Archivo: {e.get_nombre_archivo()}")
    print(f"Operación: {e.get_tipo_operacion().value}")
```

**Trazabilidad**: `main.py` linea 242, 

---

### US-022:  Recuperar Registro Hotelero desde Disco

**Como** auditor
**Quiero** recuperar registros  hoteleros guardados previamente
**Para** consultar historicos y realizar auditorias

#### Criterios de Aceptacion

- [x] El sistema debe:
  - Deserializar archivo `.dat` con Pickle
  - Buscar en directorio `data/`
  - Validar que propietario no sea nulo/vacio
  - Retornar RegistroHotelero completo
  - Mostrar mensaje de confirmacion
- [x] Si archivo no existe, lanzar `PersistenciaException`
- [x] Si archivo corrupto, lanzar `PersistenciaException`
- [x] Cerrar recursos apropiadamente en bloque finally

#### Detalles Tecnicos

**Servicio**: `RegistroHoteleroService.leer_registro()` (metodo estatico)

**Codigo de ejemplo**:
```python
## Leer registro persistido
registro_leido = RegistroHoteleroService.leer_registro("Carlos Rodríguez")

# Mostrar datos recuperados
registro_service.mostrar_datos(registro_leido)
```

**Salida esperada**:
```
Registro de Carlos Rodríguez recuperado exitosamente desde data/Carlos Rodríguez.dat

REGISTRO HOTELERO
=================
Hotel ID:      1
Propietario:   Carlos Rodríguez
Avalúo:        15000000.75
...
```

**Validaciones**:
```python
# Propietario vacío
try:
    RegistroHoteleroService.leer_registro("")
except ValueError as e:
    print("El nombre del propietario no puede ser nulo o vacío")

# Archivo no existe
try:
    RegistroHoteleroService.leer_registro("NoExiste")
except PersistenciaException as e:
    print(f"Archivo no encontrado: {e.get_nombre_archivo()}")
```

**Trazabilidad**: `main.py` lineas 246-247, 

---

### US-023: Mostrar Datos Completos de Registro Hotelero

**Como** auditor
**Quiero** ver todos los datos de un registro hotelero en formato legible
**Para** analizar la información completa de un hotel

#### Criterios de Aceptacion

- [x] El sistema debe mostrar:
  - Encabezado "REGISTRO HOTELERO"
  - ID de hotel
  - Propietario
  - Avaluo fiscal
  - Dirección del hotel
  - Capacidad del hotel
  - Cantidad de habitaciones configuradas
  - Listado detallado de cada habitación
- [x] CCada habitación debe mostrarse con datos específicos de su tipo
- [x] Usar Registry para dispatch polimorfico

#### Detalles Tecnicos

**Servicio**: `RegistroHoteleroService.mostrar_datos()`

**Codigo de ejemplo**:
```python
# Mostrar registro completo
registro_service.mostrar_datos(registro)
```

**Salida esperada**:
```
REGISTRO HOTELERO
=================
Hotel ID:      1
Propietario:   Carlos Rodríguez
Avalúo:        15000000.75
Dirección:     Av. Principal 123, Ciudad
Capacidad:     100
Cantidad de habitaciones configuradas: 26
Listado de Habitaciones configuradas
____________________________________

Habitación: Simple
Capacidad: 1 persona
Tarifa base: 50.0 USD
ID: 1
Estado: Disponible

Habitación: Doble
Capacidad: 2 personas
Tarifa base: 80.0 USD
Servicios: Desayuno incluido
Estado: Disponible

...
```

**Trazabilidad**: `main.py` linea 247, 

---

## Historias Tecnicas (Patrones de Diseno)

### US-TECH-001: Implementar Singleton para HabitacionServiceRegistry

**Como** arquitecto de software
**Quiero** garantizar una unica instancia del registro de servicios
**Para** compartir estado consistente entre todos los servicios

#### Criterios de Aceptacion

- [x] Implementar patron Singleton thread-safe
- [x] Usar double-checked locking con Lock
- [x] Inicializacion perezosa (lazy initialization)
- [x] Metodo `get_instance()` para acceso
- [x] Constructor `__new__` para controlar instanciacion
- [x] NO permitir multiples instancias

#### Detalles Tecnicos

**Clase**: `HabitacionServiceRegistry`
**Patron**: Singleton

**Implementacion**:
```python
from threading import Lock

class HabitacionServiceRegistry:
    _instance = None
    _lock = Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:  # Thread-safe
                if cls._instance is None:  # Double-checked
                    cls._instance = super().__new__(cls)
                    # Inicializar servicios una sola vez
                    cls._instance._inicializar_servicios()
        return cls._instance

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls()
        return cls._instance
```

**Uso**:
```python
# Opcion 1: Instanciacion directa
# Opcion 1: Instanciacion directa
registry = HabitacionServiceRegistry()

# Opcion 2: Metodo get_instance()
registry = HabitacionServiceRegistry.get_instance()

# Ambas retornan la MISMA instancia
assert registry is HabitacionServiceRegistry.get_instance()
```

**Trazabilidad**: `python_hotel/servicios/habitaciones/habitacion_service_registry.py` lineas 20-46

---

### US-TECH-002: Implementar Factory Method para Creacion de Habitacioness

**Como** arquitecto de software
**Quiero** centralizar creacion de habitaciones mediante Factory Method
**Para** desacoplar cliente de clases concretas de habitaciones

#### Criterios de Aceptacion


[x] Crear clase HabitacionFactory con método estático

[x] Soportar creación de: Simple, Doble, Suite, Presidencial

[x] Usar diccionario de factories (no if/elif cascades)

[x] Lanzar ValueError si el tipo de habitación es desconocido

[x] Retornar tipo base Habitacion (no tipos concretos)

[x] NO usar lambdas - usar métodos estáticos dedicados

#### Detalles Tecnicos

**Clase**: `HabitacionFactory`
**Patron**: Factory Method

**Implementacion**:
```python
class HabitacionFactory:
    @staticmethod
    def crear_habitacion(tipo: str) -> Habitacion:
        factories = {
            "Simple": HabitacionFactory._crear_simple,
            "Doble": HabitacionFactory._crear_doble,
            "Suite": HabitacionFactory._crear_suite,
            "Presidencial": HabitacionFactory._crear_presidencial
        }

        if tipo not in factories:
            raise ValueError(f"Tipo de habitación desconocido: {tipo}")

        return factories[tipo]()

    @staticmethod
    def _crear_simple() -> HabitacionSimple:
        from python_hotel.entidades.habitaciones.habitacion_simple import HabitacionSimple
        return HabitacionSimple(servicios_basicos=True)

    # ... otros metodos _crear_*
```

**Uso**:
```python
ffrom python_hotel.patrones.factory.habitacion_factory import HabitacionFactory

# Cliente NO conoce clases concretas
habitacion = HabitacionFactory.crear_habitacion("Simple")
# Retorna Habitacion (interfaz), no HabitacionSimple (concreto)
```

**Trazabilidad**: `python_hotel/patrones/factory/habitacion_factory.py` lineas 8-67

---

### US-TECH-003: Implementar Observer Pattern para Sensores

**Como** arquitecto de software
**Quiero** implementar patron Observer con Generics
**Para** notificar cambios de sensores(ocupacion, limpieza) de forma tipo-segura

#### Criterios de Aceptacion

[x] Crear clase Observable[T] genérica

[x] Crear interfaz Observer[T] genérica

[x] Soportar múltiples observadores

[x] Métodos: agregar_observador(), eliminar_observador(), notificar_observadores()

[x] Sensores (OcupacionReaderTask, LimpiezaReaderTask) heredan de Observable[float]

[x] Controlador (ControlLimpiezaTask) hereda de Observer[float]

[x] Thread-safe en notificaciones (implícito en la simplicidad de la lista)

#### Detalles Tecnicos

**Clases**: `Observable[T]`, `Observer[T]`
**Patron**: Observer

**Implementacion**:
```python
from typing import Generic, TypeVar, List
from abc import ABC, abstractmethod

T = TypeVar('T')

class Observer(Generic[T], ABC):
    @abstractmethod
    def actualizar(self, evento: T) -> None:
        pass

class Observable(Generic[T], ABC):
    def __init__(self):
        self._observadores: List[Observer[T]] = []

    def agregar_observador(self, observador: Observer[T]) -> None:
        if observador not in self._observadores:
            self._observadores.append(observador)

    def notificar_observadores(self, evento: T) -> None:
        for observador in self._observadores:
            observador.actualizar(evento)
```

**Uso**:
```python
# Sensor es Observable[float]
class OcupacionReaderTask(threading.Thread, Observable[float]):
    def run(self):
        while not self._detenido.is_set():
            ocupacion = self._leer_ocupacion()
            self.notificar_observadores(ocupacion)  # Notifica float

# Controlador es Observer[float]
class ControlLimpiezaTask(Observer[float]):
    def actualizar(self, evento: float) -> None:
        # Recibe la notificación (puede ser de ocupación o limpieza)
        # El controlador decide cómo manejar el float
        pass
```

**Trazabilidad**: `python_hotel/patrones/observer/observable.py, observer.py`

---

### US-TECH-004: Implementar Strategy Pattern para Mantenimiento
**Como** arquitecto de software
**Quiero** implementar algoritmos intercambiables de mantenimiento
**Para** permitir diferentes estrategias segun tipo de habitación (Estándar vs. Premium)

#### Criterios de Aceptacion

[x] Crear interfaz MantenimientoStrategy abstracta

[x] Implementar MantenimientoEstandarStrategy (habitaciones estándar)

[x] Implementar MantenimientoPremiumStrategy (suites)

[x] Inyectar estrategia en constructor de servicios de habitación

[x] Servicios delegan cálculo de mantenimiento a la estrategia

[x] Estrategias usan constantes de constantes.py

#### Detalles Tecnicos

**Interfaz**: `MantenimientoStrategy`
**Implementaciones**: `MantenimientoEstandarStrategy`, `AMantenimientoPremiumStrategy`
**Patron**: Strategy

**Implementacion**:
```python
# Interfaz
class MantenimientoStrategy(ABC):
    @abstractmethod
    def calcular_mantenimiento(
        self,
        fecha: date,
        ocupacion: float,
        habitacion: 'Habitacion'
    ) -> int:
        pass

# Estrategia 1: Estandar
class MantenimientoEstandarStrategy(MantenimientoStrategy):
    def calcular_mantenimiento(self, fecha, ocupacion, habitacion):
        if ocupacion < 0.3: # Baja ocupación
            return MANTENIMIENTO_ESTANDAR_COMPLETO # 60 min
        else:
            return MANTENIMIENTO_ESTANDAR_BASICO # 30 min

# Estrategia 2: Premium
class MantenimientoPremiumStrategy(MantenimientoStrategy):
    def __init__(self, tiempo_constante: int):
        self._tiempo = tiempo_constante

    def calcular_mantenimiento(self, fecha, ocupacion, habitacion):
        return self._tiempo # Siempre el mismo tiempo (ej. 90 min)
```

**Inyeccion**:
```python
class HabitacionSimpleService(HabitacionService):
    def __init__(self):
        super().__init__(MantenimientoEstandarStrategy())  # Inyeccion

class SuitePresidencialService(HabitacionService):
    def __init__(self):
        super().__init__(MantenimientoPremiumStrategy(90))  # Inyeccion
```

**Delegacion**:
```python
class HabitacionService(ABC):
    def realizar_mantenimiento(self, habitacion: 'Habitacion') -> int:
        # Delegar a estrategia
        tiempo_mantenimiento = self._estrategia_mantenimiento.calcular_mantenimiento(
            fecha, ocupacion, habitacion
        )
        habitacion.set_estado("En Mantenimiento")
        return tiempo_mantenimiento
```

**Trazabilidad**: `python_hotel/patrones/strategy/impl/mantenimiento_estandar_strategy.py, mantenimiento_premium_strategy.py` lineas 35-59

---

### US-TECH-005: Implementar Registry Pattern para Dispatch Polimórfico

**Como** arquitecto de software
**Quiero** eliminar cascadas de isinstance() al operar sobre habitaciones
**Para** mejorar mantenibilidad y extensibilidad

#### Criterios de Aceptacion

[x] Crear diccionarios de handlers por tipo de habitación

[x] Registrar un handler para cada tipo (Simple, Doble, Suite, Presidencial)

[x] Método realizar_mantenimiento() usa dispatch automático

[x] Método mostrar_datos_especificos() usa dispatch automático

[x] Lanzar error si el tipo de habitación no está registrado

[x] NO usar lambdas - usar métodos de instancia dedicados

#### Detalles Tecnicos

**Clase**: `HabitacionServiceRegistry`
**Patron**: Registry

**Implementacion**:
```python
class HabitacionServiceRegistry:
    def __init__(self):
        # Diccionarios de handlers
        self._mantenimiento_handlers = {
            HabitacionSimple: self._mantenimiento_simple,
            HabitacionDoble: self._mantenimiento_doble,
            Suite: self._mantenimiento_suite,
            SuitePresidencial: self._mantenimiento_presidencial
        }

        self._mostrar_datos_handlers = {
            HabitacionSimple: self._mostrar_datos_simple,
            HabitacionDoble: self._mostrar_datos_doble,
            # ... etc
        }

    def realizar_mantenimiento(self, habitacion: Habitacion) -> int:
        tipo = type(habitacion)
        if tipo not in self._mantenimiento_handlers:
            raise ValueError(f"Tipo de habitación desconocido: {tipo}")
        return self._mantenimiento_handlers[tipo](habitacion)

    # Handlers dedicados (NO lambdas)
    def _mantenimiento_simple(self, habitacion):
        return self._simple_service.realizar_mantenimiento(habitacion)
```

**Ventajas**:
- Sin `isinstance()` cascades
- Facil agregar nuevos tipos de habitacion
- Mejor rendimiento (O(1) lookup)
- Mas testeable

**Trazabilidad**: `python_hotel/servicios/habitaciones/habitacion_service_registry.py` lineas 48-89

---

## Resumen de Cobertura Funcional

### Totales por Epic

| Epic | Historias | Completadas | Cobertura |
|------|-----------|-------------|-----------|
| Epic 1: gestion hoteles y alas | 3 | 3 | 100% |
| Epic 2: Gestion de habitaciones | 6 | 6 | 100% |
| Epic 3: Sistema de limpieza Automatizado | 4 | 4 | 100% |
| Epic 4: Gestion de Personal | 4 | 4 | 100% |
| Epic 5: Operaciones de Negocio | 3 | 3 | 100% |
| Epic 6: Persistencia y Auditoria | 3 | 3 | 100% |
| Historias Tecnicas (Patrones) | 5 | 5 | 100% |
| **TOTAL** | **28** | **28** | **100%** |

### Patrones de Diseno Cubiertos

- [x] SINGLETON - HabitacionesServiceRegistry
- [x] FACTORY METHOD - HabitacionFactory
- [x] OBSERVER - Sensores (ocupacion,limpieza) y controlador
- [x] STRATEGY - MantenimientoStrategy (estandar,premiun)
- [x] REGISTRY - Dispatch polimorfico HabitacionServiceResgistry

### Funcionalidades Completas

-[x] Gestión de 4 tipos de habitaciones

[x] Sistema de limpieza automatizado con 3 threads

[x] Gestión de empleados con certificación profesional

[x] Persistencia con Pickle

[x] Operaciones de negocio de alto nivel (check-out, desinfección)

[x] Manejo de excepciones específicas

[x] PEP 8 compliance 100%

[x] Type hints con TYPE_CHECKING

[x] Constantes centralizadas

[x] Código limpio sin lambdas

---

**Ultima actualizacion**: Noviembre 2025
**Estado**: COMPLETO
**Cobertura funcional**: 100%