# Sobre escritura de métodos
'''
¿Qué es la sobreescritura de métodos?

La sobreescritura de métodos ocurre cuando una clase hija (subclase) define un método con el mismo nombre y
firma (parámetros) que un método de su clase padre (superclase).
De esta forma, cuando se usa el método en un objeto de la clase hija, se ejecuta el de la hija y no el del padre.

Cuando se realice la sobreescritura del método se tiene que nombrar al método tal cual esta en la clase padre, de lo contrario
simplemente estaría creando un método completamente diferente.
'''
# Clase Padre
class Animal:
    def hacer_sonido(self): # Método original
        print("Hago un gruñido")

# Clase Hija
class Perro(Animal):
    # Sobreescribimos el método hacer_sonido
    def hacer_sonido(self): # Sobrescritura de método
        print("Guau Guau")

# Clase Hija 2
class Gato(Animal):
    def hacer_sonido(self): # Sobrescritura de método
        print("Miau Miau")

# Creacion de objetos
animal = Animal()
perro = Perro()
gato = Gato()

# Cada clase usará su propio método hacer_sonido,  pero las clase hijas(Gato y Perro) sobreescribieron el método original
animal.hacer_sonido()  # → Hago un gruñido
perro.hacer_sonido()   # → Guau Guau
gato.hacer_sonido()    # → Miau Miau