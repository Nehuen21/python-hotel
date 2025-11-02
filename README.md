# Sistema de Gestion Forestal

[![Python Version](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Code Style](https://img.shields.io/badge/code%20style-PEP%208-orange.svg)](https://www.python.org/dev/peps/pep-0008/)

Sistema integral de gestión hotelera que demuestra la implementación de múltiples patrones de diseño de software con enfoque educativo y profesional.

---

## Tabla de Contenidos

- [Contexto del Dominio](#contexto-del-dominio)
- [Caracteristicas Principales](#caracteristicas-principales)
- [Arquitectura del Sistema](#arquitectura-del-sistema)
- [Patrones de Diseno Implementados](#patrones-de-diseno-implementados)
- [Requisitos del Sistema](#requisitos-del-sistema)
- [Instalacion](#instalacion)
- [Uso del Sistema](#uso-del-sistema)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Modulos del Sistema](#modulos-del-sistema)
- [Documentacion Tecnica](#documentacion-tecnica)
- [Testing y Validacion](#testing-y-validacion)
- [Contribucion](#contribucion)
- [Licencia](#licencia)

---

## Contexto del Dominio

### Problema que Resuelve

El sistema PythonHotel aborda los desafíos de la gestión moderna de establecimientos hoteleros:

1. **Gestion de Multiples Tipos de Habitaciones**
   - Habitaciones estándar (Simple, Doble) con características básicas

    - Suites premium (Suite, Presidencial) con servicios exclusivos

    - Cada tipo con capacidades, tarifas y servicios particulares



2. **Monitoreo Monitoreo automatizado de condiciones**
   - Sensores de ocupación y limpieza que operan continuamente

    - Sistema de limpieza automatizado basado en condiciones

    - Respuesta dinámica a cambios en ocupación y necesidades de mantenimiento

3. **Gestion de Recursos Humanos**
    - Control de empleados con certificaciones profesionales

    - Asignación y seguimiento de tareas de limpieza y mantenimiento

    - Equipos con certificaciones de higiene y seguridad

4. **Planificación de Capacidad**
   - Optimizacion del uso de espacio disponible
   - Registro de alas y pisos en hoteles
   - Control de habitaciones y distribucion espacial

5. **Persistencia y Trazabilidad**
   - Almacenamiento permanente de registros hoteleros
   - Recuperacion de historicos para auditoria
   - Valuacion de propiedades y gestion financiera

### Actores del Sistema

- **Gerente de hotel**: Gestiona el registro hotelero, supervisa operaciones
- **Empleado de limpieza**: Ejecuta tareas de mantenimiento,  y limpieza
- **Sistema de Limpieza Automatizado**: Opera de forma autonoma basado en sensores
- **Auditor/Inspector**: Consulta registros persistidos para verificacion

### Flujo de Operaciones Tipico


1. REGISTRO --> Se crea un registro hotelero con hotel y ala
2. CONFIGURACIÓN --> Se configuran habitaciones según capacidad disponible
3. MONITOREO --> Sensores detectan ocupación y limpieza continuamente
4. LIMPIEZA AUTOMATIZADA --> Sistema limpia cuando se cumplen condiciones
5. MANTENIMIENTO --> Habitaciones reciben mantenimiento según estrategias
6. TAREAS --> Empleados ejecutan mantenimiento con equipos
7. CHECK-OUT --> Huéspedes salen y habitaciones se preparan
8. PERSISTENCIA --> Datos se guardan para auditoría futura



## Caracteristicas Principales

### Funcionalidades del Sistema

#### 1. Gestion de habitaciones

- **Creacion dinamica** de 4 tipos de habitaciones mediante Factory Pattern
  - **habitacion simple**: Habitación económica individual con servicios básicos
  - **habitacion doble**:  Habitación para dos personas con amenities estándar
  - **Suite**: Suite con amenities mejoradas y espacio adicional
  - **Suite presidencial**: Suite de lujo con todos los servicios exclusivos

- **Estrategias de mantenimiento diferenciadas por tipo** por tipo
  - Habitaciones estándar: Mantenimiento básico (30 min)
  - Suites premium: Mantenimiento completo (60-90 min)

- **Actualización automática de estado** de estado
  - Cambio automático de estado después del mantenimiento
  - Actualización de tarifas según temporada

#### 2. Sistema de Limpieza Inteligente

- **Sensores en tiempo real** (patron Observer)
  - Sensor de ocupación: lecturas cada 2 segundos
  - Sensor de limpieza: lecturas cada 3 segundos
  - Rangos: 0-100% ocupación, 0-100% nivel de limpieza

- **Limpieza automatizada condicional**
  - Se activa cuando:
    - Ocupación menor al 10%, Y nivel de limpieza menor al 70%
  - Control cada 2.5 segundos

- **Notificaciones de eventos**
  - Eventos de sensores a observadores suscritos
  - Sistema tipo-seguro con Generics (Observable[float])

#### 3. Gestion de Personal

- **Empleados con certificacion profesional**
  - Certificación obligatoria para trabajar
  - Validación automática antes de ejecutar tareas
  - Fecha de emisión y especializaciones

- **Sistema de tareas**
  - Asignación múltiple de tareas por empleado
  - Ejecución ordenada por prioridad (descendente)
  - Estado de tareas (pendiente/completada)
  - Fecha programada para cada tarea

- **Equipos certificadas**
  - ID unico, nombre y certificacion Higuiene
  - Asignacion a empleados durante tareas

#### 4. Gestion Hotelera

- **Hotel**
  - Identificación única
  - Capacidad total en habitaciones
  - Dirección de ubicación

- **Ala hotel**
  - Nombre identificatorio
  - Control de capacidad disponible
  - Lista de habitaciones configuradas
  - Presupuesto disponible
  - Empleados asignados

- **Registro Hotelero**
  - Vincula hotel con ala específica
  - Propietario y valoración fiscal
  - Persistible en disco

#### 5. Operaciones de Negocio

- **Configuración automática de habitaciones**
  - Cálculo de capacidad requerida
  - Validación de espacio disponible
  - Creacion via Factory Method

- **Limpieza centralizado**
  - Limpia todas las habitaciones de un ala
  - Verifica disponibilidad antes de limpiar


  -Excepción si no hay presupuesto disponible

- **Check-out tipado**
  - Check-out selectivo por tipo de habitación
  - Empaquetado en registros genéricos tipo-seguros
  - Mostración de contenido de registros
- **Desinfección**
  - Aplicación de desinfectante a toda el ala
  - Registro de tipo de desinfectante aplicado



#### 6. Persistencia de Datos

- **Serializacion con Pickle**
  - Guardado completo de RegistroHotelero
  - Directorio configurable (default: `data/`)
  - Nombre de archivo: `{propietario}.dat`

- **Recuperacion de datos**
  - Lectura de registros persistidos
  - Validacion de integridad
  - Manejo de excepciones especificas

---

## Arquitectura del Sistema

### Principios Arquitectonicos

El sistema esta disenado siguiendo principios SOLID:

- **Single Responsibility**: Cada clase tiene una unica razon para cambiar
  - Entidades: Solo contienen datos (DTOs)
  - Servicios: Solo contienen logica de negocio
  - Patrones: Implementaciones aisladas y reutilizables

- **Open/Closed**: Abierto a extension, cerrado a modificacion
  - Nuevas habitaciones: Agregar sin modificar factory existente
  - Nuevas estrategias: Implementar interfaz sin cambiar servicios

- **Liskov Substitution**: Subtipos intercambiables
  - Todas las habitaciones son Habitacion
  - Todas las estrategias implementan AbsorcionAguaStrategy

- **Interface Segregation**: Interfaces especificas
  - Observer[T]: Generico para cualquier tipo de evento
  - MantenimientoStrategy: Específico para mantenimiento

- **Dependency Inversion**: Dependencias de abstracciones
  - Servicios dependen de Strategy (abstraccion), no implementaciones
  - Factory retorna Habitacion (interfaz), no tipos concretos

### Separacion de Capas

+----------------------------------+
|        PRESENTACIÓN              |
|  (main.py - Demostración CLI)    |
+----------------------------------+
                |
                v
+----------------------------------+
|      SERVICIOS DE NEGOCIO        |
|  (HotelesService, Paquete)       |
+----------------------------------+
                |
                v
+----------------------------------+
|      SERVICIOS DE DOMINIO        |
|  (AlaHotelService, etc.)         |
+----------------------------------+
                |
                v
+----------------------------------+
|          ENTIDADES               |
|  (Habitacion, Hotel, Empleado)   |
+----------------------------------+
                |
                v
+----------------------------------+
|      PATRONES / UTILIDADES       |
|  (Factory, Strategy, Observer)   |
+----------------------------------+

### Inyeccion de Dependencias

El sistema utiliza inyeccion manual de dependencias:

```python
# Estrategia inyectada en constructor
class HabitacionSimpleService(HabitacionBaseService):
    def __init__(self):
        super().__init__(MantenimientoEstandarStrategy())

# Sensores inyectados en controlador
tarea_control = ControlLimpiezaTask(
    sensor_ocupacion,    # Dependencia inyectada
    sensor_limpieza,     # Dependencia inyectada
    ala_hotel,
    ala_hotel_service
)
```

---

## Patrones de Diseno Implementados

### 1. SINGLETON Pattern

**Ubicacion**: `python_hotel/servicios/habitaciones/habitacion_service_registry.py`

**Problema que resuelve**:
- Garantizar una unica instancia del registro de servicios
- Compartir estado entre todos los servicios del sistema
- Evitar multiples registros inconsistentes

**Implementacion**:
```python
class HabitacionServiceRegistry:
    _instance = None
    _lock = Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:  # Thread-safe double-checked locking
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance
```

**Uso en el sistema**:
- Todos los servicios de cultivos comparten el mismo registry
- Elimina cadenas de `isinstance()` mediante dispatch polimorfico
- Acceso: `HabitacionServiceRegistry.get_instance()`

**Ventajas**:
- Thread-safe mediante Lock
- Inicializacion perezosa (lazy initialization)
- Punto unico de control

---

### 2. FACTORY METHOD Pattern

**Ubicacion**: `python_hotel/patrones/factory/habitacion_factory.py`

**Problema que resuelve**:
- Creación de habitaciones sin conocer clases concretas
- Encapsulacion de logica de construccion compleja
- Extensibilidad para nuevos tipos de habitaciones

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
```

**Uso en el sistema**:
```python
## AlaHotelService usa factory internamente
ala_hotel_service.configurar(ala_hotel, "Simple", 5)
# Crea 5 Habitaciones Simples sin conocer constructor
```

**Ventajas**:
- Codigo cliente independiente de clases concretas
- Fácil agregar nuevas habitaciones
- Validacion centralizada de especies

---

### 3. OBSERVER Pattern

**Ubicacion**: `python_hotel/patrones/observer/`

**Problema que resuelve**:
- Notificación automática a múltiples observadores
- Desacoplamiento entre sensores y consumidores
- Sistema de eventos tipo-seguro

**Implementacion**:
```python
class Observable(Generic[T], ABC):
    def __init__(self):
        self._observadores: List[Observer[T]] = []

    def agregar_observador(self, observador: Observer[T]) -> None:
        self._observadores.append(observador)

    def notificar_observadores(self, evento: T) -> None:
        for observador in self._observadores:
            observador.actualizar(evento)
```

**Uso en el sistema**:
```python
# Sensor es Observable
class OcupacionReaderTask(threading.Thread, Observable[float]):
    def run(self):
        while not self._detenido.is_set():
            ocupacion = self._leer_ocupacion()
            # Notifica a todos los observadores
            self.notificar_observadores(ocupacion)
            time.sleep(INTERVALO_SENSOR_OCUPACION)

# ControlLimpiezaTask es Observer
class ControlLimpiezaTask(Observer[float]):
    def actualizar(self, evento: float) -> None:
        # Recibe notificación automáticamente
        self._ultima_ocupacion = evento
```

**Ventajas**:
- Tipo-seguro con Generics
- Desacoplamiento total
- Multiples observadores permitidos

---

### 4. STRATEGY Pattern

**Ubicacion**: `python_hotel/patrones/strategy/`

**Problema que resuelve**:
- Algoritmos de mantenimiento intercambiables
- Eliminar condicionales tipo if/else
- Permitir cambios en tiempo de ejecucion

**Implementacion**:
```python
class MantenimientoStrategy(ABC):
    @abstractmethod
    def calcular_mantenimiento(
        self,
        fecha: date,
        ocupacion: float,
        limpieza: float,
        habitacion: 'Habitacion'
    ) -> int:
        pass

# Estrategia 1: Estandar
class MantenimientoEstandarStrategy(MantenimientoStrategy):
    def calcular_mantenimiento(self, fecha, ocupacion, limpieza, habitacion):
        if ocupacion < 0.3:  # Baja ocupación
            return MANTENIMIENTO_ESTANDAR_COMPLETO  # 60 min
        else:
            return MANTENIMIENTO_ESTANDAR_BASICO  # 30 min

# Estrategia 2: Premium
class MantenimientoPremiumStrategy(MantenimientoStrategy):
    def __init__(self, tiempo_constante: int):
        self._tiempo = tiempo_constante

    def calcular_mantenimiento(self, fecha, ocupacion, limpieza, habitacion):
        return self._tiempo  # Siempre el mismo tiempo

```
**Uso en el sistema**
```python
# Inyección de estrategia en servicio
class HabitacionSimpleService(HabitacionBaseService):
    def __init__(self):
        super().__init__(MantenimientoEstandarStrategy())  # Estándar: estacional

class SuitePresidencialService(HabitacionService):
    def __init__(self):
        super().__init__(MantenimientoPremiumStrategy(90))  # Premium: constante
```
**Ventajas**:
- Algoritmos intercambiables
- Sin modificar codigo cliente
- Testeable independientemente

---

### 5. REGISTRY Pattern (Bonus)

**Ubicacion**: `python_hotel/servicios/habitaciones/habitacion_service_registry.py`

**Problema que resuelve**:
- Eliminar cascadas de `isinstance()`
- Dispatch polimorfico basado en tipo
- Punto unico de registro de servicios

**Implementacion**:
```python
class HabitacionServiceRegistry:
    def __init__(self):
        # Registro de handlers por tipo
        self._realizar_mantenimiento_handlers = {
            HabitacionSimple: self._realizar_mantenimiento_simple,
            HabitacionDoble: self._realizar_mantenimiento_doble,
            Suite: self._realizar_mantenimiento_suite,
            SuitePresidencial: self._realizar_mantenimiento_presidencial
        }

    def realizar_mantenimiento(self, habitacion: Habitacion) -> int:
        tipo = type(habitacion)
        if tipo not in self._realizar_mantenimiento_handlers:
            raise ValueError(f"Tipo desconocido: {tipo}")

        # Dispatch polimórfico
        return self._realizar_mantenimiento_handlers[tipo](habitacion)
```

**Antes (con isinstance)**:
```python
if isinstance(habitacion, HabitacionSimple):
    return simple_service.realizar_mantenimiento(habitacion)
elif isinstance(habitacion, HabitacionDoble):
    return doble_service.realizar_mantenimiento(habitacion)
elif isinstance(habitacion, Suite):
    return suite_service.realizar_mantenimiento(habitacion)
# ... 4 más
```

**Despues (con Registry)**:
```python
return registry.realizar_mantenimiento(habitacion)  # Despacho automático
```

---

## Requisitos del Sistema

### Requisitos de Software

- **Python 3.13** o superior
- **Sistema Operativo**: Windows, Linux, macOS
- **Modulos Estandar**: Solo biblioteca estandar de Python (sin dependencias externas)

### Requisitos de Hardware

- **RAM**: Minimo 512 MB
- **Disco**: 50 MB libres
- **Procesador**: Cualquier procesador moderno (1 GHz+)

---

## Instalacion

### 1. Clonar el Repositorio

```bash
git clone https://github.com/usuario/python-hotel.git
cd python-hotel
```

### 2. Crear Entorno Virtual

#### Windows:
```bash
python -m venv .venv
.venv\Scripts\activate
```

#### Linux/macOS:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Verificar Instalacion

```bash
python --version
# Debe mostrar Python 3.13 o superior
```

### 4. Ejecutar Sistema

```bash
python main.py
```

**Salida esperada**:
```
======================================================================
         SISTEMA DE GESTIÓN HOTELERA - PATRONES DE DISEÑO
======================================================================

----------------------------------------------------------------------
  PATRON SINGLETON: Inicializando servicios
----------------------------------------------------------------------
[OK] Todos los servicios comparten la misma instancia del Registry

1. Creando hotel con ala...
...
======================================================================
              EJEMPLO COMPLETADO EXITOSAMENTE
======================================================================
  [OK] SINGLETON   - HabitacionServiceRegistry (instancia única)
  [OK] FACTORY     - Creación de habitaciones
  [OK] OBSERVER    - Sistema de sensores y eventos
  [OK] STRATEGY    - Algoritmos de mantenimiento
======================================================================
```

---

## Uso del Sistema

### Ejemplo Basico

```python
from python_hotel.servicios.hotel.hotel_service import HotelService
from python_hotel.servicios.hotel.ala_hotel_service import AlaHotelService

# 1. Crear hotel con ala
hotel_service = HotelService()
hotel = hotel_service.crear_hotel_con_ala(
    id_hotel=1,
    capacidad=100,
    direccion="Av. Principal 123, Ciudad",
    nombre_ala="Ala Norte"
)

# 2. Obtener ala
ala_hotel = hotel.get_ala()

# 3. Configurar habitaciones (usa Factory Method internamente)
ala_hotel_service = AlaHotelService()
ala_hotel_service.configurar(ala_hotel, "Simple", 5)
ala_hotel_service.configurar(ala_hotel, "Doble", 3)

# 4. Realizar limpieza (usa Strategy Pattern internamente)
ala_hotel_service.limpiar(ala_hotel)

# 5. Realizar check-out
ala_hotel_service.realizar_checkout(ala_hotel)
```

### Sistema de Limpieza Automatizado

```python
from python_hotel.monitoreo.sensores.ocupacion_reader_task import OcupacionReaderTask
from python_hotel.monitoreo.sensores.limpieza_reader_task import LimpiezaReaderTask
from python_hotel.monitoreo.control.control_limpieza_task import ControlLimpiezaTask

# Crear sensores (Observable)
sensor_ocupacion = OcupacionReaderTask()
sensor_limpieza = LimpiezaReaderTask()

# Crear controlador (Observer)
control_limpieza = ControlLimpiezaTask(
    sensor_ocupacion,
    sensor_limpieza,
    ala_hotel,
    ala_hotel_service
)

# Iniciar threads daemon
sensor_ocupacion.start()
sensor_limpieza.start()
control_limpieza.start()

# Sistema funciona automáticamente
time.sleep(20)  # Dejarlo funcionar 20 segundos

# Detener sistema
sensor_ocupacion.detener()
sensor_limpieza.detener()
control_limpieza.detener()
```

### Persistencia de Datos

```python
from python_hotel.servicios.hotel.registro_hotelero_service import RegistroHoteleroService
from python_hotel.entidades.hotel.registro_hotelero import RegistroHotelero

# Crear registro
registro = RegistroHotelero(
    id_hotel=1,
    hotel=hotel,
    ala_hotel=ala_hotel,
    propietario="Carlos Rodríguez",
    avaluo=15000000.75
)

# Persistir
registro_service = RegistroHoteleroService()
registro_service.persistir(registro)
# Crea archivo: data/Carlos Rodríguez.dat

# Recuperar
registro_leido = RegistroHoteleroService.leer_registro("Carlos Rodríguez")
registro_service.mostrar_datos(registro_leido)
```

---

## Estructura del Proyecto

```
PythonHotel/
|
+-- main.py                          # Punto de entrada del sistema
+-- CLAUDE.md                        # Guía para Claude Code
+-- README.md                        # Este archivo
+-- USER_STORIES.md                  # Historias de usuario detalladas
+-- RUBRICA_EVALUACION.md            # Rúbrica de evaluación técnica
+-- RUBRICA_AUTOMATIZADA.md          # Rúbrica para automatización n8n
|
+-- .venv/                           # Entorno virtual Python
|
+-- data/                            # Datos persistidos (archivos .dat)
|
+-- python_hotel/                    # Paquete principal
    |
    +-- __init__.py
    +-- constantes.py                # Constantes centralizadas del sistema
    |
    +-- entidades/                   # Objetos de dominio (DTOs)
    |   +-- __init__.py
    |   |
    |   +-- habitaciones/            # Habitaciones del sistema
    |   |   +-- __init__.py
    |   |   +-- habitacion.py        # Interfaz base
    |   |   +-- habitacion_base.py   # Base para habitaciones estándar
    |   |   +-- habitacion_premium.py # Base para suites premium
    |   |   +-- habitacion_simple.py # Habitación tipo Simple
    |   |   +-- habitacion_doble.py  # Habitación tipo Doble
    |   |   +-- suite.py             # Suite estándar
    |   |   +-- suite_presidencial.py # Suite presidencial
    |   |
    |   +-- hotel/                   # Gestión hotelera
    |   |   +-- __init__.py
    |   |   +-- hotel.py             # Hotel completo
    |   |   +-- ala_hotel.py         # Ala o piso del hotel
    |   |   +-- registro_hotelero.py # Registro completo
    |   |
    |   +-- personal/                # Recursos humanos
    |       +-- __init__.py
    |       +-- empleado.py          # Empleado del hotel
    |       +-- equipo_limpieza.py   # Equipo de limpieza
    |       +-- tarea.py             # Tarea asignada
    |       +-- certificacion.py     # Certificación profesional
    |
    +-- servicios/                   # Lógica de negocio
    |   +-- __init__.py
    |   |
    |   +-- habitaciones/            # Servicios de habitaciones
    |   |   +-- __init__.py
    |   |   +-- habitacion_service.py           # Servicio base
    |   |   +-- habitacion_base_service.py      # Servicio base estándar
    |   |   +-- habitacion_simple_service.py    # Servicio Simple
    |   |   +-- habitacion_doble_service.py     # Servicio Doble
    |   |   +-- suite_service.py                # Servicio Suite
    |   |   +-- suite_presidencial_service.py   # Servicio Presidencial
    |   |   +-- habitacion_service_registry.py  # Registry + Singleton
    |   |
    |   +-- hotel/                   # Servicios hoteleros
    |   |   +-- __init__.py
    |   |   +-- hotel_service.py                # Servicio Hotel
    |   |   +-- ala_hotel_service.py            # Servicio AlaHotel
    |   |   +-- registro_hotelero_service.py    # Servicio Registro
    |   |
    |   +-- personal/                # Servicios de personal
    |   |   +-- __init__.py
    |   |   +-- empleado_service.py             # Servicio Empleado
    |   |
    |   +-- negocio/                 # Servicios de alto nivel
    |       +-- __init__.py
    |       +-- hoteles_service.py              # Operaciones hoteles
    |       +-- paquete.py                      # Empaquetado genérico
    |
    +-- patrones/                    # Implementaciones de patrones
    |   +-- __init__.py
    |   |
    |   +-- singleton/               # Patrón Singleton
    |   |   +-- __init__.py
    |   |
    |   +-- factory/                 # Patrón Factory Method
    |   |   +-- __init__.py
    |   |   +-- habitacion_factory.py           # Factory de habitaciones
    |   |
    |   +-- observer/                # Patrón Observer
    |   |   +-- __init__.py
    |   |   +-- observable.py                   # Clase Observable[T]
    |   |   +-- observer.py                     # Interfaz Observer[T]
    |   |   +-- eventos/
    |   |       +-- __init__.py
    |   |       +-- evento_sensor.py            # Evento de sensores
    |   |       +-- evento_hotel.py             # Evento de hotel
    |   |
    |   +-- strategy/                # Patrón Strategy
    |       +-- __init__.py
    |       +-- mantenimiento_strategy.py       # Interfaz Strategy
    |       +-- impl/
    |           +-- __init__.py
    |           +-- mantenimiento_estandar_strategy.py    # Estandar
    |           +-- mantenimiento_premium_strategy.py     # Premium
    |
    +-- monitoreo/                   # Sistema de monitoreo automatizado
    |   +-- __init__.py
    |   |
    |   +-- sensores/                # Sensores de monitoreo
    |   |   +-- __init__.py
    |   |   +-- ocupacion_reader_task.py        # Sensor ocupación
    |   |   +-- limpieza_reader_task.py         # Sensor limpieza
    |   |
    |   +-- control/                 # Control de limpieza
    |       +-- __init__.py
    |       +-- control_limpieza_task.py        # Controlador
    |
    +-- excepciones/                 # Excepciones personalizadas
        +-- __init__.py
        +-- hotel_exception.py                  # Excepción base
        +-- capacidad_insuficiente_exception.py
        +-- presupuesto_agotado_exception.py
        +-- persistencia_exception.py
        +-- mensajes_exception.py               # Mensajes centralizados
```

---

## Modulos del Sistema

### Modulo: `entidades`

**Responsabilidad**: Objetos de dominio puros (DTOs - Data Transfer Objects)

**Caracteristicas**:
- Solo contienen datos y getters/setters
- NO contienen logica de negocio
- Campos privados con encapsulacion

**Clases principales**:
- `Habitacion`: Interfaz base para todas las habitaciones
- `habitacion base`: Base para habitaciones standar (simple, doble)
- `HabitacionPremium`: Base para suites premium (Suite, Presidencial)
- `Hotel`: Instalación hotelera completa
- `AlaHotel`: Ala o piso del hotel con habitaciones
- `Empleado`:Persona con tareas asignadas

---

### Modulo: `servicios`

**Responsabilidad**: Logica de negocio del sistema

**Caracteristicas**:
- Servicios sin estado (stateless)
- Operaciones sobre entidades
- Orquestacion de patrones

**Servicios principales**:
- `AlaHotelService`:  Configurar, limpiar, realizar checkout, desinfectar
- `EmpleadoService`: Asignar tareas, verificar certificación
- `RegistroHoteleroService`: Persistir y recuperar registros
- `HotelesService`: Operaciones de alto nivel en hoteles

---

### Modulo: `patrones`

**Responsabilidad**: Implementaciones de patrones de diseno

**Patrones incluidos**:
1. **Singleton**: `HabitacionServiceRegistry`
2. **Factory Method**: `HabitacionFactory`
3. **Observer**: `Observable[T]` / `Observer[T]`
4. **Strategy**: `MantenimientoStrategy` + implementaciones

---

### Modulo: `monitoreo`

**Responsabilidad**: Sistema de monitoreo automatizado con threads

**Componentes**:
- **Sensores** (Observable):
  - `OcupacionReaderTask`: Lee ocupacion cada 2s
  - `LimpiezaReaderTask`: Lee nivel de limpieza cada 3s

- **Control** (Observer):
  - `ControlLimpiezaTask`: Observa sensores y limpia automaticamente

**Modelo de threading**:
- Threads daemon (finalizan con main)
- Graceful shutdown con `threading.Event`
- Timeouts configurables

---

### Modulo: `excepciones`

**Responsabilidad**: Excepciones de dominio especificas

**Jerarquia**:
```
HotelException (base)
  +-- CapacidadInsuficienteException
  +-- PresupuestoAgotadoException
  +-- PersistenciaException
```

**Caracteristicas**:
- Mensajes separados: usuario vs tecnico
- Contexto especifico del error
- Causas encadenadas

---

## Documentacion Tecnica

### Convenciones de Codigo

#### PEP 8 Compliance (100%)

- **Nombres de variables**: `snake_case`
- **Nombres de clases**: `PascalCase`
- **Constantes**: `UPPER_SNAKE_CASE` en `constantes.py`
- **Privados**: Prefijo `_nombre`

#### Docstrings (Google Style)

```python
def metodo(self, parametro: str) -> int:
    """
    Descripcion breve del metodo.

    Args:
        parametro: Descripcion del parametro

    Returns:
        Descripcion del valor de retorno

    Raises:
        ValueError: Cuando ocurre validacion
    """
```

#### Type Hints

```python
from typing import TYPE_CHECKING, List, Optional

if TYPE_CHECKING:
    from modulo import Clase  # Evita imports circulares

def metodo(self, lista: List[int]) -> Optional[str]:
    pass
```

### Configuracion de Constantes

Todas las constantes en `constantes.py`:

```python
# Capacidad
CAPACIDAD_MINIMA = 1
CAPACIDAD_MAXIMA_HOTEL = 1000

# Presupuesto
PRESUPUESTO_INICIAL_ALA = 5000
PRESUPUESTO_MINIMO = 100

# Habitaciones - Capacidades
CAPACIDAD_SIMPLE = 1
CAPACIDAD_DOBLE = 2
CAPACIDAD_SUITE = 4
CAPACIDAD_PRESIDENCIAL = 6

# Mantenimiento
MANTENIMIENTO_ESTANDAR_BASICO = 30  # minutos
MANTENIMIENTO_ESTANDAR_COMPLETO = 60
MANTENIMIENTO_PREMIUM_BASICO = 60
MANTENIMIENTO_PREMIUM_COMPLETO = 90

# Monitoreo
INTERVALO_SENSOR_OCUPACION = 2.0
INTERVALO_SENSOR_LIMPIEZA = 3.0
INTERVALO_CONTROL_LIMPIEZA = 2.5
```

**Regla**: NUNCA hardcodear valores magicos en el codigo.

### Manejo de Excepciones

```python
try:
    ala_hotel_service.configurar(ala_hotel, "Simple", 100)
except CapacidadInsuficienteException as e:
    print(e.get_user_message())
    print(f"Requerida: {e.get_capacidad_requerida()}")
    print(f"Disponible: {e.get_capacidad_disponible()}")
except HotelException as e:
    print(e.get_full_message())
```

---

## Testing y Validacion

### Ejecucion del Sistema Completo

El archivo `main.py` contiene un test de integracion completo que valida:

1. [x] Patron Singleton - Instancia unica compartida
2. [x] Patron Factory - Creacion de 4 tipos de habitaciones
3. [x] Patron Observer - Sensores y notificaciones
4. [x] Patron Strategy - mantenimiento diferenciado
5. [x] Configuracion y control de capacidad
6. [x] Limpieza automatizada
7. [x] Gestión de empleados con certificación
8. [x] Check-out y empaquetado tipado
9. [x] Persistencia y recuperacion
10. [x] Threading y graceful shutdown

### Validacion Manual

```bash
python main.py
```

**Criterios de exito**:
- No errores de importacion
- No excepciones no controladas
- Mensaje final: `EJEMPLO COMPLETADO EXITOSAMENTE`
- Archivo creado: `data/Carlos Rodríguez.dat`

### Casos de Prueba

#### Caso 1: Capacidad Insuficiente
```python
# Configuración requiere más capacidad de la disponible
try:
    ala_hotel_service.configurar(ala_hotel, "Simple", 10000)
except CapacidadInsuficienteException as e:
    assert e.get_capacidad_requerida() > e.get_capacidad_disponible()
```

#### Caso 2: Presupuesto Agotado
```python
# Limpieza sin presupuesto disponible
ala_hotel.set_presupuesto_disponible(0)
try:
    ala_hotel_service.limpiar(ala_hotel)
except PresupuestoAgotadoException as e:
    assert "agotado" in e.get_user_message().lower()
```

#### Caso 3: Empleado sin certificacion
```python
# Empleado sin certificación no puede trabajar
empleado = Empleado(12345678, "Test", [])
resultado = empleado_service.trabajar(empleado, date.today(), equipo)
assert resultado == False
```

---

## Contribucion

### Como Agregar un Nuevo Tipo de Habitacion

#### Paso 1: Definir Constantes

En `constantes.py`:
```python
# Constantes de la nueva habitación
CAPACIDAD_FAMILIAR = 5
TARIFA_BASE_FAMILIAR = 150.0
```

#### Paso 2: Crear Entidad

En `entidades/habitaciones/habitacion_familiar.py:`:
```python
from python_hotel.entidades.habitaciones.habitacion_base import HabitacionBase
from python_hotel.constantes import CAPACIDAD_FAMILIAR, TARIFA_BASE_FAMILIAR

class HabitacionFamiliar(HabitacionBase):
    """Entidad HabitacionFamiliar - solo datos."""

    def __init__(self, id: int, tiene_cuna: bool = False):
        super().__init__(
            id=id,
            capacidad=CAPACIDAD_FAMILIAR,
            tarifa_base=TARIFA_BASE_FAMILIAR
        )
        self._tiene_cuna = tiene_cuna

    def get_tiene_cuna(self) -> bool:
        return self._tiene_cuna

    def set_tiene_cuna(self, tiene_cuna: bool) -> None:
        self._tiene_cuna = tiene_cuna
```

#### Paso 3: Crear Servicio

En `servicios/habitaciones/habitacion_familiar_service.py`:
```python
from python_hotel.servicios.habitaciones.habitacion_base_service import HabitacionBaseService
from python_hotel.patrones.strategy.impl.mantenimiento_estandar_strategy import MantenimientoEstandarStrategy

class HabitacionFamiliarService(HabitacionBaseService):
    """Servicio para HabitacionFamiliar."""

    def __init__(self):
        super().__init__(MantenimientoEstandarStrategy())

    def mostrar_datos(self, habitacion: 'HabitacionFamiliar') -> None:
        super().mostrar_datos(habitacion)
        print(f"Cuna disponible: {'Sí' if habitacion.get_tiene_cuna() else 'No'}")
```

#### Paso 4: Registrar en Registry

En `habitacion_service_registry.py`:
```python
from python_hotel.entidades.habitaciones.habitacion_familiar import HabitacionFamiliar
from python_hotel.servicios.habitaciones.habitacion_familiar_service import HabitacionFamiliarService

class HabitacionServiceRegistry:
    def __init__(self):
        self._habitacion_familiar_service = HabitacionFamiliarService()

        self._realizar_mantenimiento_handlers[HabitacionFamiliar] = self._realizar_mantenimiento_familiar
        self._mostrar_datos_handlers[HabitacionFamiliar] = self._mostrar_datos_familiar

    def _realizar_mantenimiento_familiar(self, habitacion):
        return self._habitacion_familiar_service.realizar_mantenimiento(habitacion)

    def _mostrar_datos_familiar(self, habitacion):
        return self._habitacion_familiar_service.mostrar_datos(habitacion)
```

#### Paso 5: Registrar en Factory

En `habitacion_factory.py`:
```python
@staticmethod
def _crear_familiar() -> HabitacionFamiliar:
    from python_hotel.entidades.habitaciones.habitacion_familiar import HabitacionFamiliar
    return HabitacionFamiliar(id=id_generado, tiene_cuna=True)

@staticmethod
def crear_habitacion(tipo: str) -> Habitacion:
    factories = {
        # ... existentes
        "Familiar": HabitacionFactory._crear_familiar
    }
```

#### Paso 6: Usar el Nuevo Cultivo

```python
ala_hotel_service.configurar(ala_hotel, "Familiar", 3)
```

---

## Licencia

Este proyecto es de codigo abierto y esta disponible bajo la licencia MIT.

---

## Contacto y Soporte

- **Documentacion**: Ver `CLAUDE.md` para guia tecnica detallada
- **Historias de Usuario**: Ver `USER_STORIES.md` para casos de uso
- **Rubrica de Evaluacion**: Ver `RUBRICA_EVALUACION.md`

---

## Notas Adicionales

### Compatibilidad con Windows

El sistema fue desarrollado y probado en Windows. Consideraciones:

- **NO usar emojis** en print (problema de encoding)
- **NO usar caracteres Unicode especiales** en consola
- Usar solo ASCII estandar: `[OK]`, `[!]`, `[INFO]`

### Rendimiento

- Sistema optimizado para operaciones locales
- Threads livianos para sensores
- Persistencia con Pickle (rapida pero NO para produccion)

### Limitaciones Conocidas

1. Pickle NO es seguro para datos no confiables
2. Sistema single-process (no distribuido)
3. Sin base de datos relacional
4. Sin interfaz grafica (solo CLI)

**Este es un proyecto EDUCATIVO** enfocado en patrones de diseno, NO en produccion real.

---

**Ultima actualizacion**: Octubre 2025
**Version del sistema**: 1.0.0
**Python requerido**: 3.13+