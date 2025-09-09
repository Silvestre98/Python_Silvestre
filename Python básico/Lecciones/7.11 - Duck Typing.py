# Duck typing
'''
Es una función polimorfica, es decir, esta función puede recibir diferentes tipos de datos, en este caso recibirá diferentes tipos de objetos.
'''
# Clase Padre
class Animal:
    def hacer_sonido(self): # Método original
        print("Hago un gruñido")
# Clase Hija
class Perro(Animal):
    def hacer_sonido(self):
        print("Guau Guau")
# Clase Hija 2
class Gato(Animal):
    def hacer_sonido(self):
        print("Miau Miau")
class Pez(Animal):
    def nadar(self):
        print('Nadando...')
class Carro:
    def conducir(self):
        print('El auto avanza')

# Función polimorfica

# La función recibe un tipo de dato genérico, en este caso 'animal'
def hacer_sonido_animal(animal): #--> Recibe el tipo de dato genérico que podría llegar a ser un objeto.
    animal.hacer_sonido() #--> Por medio del método hacer_sonido podría llegar a usar cualquiera de los métodos de las clases. obviamente
                                 #    depende de qué clase se instancie el objeto (Animal, Perro o Gato).

# Ejemplo Correcto
gato = Gato() # Crear objeto
# Mandar a llamar la función polimorfica.
hacer_sonido_animal(gato)


# Ejemplo Clase Hijo sin el método
pez = Pez() # Crear objeto
# Mandar a llamar la función polimorfica.
hacer_sonido_animal(pez) # Al no tener un método propio de hacer_sonido directamente manda a llamar al método del padre.

# Ejemplo Clase sin el método
carro = Carro()
# Al no tener el método en la clase dará error, porque aquí lo importante no es la clase que lo este instanciando
# sino que la clase tenga el método que estamos llamado en este caso hacer_sonido.
hacer_sonido_animal(carro)