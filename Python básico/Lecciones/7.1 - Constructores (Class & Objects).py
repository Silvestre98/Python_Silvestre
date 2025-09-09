# Constructores

'''
Un constructor es un método especial y se utiliza para crear un objeto, o instanciar una clase, además nos puede servir
para crear e inicializar los atributos de un nuevo objeto.

Por ejemplo __init__ que es un método especial o de tipo dunder (Double underscore o doble guion bajo) que sirve para inicializar una clase,
y se les conoce como métodos magicos porque realizan varias tareas y parece que las realizan con magia, en este caso creará los atributos y los inicializa.

Los constructores de clase se manda a llamar de forma automática.

    Sintaxis:
    Class NombreDeLaClase:
        def __init__(self, parametro1, parametro2):
            self.parametro1 = parametro1
            self.parametro2 = parametro2
'''

# Creacion de clase con constructor
class Persona_2:
    def __init__(self, nombre, apellido): # Creación de método con init
        # Creación de atributos
        self.nombre = nombre
        self.apellido = apellido

    def saludar(self):
        print(f'Hola {self.nombre} {self.apellido}')
# Como estamos usando un constructor a la hora de crear nuestro objeto le debemos de pasar los parámetros para su correcta creación.
persona_1 = Persona_2('Silvestre','R´hyle')

persona_1.saludar()