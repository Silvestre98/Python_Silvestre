
# Metodos Get y Set
"""
El método Get y Set facilitan el acceso a los atributos de la clase, ya que uno se encarga de leer (get) y otro de
realizar las modificaciones pertinentes a los valores del atributo (set).
"""
class Automovil:
    def __init__(self, marca, modelo, color):
        self._color = color
        self._marca = marca
        self._modelo = modelo

    def manejar(self):
        return print(f'''
        Conduciendo:
        Color de carro: {self._color}
        Marca: {self._marca}
        Modelo: {self._modelo}
    ''')

    #Creacion de los métodos set y get para cada uno de los atributos de forma tradicional.

    # Get marca
    def get_marca(self):
        return print(f'Marca de auto: {self._marca}')
    # Set marca
    def set_marca(self,marca):
        self._marca = marca

    # Get color
    def get_color(self):
        return print(f'Color de auto: {self._color}')
    # Set color
    def set_color(self,color):
        self._color = color

    # Get modelo
    def get_modelo(self):
        return print(f'Modelo de auto: {self._modelo}')
    # Set modelo
    def set_modelo(self,modelo):
        self._modelo = modelo

# Utilizando los metodos Get y Set

#Creando objeto
vehiculo = Automovil('BMW','A43','Verde')

# Usando get y set, para modificar y acceder a su información.
vehiculo.set_marca('Maseratti')
vehiculo.get_marca()

vehiculo.set_color('Morado')
vehiculo.get_color()

vehiculo.set_modelo('Lk-12')
vehiculo.get_modelo()
print()


# ********************************************************************************************************************** #
# Mejorando el encapulamiento
# Pythonico que el código sea más conciso
"""
¿Qué es @property?
Es un decorador que convierte un método de clase en una propiedad (atributo de solo lectura),
gracias a este se puede acceder a un método como si fuera un atributo normal, sin tener que llamarlo con ().

¿Qué es @atributo.setter
Un setter en Python es un método especial que sirve para cambiar (asignar) el valor de un a
tributo de una clase, pero de forma controlada.
En lugar de acceder directamente a la variable interna (self._atributo), usamos el setter para 
validar o modificar lo que se le asigna.
"""
# Definir clase de ejemplo
class Fruta:
    def __init__(self, color, sabor, nombre):
        self._color = color
        self._sabor = sabor
        self._nombre = nombre

    def mostrarFruta(self):
        return print(f'''\nMostrar información de la fruta
Nombre: {self._nombre}
Sabor: {self._sabor}
Color: {self._color}''')


# *********************************************************************************************************************************************
# Definir método Get de forma Pythonica
    @property # Decorador de Property que indica que este atributo es una propiedad de nuestra clase.
    def color(self):
        return print(f'Color de la fruta: {self._color}')
# A la hora de realizar la llamada del método se podrá ver como un atributo y no como un método como tal.
# Ejemplo: Sin @property ->> fruta1.color()  | Con @property ->> fruta1.color


# *********************************************************************************************************************************************
# Definir método Set de forma Pythonica
    @color.setter # @nombre_atributo.setter
    def color(self, nuevo_color): # self, nueva_variable que recibirá el nuevo valor
        self._color = nuevo_color
# El método Set es identico al método de Get solo cambia un poco al generarlo y es con la siguiente:
    #  SINTAXIS:  @color.setter ->> @nombre_atributo.setter

    # Método get de sabor y nombre
    @property
    def sabor(self):
        return print(f'Sabor de la fruta: {self._sabor}')

    @property
    def nombre(self):
        return print(f'Nombre de la fruta: {self._nombre}')

    # Método Set de sabor y nombre
    @sabor.setter
    def sabor(self,nuevo_sabor):
        self._sabor = nuevo_sabor

    @nombre.setter
    def nombre(self,nuevo_nombre):
        self._nombre = nuevo_nombre

fruta1 = Fruta('Azul','Dulce','Mora Azul')
fruta1.color # Funcionamiento del decorador property
fruta1.mostrarFruta()

# Modificando el nombre usando Setter
fruta1.nombre = 'Piña'
fruta1.mostrarFruta() #->> Muestro la información del objeto