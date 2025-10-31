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

**Crecimiento**:
```python
# Pino: +0.10m por riego
# Olivo: +0.01m por riego
```

**Trazabilidad**: `plantacion_service.py` lineas 82-129

---

### US-009: Mostrar Datos de Cultivos por Tipo

**Como** administrador de finca
**Quiero** ver los datos de cada cultivo de forma especifica
**Para** conocer el estado actual de mis plantaciones

#### Criterios de Aceptacion

- [x] El sistema debe mostrar datos especificos por tipo:
  - **Pino**: Cultivo, Superficie, Agua, ID, Altura, Variedad
  - **Olivo**: Cultivo, Superficie, Agua, ID, Altura, Tipo de aceituna
  - **Lechuga**: Cultivo, Superficie, Agua, Variedad, Invernadero
  - **Zanahoria**: Cultivo, Superficie, Agua, Es baby carrot
- [x] Usar el patron Registry para dispatch polimorfico
- [x] NO usar cascadas de isinstance()

#### Detalles Tecnicos

**Registry**: `CultivoServiceRegistry.mostrar_datos()`

**Codigo de ejemplo**:
```python
from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry

registry = CultivoServiceRegistry.get_instance()

for cultivo in plantacion.get_cultivos():
    registry.mostrar_datos(cultivo)
    # Despacho automatico al servicio correcto
```

**Salida ejemplo (Pino)**:
```
Cultivo: Pino
Superficie: 2.0 m²
Agua almacenada: 7 L
ID: 1
Altura: 1.2 m
Variedad: Parana
```

**Trazabilidad**: `cultivo_service_registry.py` lineas 78-89

---

## Epic 3: Sistema de Riego Automatizado

### US-010: Monitorear Temperatura en Tiempo Real

**Como** sistema de riego automatizado
**Quiero** leer la temperatura ambiental cada 2 segundos
**Para** tomar decisiones de riego basadas en condiciones reales

#### Criterios de Aceptacion

- [x] El sensor debe:
  - Ejecutarse en un thread daemon separado
  - Leer temperatura cada 2 segundos (configurable)
  - Generar lecturas aleatorias entre -25C y 50C
  - Notificar a observadores cada vez que lee
  - Soportar detencion graceful con timeout
- [x] Implementar patron Observer (Observable)
- [x] Usar Generics para tipo-seguridad: `Observable[float]`

#### Detalles Tecnicos

**Clase**: `TemperaturaReaderTask` (`python_forestacion/riego/sensores/temperatura_reader_task.py`)
**Patron**: Observer (Observable[float])

**Codigo de ejemplo**:
```python
from python_forestacion.riego.sensores.temperatura_reader_task import TemperaturaReaderTask

# Crear sensor (thread daemon)
tarea_temp = TemperaturaReaderTask()

# Iniciar lectura continua
tarea_temp.start()

# Detener cuando sea necesario
tarea_temp.detener()
tarea_temp.join(timeout=2.0)
```

**Constantes**:
```python
INTERVALO_SENSOR_TEMPERATURA = 2.0  # segundos
SENSOR_TEMP_MIN = -25  # °C
SENSOR_TEMP_MAX = 50  # °C
```

**Eventos generados**:
```python
# Cada lectura notifica valor float a observadores
temperatura: float = 22.5
self.notificar_observadores(temperatura)
```

**Trazabilidad**: `main.py` lineas 158-166

---

### US-011: Monitorear Humedad en Tiempo Real

**Como** sistema de riego automatizado
**Quiero** leer la humedad ambiental cada 3 segundos
**Para** complementar datos de temperatura en decisiones de riego

#### Criterios de Aceptacion

- [x] El sensor debe:
  - Ejecutarse en un thread daemon separado
  - Leer humedad cada 3 segundos (configurable)
  - Generar lecturas aleatorias entre 0% y 100%
  - Notificar a observadores cada vez que lee
  - Soportar detencion graceful con timeout
- [x] Implementar patron Observer (Observable)
- [x] Usar Generics para tipo-seguridad: `Observable[float]`

#### Detalles Tecnicos

**Clase**: `HumedadReaderTask` (`python_forestacion/riego/sensores/humedad_reader_task.py`)
**Patron**: Observer (Observable[float])

**Codigo de ejemplo**:
```python
from python_forestacion.riego.sensores.humedad_reader_task import HumedadReaderTask

# Crear sensor (thread daemon)
tarea_hum = HumedadReaderTask()

# Iniciar lectura continua
tarea_hum.start()

# Detener cuando sea necesario
tarea_hum.detener()
tarea_hum.join(timeout=2.0)
```

**Constantes**:
```python
INTERVALO_SENSOR_HUMEDAD = 3.0  # segundos
SENSOR_HUMEDAD_MIN = 0  # %
SENSOR_HUMEDAD_MAX = 100  # %
```

**Trazabilidad**: `main.py` lineas 158-166

---

### US-012: Control Automatico de Riego Basado en Sensores

**Como** sistema de riego automatizado
**Quiero** regar automaticamente cuando se cumplan condiciones ambientales
**Para** optimizar el uso de agua segun necesidades reales

#### Criterios de Aceptacion

- [x] El controlador debe:
  - Ejecutarse en un thread daemon separado
  - Evaluar condiciones cada 2.5 segundos
  - Observar sensores de temperatura y humedad
  - Regar cuando:
    - Temperatura entre 8C y 15C, Y
    - Humedad menor a 50%
  - NO regar si condiciones no se cumplen
  - Manejar excepcion si no hay agua disponible
- [x] Implementar patron Observer (Observer[float])
- [x] Recibir sensores via inyeccion de dependencias

#### Detalles Tecnicos

**Clase**: `ControlRiegoTask` (`python_forestacion/riego/control/control_riego_task.py`)
**Patron**: Observer (observa sensores)

**Codigo de ejemplo**:
```python
from python_forestacion.riego.control.control_riego_task import ControlRiegoTask

# Inyectar dependencias
tarea_control = ControlRiegoTask(
    sensor_temperatura=tarea_temp,
    sensor_humedad=tarea_hum,
    plantacion=plantacion,
    plantacion_service=plantacion_service
)

# Iniciar control automatico
tarea_control.start()

# Detener cuando sea necesario
tarea_control.detener()
tarea_control.join(timeout=2.0)
```

**Logica de decision**:
```python
if (TEMP_MIN_RIEGO <= temperatura <= TEMP_MAX_RIEGO) and (humedad < HUMEDAD_MAX_RIEGO):
    # REGAR
    plantacion_service.regar(plantacion)
else:
    # NO REGAR
    pass
```

**Constantes de riego**:
```python
TEMP_MIN_RIEGO = 8  # °C
TEMP_MAX_RIEGO = 15  # °C
HUMEDAD_MAX_RIEGO = 50  # %
INTERVALO_CONTROL_RIEGO = 2.5  # segundos
```

**Trazabilidad**: `main.py` lineas 160-166, `control_riego_task.py` lineas 67-91

---

### US-013: Detener Sistema de Riego de Forma Segura

**Como** administrador del sistema
**Quiero** detener el sistema de riego de forma controlada
**Para** evitar corrupcion de datos o procesos incompletos

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
from python_forestacion.constantes import THREAD_JOIN_TIMEOUT

# Detener sensores y control
tarea_temp.detener()
tarea_hum.detener()
tarea_control.detener()

# Esperar finalizacion con timeout
tarea_temp.join(timeout=THREAD_JOIN_TIMEOUT)  # 2s
tarea_hum.join(timeout=THREAD_JOIN_TIMEOUT)
tarea_control.join(timeout=THREAD_JOIN_TIMEOUT)

# Si timeout expira, threads daemon finalizan automaticamente
```

**Constantes**:
```python
THREAD_JOIN_TIMEOUT = 2.0  # segundos
```

**Trazabilidad**: `main.py` lineas 256-263

---

## Epic 4: Gestion de Personal

### US-014: Registrar Trabajador con Tareas Asignadas

**Como** jefe de personal
**Quiero** registrar trabajadores con sus tareas asignadas
**Para** organizar el trabajo agricola

#### Criterios de Aceptacion

- [x] Un trabajador debe tener:
  - DNI unico (numero entero)
  - Nombre completo
  - Lista de tareas asignadas (puede estar vacia)
  - Apto medico (inicialmente sin apto)
- [x] Las tareas deben tener:
  - ID unico
  - Fecha programada
  - Descripcion de la tarea
  - Estado (pendiente/completada)
- [x] Un trabajador puede tener multiples tareas
- [x] Lista de trabajadores es inmutable (defensive copy)

#### Detalles Tecnicos

**Clases**:
- `Trabajador` (`python_forestacion/entidades/personal/trabajador.py`)
- `Tarea` (`python_forestacion/entidades/personal/tarea.py`)

**Codigo de ejemplo**:
```python
from python_forestacion.entidades.personal.trabajador import Trabajador
from python_forestacion.entidades.personal.tarea import Tarea
from datetime import date

# Crear tareas
tareas = [
    Tarea(1, date.today(), "Desmalezar"),
    Tarea(2, date.today(), "Abonar"),
    Tarea(3, date.today(), "Marcar surcos")
]

# Crear trabajador
trabajador = Trabajador(
    dni=43888734,
    nombre="Juan Perez",
    tareas=tareas
)
```

**Trazabilidad**: `main.py` lineas 176-185

---

### US-015: Asignar Apto Medico a Trabajador

**Como** medico laboral
**Quiero** asignar un apto medico a un trabajador
**Para** certificar que esta apto para trabajar

#### Criterios de Aceptacion

- [x] Un apto medico debe tener:
  - Estado de aptitud (True/False)
  - Fecha de emision
  - Observaciones medicas (opcional)
- [x] El sistema debe verificar apto antes de trabajar
- [x] Si no tiene apto valido, no puede ejecutar tareas
- [x] El servicio debe permitir asignar/actualizar apto

#### Detalles Tecnicos

**Clase**: `AptoMedico` (`python_forestacion/entidades/personal/apto_medico.py`)
**Servicio**: `TrabajadorService.asignar_apto_medico()`

**Codigo de ejemplo**:
```python
from python_forestacion.servicios.personal.trabajador_service import TrabajadorService
from datetime import date

trabajador_service = TrabajadorService()

# Asignar apto medico
trabajador_service.asignar_apto_medico(
    trabajador=trabajador,
    apto=True,
    fecha_emision=date.today(),
    observaciones="Estado de salud: excelente"
)

# Verificar apto
if trabajador.get_apto_medico().esta_apto():
    print("Trabajador apto para trabajar")
else:
    print("Trabajador NO apto")
```

**Trazabilidad**: `main.py` lineas 191-196

---

### US-016: Ejecutar Tareas Asignadas a Trabajador

**Como** trabajador agricola
**Quiero** ejecutar las tareas que me fueron asignadas
**Para** completar mi jornada laboral

#### Criterios de Aceptacion

- [x] El trabajador debe:
  - Tener apto medico valido
  - Ejecutar solo tareas de la fecha especificada
  - Usar una herramienta asignada
  - Marcar tareas como completadas
- [x] Las tareas deben ejecutarse en orden ID descendente
- [x] Si no tiene apto medico, retornar False (no ejecuta)
- [x] Si tiene apto medico, retornar True (ejecuta)

#### Detalles Tecnicos

**Servicio**: `TrabajadorService.trabajar()`
**Clase**: `Herramienta` (`python_forestacion/entidades/personal/herramienta.py`)

**Codigo de ejemplo**:
```python
from python_forestacion.entidades.personal.herramienta import Herramienta

# Crear herramienta
herramienta = Herramienta(
    id_herramienta=1,
    nombre="Pala",
    certificado_hys=True
)

# Ejecutar tareas
resultado = trabajador_service.trabajar(
    trabajador=trabajador,
    fecha=date.today(),
    util=herramienta
)

if resultado:
    print("Tareas ejecutadas exitosamente")
else:
    print("No puede trabajar - sin apto medico")
```

**Salida esperada**:
```
El trabajador Juan Perez realizo la tarea 3 Marcar surcos con herramienta: Pala
El trabajador Juan Perez realizo la tarea 2 Abonar con herramienta: Pala
El trabajador Juan Perez realizo la tarea 1 Desmalezar con herramienta: Pala
```

**Ordenamiento**:
```python
# Tareas se ordenan por ID descendente (3, 2, 1)
# Usa metodo estatico _obtener_id_tarea() en lugar de lambda
```

**Trazabilidad**: `main.py` lineas 199-204, `trabajador_service.py` lineas 34-72

---

### US-017: Asignar Trabajadores a Plantacion

**Como** jefe de personal
**Quiero** asignar trabajadores a una plantacion especifica
**Para** organizar el personal por finca

#### Criterios de Aceptacion

- [x] Una plantacion debe poder tener multiples trabajadores
- [x] La lista de trabajadores debe ser inmutable (defensive copy)
- [x] Debe poder obtener lista de trabajadores
- [x] Debe poder reemplazar lista completa de trabajadores

#### Detalles Tecnicos

**Clase**: `Plantacion.set_trabajadores()`

**Codigo de ejemplo**:
```python
trabajadores = [
    Trabajador(43888734, "Juan Perez", tareas.copy()),
    Trabajador(40222333, "Maria Lopez", tareas.copy())
]

# Asignar trabajadores a plantacion
plantacion.set_trabajadores(trabajadores)

# Obtener trabajadores (copia inmutable)
lista_trabajadores = plantacion.get_trabajadores()
```

**Trazabilidad**: `main.py` linea 187

---

## Epic 5: Operaciones de Negocio

### US-018: Gestionar Multiples Fincas

**Como** propietario de multiples fincas
**Quiero** gestionar varias fincas desde un servicio centralizado
**Para** tener control unificado de todas mis propiedades

#### Criterios de Aceptacion

- [x] El servicio debe permitir:
  - Agregar fincas (RegistroForestal)
  - Buscar finca por ID de padron
  - Fumigar una finca especifica
  - Cosechar y empaquetar por tipo de cultivo
- [x] Debe manejar multiples fincas simultaneamente
- [x] Debe usar diccionario interno para almacenar fincas

#### Detalles Tecnicos

**Servicio**: `FincasService` (`python_forestacion/servicios/negocio/fincas_service.py`)

**Codigo de ejemplo**:
```python
from python_forestacion.servicios.negocio.fincas_service import FincasService

fincas_service = FincasService()

# Agregar finca
fincas_service.add_finca(registro)

# Buscar finca por padron
finca = fincas_service.buscar_finca(1)
```

**Trazabilidad**: `main.py` linea 225

---

### US-019: Fumigar Plantacion Completa

**Como** tecnico agricola
**Quiero** fumigar toda una plantacion con un plaguicida especifico
**Para** controlar plagas y enfermedades

#### Criterios de Aceptacion

- [x] Debe permitir especificar:
  - ID de padron de la finca a fumigar
  - Tipo de plaguicida a aplicar
- [x] Debe fumigar todos los cultivos de la plantacion
- [x] Debe mostrar mensaje de confirmacion
- [x] Si finca no existe, manejar error apropiadamente

#### Detalles Tecnicos

**Servicio**: `FincasService.fumigar()`

**Codigo de ejemplo**:
```python
# Fumigar finca ID 1 con insecticida
fincas_service.fumigar(
    id_padron=1,
    plaguicida="insecto organico"
)
```

**Salida esperada**:
```
Fumigando plantacion con: insecto organico
```

**Trazabilidad**: `main.py` linea 228

---

### US-020: Cosechar y Empaquetar Cultivos por Tipo

**Como** encargado de cosecha
**Quiero** cosechar todos los cultivos de un tipo especifico y empaquetarlos
**Para** preparar productos para venta

#### Criterios de Aceptacion

- [x] Debe permitir cosechar por tipo de cultivo (Class type)
- [x] Debe:
  - Buscar todos los cultivos del tipo especificado
  - Removerlos de todas las plantaciones
  - Empaquetarlos en un Paquete generico tipo-seguro
  - Mostrar cantidad cosechada
- [x] Usar Generics para tipo-seguridad: `Paquete[T]`
- [x] Permitir mostrar contenido de la caja

#### Detalles Tecnicos

**Servicio**: `FincasService.cosechar_yempaquetar()`
**Clase**: `Paquete[T]` (`python_forestacion/servicios/negocio/paquete.py`)

**Codigo de ejemplo**:
```python
from python_forestacion.entidades.cultivos.lechuga import Lechuga
from python_forestacion.entidades.cultivos.pino import Pino

# Cosechar todas las lechugas
caja_lechugas = fincas_service.cosechar_yempaquetar(Lechuga)
caja_lechugas.mostrar_contenido_caja()

# Cosechar todos los pinos
caja_pinos = fincas_service.cosechar_yempaquetar(Pino)
caja_pinos.mostrar_contenido_caja()
```

**Salida esperada**:
```
COSECHANDO 5 unidades de <class 'python_forestacion.entidades.cultivos.lechuga.Lechuga'>

Contenido de la caja:
  Tipo: Lechuga
  Cantidad: 5
  ID Paquete: 1

COSECHANDO 5 unidades de <class 'python_forestacion.entidades.cultivos.pino.Pino'>

Contenido de la caja:
  Tipo: Pino
  Cantidad: 5
  ID Paquete: 2
```

**Tipo-seguridad**:
```python
# Paquete es generico tipo-seguro
caja_lechugas: Paquete[Lechuga] = ...
caja_pinos: Paquete[Pino] = ...
```

**Trazabilidad**: `main.py` lineas 232-236

---

## Epic 6: Persistencia y Auditoria

### US-021: Persistir Registro Forestal en Disco

**Como** administrador del sistema
**Quiero** guardar registros forestales en disco
**Para** mantener datos permanentes entre ejecuciones

#### Criterios de Aceptacion

- [x] El sistema debe:
  - Serializar RegistroForestal completo con Pickle
  - Guardar en directorio `data/`
  - Nombre de archivo: `{propietario}.dat`
  - Crear directorio si no existe
  - Mostrar mensaje de confirmacion
- [x] Si ocurre error, lanzar `PersistenciaException`
- [x] Cerrar recursos apropiadamente en bloque finally

#### Detalles Tecnicos

**Servicio**: `RegistroForestalService.persistir()`

**Codigo de ejemplo**:
```python
from python_forestacion.servicios.terrenos.registro_forestal_service import RegistroForestalService

registro_service = RegistroForestalService()

# Persistir registro
registro_service.persistir(registro)
# Crea: data/Juan Perez.dat
```

**Salida esperada**:
```
Registro de Juan Perez persistido exitosamente en data/Juan Perez.dat
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
    print(f"Operacion: {e.get_tipo_operacion().value}")
```

**Trazabilidad**: `main.py` linea 242, `registro_forestal_service.py` lineas 62-112

---

### US-022: Recuperar Registro Forestal desde Disco

**Como** auditor
**Quiero** recuperar registros forestales guardados previamente
**Para** consultar historicos y realizar auditorias

#### Criterios de Aceptacion

- [x] El sistema debe:
  - Deserializar archivo `.dat` con Pickle
  - Buscar en directorio `data/`
  - Validar que propietario no sea nulo/vacio
  - Retornar RegistroForestal completo
  - Mostrar mensaje de confirmacion
- [x] Si archivo no existe, lanzar `PersistenciaException`
- [x] Si archivo corrupto, lanzar `PersistenciaException`
- [x] Cerrar recursos apropiadamente en bloque finally

#### Detalles Tecnicos

**Servicio**: `RegistroForestalService.leer_registro()` (metodo estatico)

**Codigo de ejemplo**:
```python
# Leer registro persistido
registro_leido = RegistroForestalService.leer_registro("Juan Perez")

# Mostrar datos recuperados
registro_service.mostrar_datos(registro_leido)
```

**Salida esperada**:
```
Registro de Juan Perez recuperado exitosamente desde data/Juan Perez.dat

REGISTRO FORESTAL
=================
Padron:      1
Propietario: Juan Perez
Avaluo:      50309233.55
...
```

**Validaciones**:
```python
# Propietario vacio
try:
    RegistroForestalService.leer_registro("")
except ValueError as e:
    print("El nombre del propietario no puede ser nulo o vacio")

# Archivo no existe
try:
    RegistroForestalService.leer_registro("NoExiste")
except PersistenciaException as e:
    print(f"Archivo no encontrado: {e.get_nombre_archivo()}")
```

**Trazabilidad**: `main.py` lineas 246-247, `registro_forestal_service.py` lineas 114-171

---

### US-023: Mostrar Datos Completos de Registro Forestal

**Como** auditor
**Quiero** ver todos los datos de un registro forestal en formato legible
**Para** analizar la informacion completa de una finca

#### Criterios de Aceptacion

- [x] El sistema debe mostrar:
  - Encabezado "REGISTRO FORESTAL"
  - Padron catastral
  - Propietario
  - Avaluo fiscal
  - Domicilio del terreno
  - Superficie del terreno
  - Cantidad de cultivos plantados
  - Listado detallado de cada cultivo
- [x] Cada cultivo debe mostrarse con datos especificos de su tipo
- [x] Usar Registry para dispatch polimorfico

#### Detalles Tecnicos

**Servicio**: `RegistroForestalService.mostrar_datos()`

**Codigo de ejemplo**:
```python
# Mostrar registro completo
registro_service.mostrar_datos(registro)
```

**Salida esperada**:
```
REGISTRO FORESTAL
=================
Padron:      1
Propietario: Juan Perez
Avaluo:      50309233.55
Domicilio:   Agrelo, Mendoza
Superficie: 10000.0
Cantidad de cultivos plantados: 20
Listado de Cultivos plantados
____________________________

Cultivo: Pino
Superficie: 2.0 m²
Agua almacenada: 7 L
ID: 1
Altura: 1.2 m
Variedad: Parana

Cultivo: Olivo
Superficie: 3.0 m²
Agua almacenada: 9 L
ID: 2
Altura: 0.52 m
Tipo de aceituna: Arbequina

...
```

**Trazabilidad**: `main.py` linea 247, `registro_forestal_service.py` lineas 28-60

---

## Historias Tecnicas (Patrones de Diseno)

### US-TECH-001: Implementar Singleton para CultivoServiceRegistry

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

**Clase**: `CultivoServiceRegistry`
**Patron**: Singleton

**Implementacion**:
```python
from threading import Lock

class CultivoServiceRegistry:
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
registry = CultivoServiceRegistry()

# Opcion 2: Metodo get_instance()
registry = CultivoServiceRegistry.get_instance()

# Ambas retornan la MISMA instancia
assert registry is CultivoServiceRegistry.get_instance()
```

**Trazabilidad**: `cultivo_service_registry.py` lineas 20-46

---

### US-TECH-002: Implementar Factory Method para Creacion de Cultivos

**Como** arquitecto de software
**Quiero** centralizar creacion de cultivos mediante Factory Method
**Para** desacoplar cliente de clases concretas

#### Criterios de Aceptacion

- [x] Crear clase `CultivoFactory` con metodo estatico
- [x] Soportar creacion de: Pino, Olivo, Lechuga, Zanahoria
- [x] Usar diccionario de factories (no if/elif cascades)
- [x] Lanzar `ValueError` si especie desconocida
- [x] Retornar tipo base `Cultivo` (no tipos concretos)
- [x] NO usar lambdas - usar metodos estaticos dedicados

#### Detalles Tecnicos

**Clase**: `CultivoFactory`
**Patron**: Factory Method

**Implementacion**:
```python
class CultivoFactory:
    @staticmethod
    def crear_cultivo(especie: str) -> Cultivo:
        factories = {
            "Pino": CultivoFactory._crear_pino,
            "Olivo": CultivoFactory._crear_olivo,
            "Lechuga": CultivoFactory._crear_lechuga,
            "Zanahoria": CultivoFactory._crear_zanahoria
        }

        if especie not in factories:
            raise ValueError(f"Especie desconocida: {especie}")

        return factories[especie]()

    @staticmethod
    def _crear_pino() -> Pino:
        from python_forestacion.entidades.cultivos.pino import Pino
        return Pino(variedad="Parana")

    # ... otros metodos _crear_*
```

**Uso**:
```python
from python_forestacion.patrones.factory.cultivo_factory import CultivoFactory

# Cliente NO conoce clases concretas
cultivo = CultivoFactory.crear_cultivo("Pino")
# Retorna Cultivo (interfaz), no Pino (concreto)
```

**Trazabilidad**: `cultivo_factory.py` lineas 8-67

---

### US-TECH-003: Implementar Observer Pattern para Sensores

**Como** arquitecto de software
**Quiero** implementar patron Observer con Generics
**Para** notificar cambios de sensores de forma tipo-segura

#### Criterios de Aceptacion

- [x] Crear clase `Observable[T]` generica
- [x] Crear interfaz `Observer[T]` generica
- [x] Soportar multiples observadores
- [x] Metodos: `agregar_observador()`, `eliminar_observador()`, `notificar_observadores()`
- [x] Sensores heredan de `Observable[float]`
- [x] Controlador hereda de `Observer[float]`
- [x] Thread-safe en notificaciones

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
class TemperaturaReaderTask(threading.Thread, Observable[float]):
    def run(self):
        while not self._detenido.is_set():
            temp = self._leer_temperatura()
            self.notificar_observadores(temp)  # Notifica float

# Controlador es Observer[float]
class ControlRiegoTask(Observer[float]):
    def actualizar(self, evento: float) -> None:
        self._ultima_temperatura = evento  # Recibe float
```

**Trazabilidad**: `observable.py`, `observer.py`

---

### US-TECH-004: Implementar Strategy Pattern para Absorcion de Agua

**Como** arquitecto de software
**Quiero** implementar algoritmos intercambiables de absorcion
**Para** permitir diferentes estrategias segun tipo de cultivo

#### Criterios de Aceptacion

- [x] Crear interfaz `AbsorcionAguaStrategy` abstracta
- [x] Implementar `AbsorcionSeasonalStrategy` (arboles)
- [x] Implementar `AbsorcionConstanteStrategy` (hortalizas)
- [x] Inyectar estrategia en constructor de servicios
- [x] Servicios delegan calculo a estrategia
- [x] Estrategias usan constantes de `constantes.py`

#### Detalles Tecnicos

**Interfaz**: `AbsorcionAguaStrategy`
**Implementaciones**: `AbsorcionSeasonalStrategy`, `AbsorcionConstanteStrategy`
**Patron**: Strategy

**Implementacion**:
```python
# Interfaz
class AbsorcionAguaStrategy(ABC):
    @abstractmethod
    def calcular_absorcion(
        self,
        fecha: date,
        temperatura: float,
        humedad: float,
        cultivo: 'Cultivo'
    ) -> int:
        pass

# Estrategia 1: Seasonal
class AbsorcionSeasonalStrategy(AbsorcionAguaStrategy):
    def calcular_absorcion(self, fecha, temperatura, humedad, cultivo):
        mes = fecha.month
        if MES_INICIO_VERANO <= mes <= MES_FIN_VERANO:
            return ABSORCION_SEASONAL_VERANO  # 5L
        else:
            return ABSORCION_SEASONAL_INVIERNO  # 2L

# Estrategia 2: Constante
class AbsorcionConstanteStrategy(AbsorcionAguaStrategy):
    def __init__(self, cantidad_constante: int):
        self._cantidad = cantidad_constante

    def calcular_absorcion(self, fecha, temperatura, humedad, cultivo):
        return self._cantidad
```

**Inyeccion**:
```python
class PinoService(ArbolService):
    def __init__(self):
        super().__init__(AbsorcionSeasonalStrategy())  # Inyeccion

class ZanahoriaService(CultivoService):
    def __init__(self):
        super().__init__(AbsorcionConstanteStrategy(2))  # Inyeccion
```

**Delegacion**:
```python
class CultivoService(ABC):
    def absorver_agua(self, cultivo: 'Cultivo') -> int:
        # Delegar a estrategia
        agua_absorvida = self._estrategia_absorcion.calcular_absorcion(
            fecha, temperatura, humedad, cultivo
        )
        cultivo.set_agua(cultivo.get_agua() + agua_absorvida)
        return agua_absorvida
```

**Trazabilidad**: `absorcion_seasonal_strategy.py`, `absorcion_constante_strategy.py`, `cultivo_service.py` lineas 35-59

---

### US-TECH-005: Implementar Registry Pattern para Dispatch Polimorfico

**Como** arquitecto de software
**Quiero** eliminar cascadas de isinstance()
**Para** mejorar mantenibilidad y extensibilidad

#### Criterios de Aceptacion

- [x] Crear diccionarios de handlers por tipo
- [x] Registrar handler para cada tipo de cultivo
- [x] Metodo `absorber_agua()` usa dispatch automatico
- [x] Metodo `mostrar_datos()` usa dispatch automatico
- [x] Lanzar error si tipo no registrado
- [x] NO usar lambdas - usar metodos de instancia dedicados

#### Detalles Tecnicos

**Clase**: `CultivoServiceRegistry`
**Patron**: Registry

**Implementacion**:
```python
class CultivoServiceRegistry:
    def __init__(self):
        # Diccionarios de handlers
        self._absorber_agua_handlers = {
            Pino: self._absorber_agua_pino,
            Olivo: self._absorber_agua_olivo,
            Lechuga: self._absorber_agua_lechuga,
            Zanahoria: self._absorber_agua_zanahoria
        }

        self._mostrar_datos_handlers = {
            Pino: self._mostrar_datos_pino,
            Olivo: self._mostrar_datos_olivo,
            Lechuga: self._mostrar_datos_lechuga,
            Zanahoria: self._mostrar_datos_zanahoria
        }

    def absorber_agua(self, cultivo: Cultivo) -> int:
        tipo = type(cultivo)
        if tipo not in self._absorber_agua_handlers:
            raise ValueError(f"Tipo desconocido: {tipo}")
        return self._absorber_agua_handlers[tipo](cultivo)

    # Handlers dedicados (NO lambdas)
    def _absorber_agua_pino(self, cultivo):
        return self._pino_service.absorver_agua(cultivo)
```

**Ventajas**:
- Sin `isinstance()` cascades
- Facil agregar nuevos tipos
- Mejor rendimiento (O(1) lookup)
- Mas testeable

**Trazabilidad**: `cultivo_service_registry.py` lineas 48-89

---

## Resumen de Cobertura Funcional

### Totales por Epic

| Epic | Historias | Completadas | Cobertura |
|------|-----------|-------------|-----------|
| Epic 1: Terrenos y Plantaciones | 3 | 3 | 100% |
| Epic 2: Gestion de Cultivos | 6 | 6 | 100% |
| Epic 3: Riego Automatizado | 4 | 4 | 100% |
| Epic 4: Gestion de Personal | 4 | 4 | 100% |
| Epic 5: Operaciones de Negocio | 3 | 3 | 100% |
| Epic 6: Persistencia y Auditoria | 3 | 3 | 100% |
| Historias Tecnicas (Patrones) | 5 | 5 | 100% |
| **TOTAL** | **28** | **28** | **100%** |

### Patrones de Diseno Cubiertos

- [x] SINGLETON - CultivoServiceRegistry
- [x] FACTORY METHOD - CultivoFactory
- [x] OBSERVER - Sensores y eventos
- [x] STRATEGY - Absorcion de agua
- [x] REGISTRY - Dispatch polimorfico (bonus)

### Funcionalidades Completas

- [x] Gestion de 4 tipos de cultivos
- [x] Sistema de riego automatizado con 3 threads
- [x] Gestion de trabajadores con apto medico
- [x] Persistencia con Pickle
- [x] Operaciones de negocio de alto nivel
- [x] Manejo de excepciones especificas
- [x] PEP 8 compliance 100%
- [x] Type hints con TYPE_CHECKING
- [x] Constantes centralizadas
- [x] Codigo limpio sin lambdas

---

**Ultima actualizacion**: Octubre 2025
**Estado**: COMPLETO
**Cobertura funcional**: 100%