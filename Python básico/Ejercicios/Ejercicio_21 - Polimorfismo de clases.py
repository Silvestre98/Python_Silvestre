# Polimorfismo

'''
Crear 3 clases, en las que 2 serán clases hijas de la clase padre y que en cada una de ellas sobre escriban el mismo método.
'''
# Creación de clases
class Animal: # Clase padre
    def hacer_sonido(self): # Método de clase padre
        return 'Gruñido'

class Perro(Animal): # Clase hija
    def hacer_sonido(self): # Método de clase hija
        return 'Guau Guau'

class Gato(Animal):  # Clase hija
    def hacer_sonido(self): # Método de clase hija
        return 'Miau Miau'

# Creación de objetos
animal1 = Animal()
animal2 = Perro()
animal3 = Gato()

# Ejecución de metodos
print (f'Soy un animal: {animal1.hacer_sonido()}')
print (f'Soy un perro: {animal2.hacer_sonido()}')
print (f'Soy un gato: {animal3.hacer_sonido()}')
