# Herencia
'''
La herencia en Programación Orientada a Objetos (POO) funciona como en la vida real: una clase hija (o derivada)
hereda atributos y métodos de una clase padre (o base).

    🔹Clase padre (superclase): contiene atributos y métodos generales.
    🔹Clase hija (subclase): hereda todo lo de la clase padre y puede:
        Usar lo heredado tal cual.
        Extenderlo (agregar nuevos métodos/atributos).
        Sobrescribirlo (cambiar el comportamiento de un método heredado).
'''

# Clase Padre o SuperClase
class Animal:

    def comer(self):
        print('Como muchas veces al día')

    def dormir(self):
        print('Duermo muchas horas')

# Clase Hija
class Perro(Animal): # Se debe de indicar dentro de un par de paréntesis su clase padre
    def ladrar(self):
        print('Puedo ladrar')

# Creación de objeto con la clase Padre
lemur = Animal() # Mi objeto lemur puedo acceder a los métodos de la CLASE PADRE, pero no a los de la CLASE HIJO
                 # por qué esta instanciado en la CLASE PADRE.
# Manipulación de los métodos
lemur.comer()
lemur.dormir()


# Creación de objeto con la clase Hijo
morgan = Perro() # Mi objeto 'morgan' puede acceder a los métodos de la CLASE PADRE e HIJO porque esta instanciado
                 # en la CLASE HIJO por lo que hereda los métodos de la CLASE PADRE.
# Manipulación de métodos
morgan.dormir()
morgan.comer()
morgan.ladrar()