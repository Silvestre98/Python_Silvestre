# Clase Abstracta
'''
Una clase abstracta es una clase que no puede instanciarse directamente y que sirve como modelo o plantilla
para que otras clases la hereden. Su propósito es definir una estructura común (métodos y atributos que deben implementarse)
sin dar todos los detalles de la implementación.

1. Características principales

    🔹 Se definen usando el módulo abc (Abstract Base Classes).
    🔹 Pueden tener métodos abstractos (obligatorios de implementar en las clases hijas).
    🔹 Pueden tener también métodos normales (con código) que se heredan tal cual.
    🔹 No puedes crear objetos directamente de una clase abstracta.
'''
# Importar la clase abc con ABS (Abstract Base Classes),abstractclassmethod
from abc import ABC, abstractmethod

# Creación de clase figura geometrica
class Carro(abs):
    # Inicializador 
    def __init__(self, marca, anio):
        self.marca = marca
        self.anio = anio
    
    # Crear método abstracto
    @abstractmethod # Decorador para crear métodos abstractos
    def avanzar(self):
        pass # Se deberá agregar la implementación del método abstracto por su cuenta en las clases hijas
    
# Ahora cada que se cree un sub clase de Carro tendrá que tener el método Abstracto de forma obligaroria
#  y de igual forma no se puede instanciar esta clase
# Ejemplo
# carro = Carro('Ford',2009) ->> Esto es incorrecto no se puede instanciar una clase Abstracta