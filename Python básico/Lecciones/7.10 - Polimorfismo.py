# Polimorfismo
'''
¿Qué es el polimorfismo?

La palabra polimorfismo viene del griego: poly (muchos) y morphos (formas).
En POO significa que un mismo método o acción puede comportarse de distintas maneras según el objeto que lo use.
En otras palabras: diferentes clases pueden tener métodos con el mismo nombre, pero cada clase ejecuta su propia versión del método.

Tipos de polimorfismo

1.- Polimorfismo por sobreescritura (override)
   🔹 Una subclase redefine un método de la clase padre.
        Ejemplo: hacer_sonido en Perro y Gato.

2.- Polimorfismo por sobrecarga (overload) (Python no lo soporta directamente)
    🔹Un método con el mismo nombre pero diferentes parámetros.
        En Python se simula con valores por defecto o *args / **kwargs.

3.- Polimorfismo de clases abstractas (interfaces en otros lenguajes)
    🔹 Se define un método en una clase base abstracta y cada subclase lo implementa de su forma.
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