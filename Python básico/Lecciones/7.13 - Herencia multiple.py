# Herencia Multiple
'''
La herencia múltiple en Python es cuando una clase puede heredar atributos y métodos de más de una clase padre al mismo tiempo.
En lugar de seguir una sola línea de herencia (como en Java, por ejemplo), Python permite que una clase tenga múltiples bases.

-- Creación de Herencia Multiple --
    Class Hija_1 (Clase_padre_1, Clase_padre_2) --> De esta forma se realiza la herencia multiple de clase es muy importante
                                                verificar el orden el en que se agrega la herencia de las clases.

-- Inicializar atributos heredados de las Clases Padre
    def __init__(atributo_1,atributo_2):
        Clase_padre_1.__init__(self, atributo_1) --> inicializa el atributo de la clase padre 1
        Clase_padre_2.__init__(selfg, atributo_2) --> inicializa el atributo de la clase padre 2

        El primer atributo que se deberá pasar es el de Self ya que se esta usando el método init de la clase Padre.
'''
# Ejemplo
class Figura_geometrica: # Clase_padre_1

    def __init__(self, alto, ancho):
        self.alto = alto
        self.ancho = ancho

class Color: # Clase_padre_2
    def __init__(self,color:str):
        self.color = color

# Aqui se muestra como se realiza la herencia multiple
class Cuadrado(Figura_geometrica, Color): # Clase hija con la Herencia de las clase Clase_padre_1 y Clase_padre_2.
    # Inicializador de la clase hija.
    def __init__(self,lado,color):
        # super().__init__() De esta forma se inicializan los atributos de la clase padre, pero
        # al tener doble herencia no es recomendable usarlo porque tomará los métodos de la primera clase
        # heredada en este caso Figura_geometrica
        Figura_geometrica.__init__(self,lado,lado) # ->> De esta forma se inicializan especificamente los atributos de cada clase
        Color.__init__(self,color)

    # Definir método para calcular área
    def Area(self):
        return f'{self.alto * self.ancho}'

# Ejemplo
# Creación de objeto
cuadrado1 = Cuadrado(10,'Azul')
# Mostrar el uso de los atributos del los padres
print(f'El Área es de: {cuadrado1.Area()}')
print(f'El Alto es de: {cuadrado1.alto}')
print(f'EL Ancho es de: {cuadrado1.ancho}')
print(f'El color es: {cuadrado1.color}')

# Method Resolution Order or MRO
'''
MRO (Method Resolution Order) es el orden en el que Python busca métodos o atributos en las clases de un objeto, 
especialmente cuando hay herencia múltiple. Es decir, define qué clase se revisa primero cuando llamas a un método o atributo.
'''
print(Cuadrado.mro()) # Imprimira el orden en el cual se van mandando a llamar las clases.