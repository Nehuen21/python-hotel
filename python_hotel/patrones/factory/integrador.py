"""
Archivo integrador generado automaticamente
Directorio: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/patrones/factory
Fecha: 2025-11-04 18:03:54
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/patrones/factory/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: habitacion_factory.py
# Ruta: /home/nehuen/Escritorio/Diseño/python-hotel/python_hotel/patrones/factory/habitacion_factory.py
# ================================================================================

"""
Modulo del Patron Factory Method.

Implementa una fabrica (Factory) para la creacion de objetos 'Habitacion',
desacoplando al cliente (servicios) de las clases concretas.
"""

from typing import TYPE_CHECKING, Callable

# Importacion de la ABSTRACCION (interfaz)
from python_hotel.entidades.habitaciones.habitacion import Habitacion

# Importacion de las clases CONCRETAS (solo para type hints)
# Las importaciones reales se hacen DENTRO de los metodos
# para evitar importaciones circulares y cargar solo lo necesario.
if TYPE_CHECKING:
    from python_hotel.entidades.habitaciones.habitacion_simple import HabitacionSimple
    from python_hotel.entidades.habitaciones.habitacion_doble import HabitacionDoble
    from python_hotel.entidades.habitaciones.suite import Suite
    from python_hotel.entidades.habitaciones.suite_presidencial import SuitePresidencial

# Definimos un tipo para nuestro "diccionario de fabricas"
# Es un diccionario que mapea un string a una funcion que no
# toma argumentos y retorna una Habitacion.
FactoryMethodType = Callable[[], Habitacion]


class HabitacionFactory:
    """
    Implementa el patron Factory Method como una clase estatica.
    Centraliza la creacion de todos los tipos de Habitacion.
    """

    @staticmethod
    def _crear_simple() -> 'HabitacionSimple':
        """Metodo 'constructor' privado para HabitacionSimple."""
        from python_hotel.entidades.habitaciones.habitacion_simple import HabitacionSimple
        # Aqui se podria agregar logica de inicializacion compleja si fuese necesario
        return HabitacionSimple()

    @staticmethod
    def _crear_doble() -> 'HabitacionDoble':
        """Metodo 'constructor' privado para HabitacionDoble."""
        from python_hotel.entidades.habitaciones.habitacion_doble import HabitacionDoble
        return HabitacionDoble()

    @staticmethod
    def _crear_suite() -> 'Suite':
        """Metodo 'constructor' privado para Suite."""
        from python_hotel.entidades.habitaciones.suite import Suite
        return Suite()

    @staticmethod
    def _crear_presidencial() -> 'SuitePresidencial':
        """Metodo 'constructor' privado para SuitePresidencial."""
        from python_hotel.entidades.habitaciones.suite_presidencial import SuitePresidencial
        return SuitePresidencial()

    @staticmethod
    def crear_habitacion(tipo: str) -> Habitacion:
        """
        El metodo Factory publico.

        Recibe un string y retorna la instancia de la habitacion correspondiente.

        Args:
            tipo: El string identificador (ej. "Simple", "Suite").

        Returns:
            Una instancia de una subclase de Habitacion.

        Raises:
            ValueError: Si el tipo de habitacion solicitado no esta registrado.
        """
        # Mapeo de string a funcion constructora (Patron Registry simple)
        factories: dict[str, FactoryMethodType] = {
            "Simple": HabitacionFactory._crear_simple,
            "Doble": HabitacionFactory._crear_doble,
            "Suite": HabitacionFactory._crear_suite,
            "Presidencial": HabitacionFactory._crear_presidencial
            # Para agregar un nuevo tipo, solo anadimos una linea aqui
        }

        # Obtenemos la funcion constructora del diccionario
        constructor_func = factories.get(tipo)

        if not constructor_func:
            raise ValueError(f"Tipo de habitación desconocido: '{tipo}'")

        # Ejecutamos la funcion constructora (ej. _crear_simple())
        nueva_habitacion = constructor_func()
        
        print(f"INFO (Factory): Creada nueva habitacion ID {nueva_habitacion.get_id()} (Tipo: {tipo})")
        return nueva_habitacion

