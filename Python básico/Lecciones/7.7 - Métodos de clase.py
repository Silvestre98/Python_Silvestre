# Métodos de clase
"""
Es similar a los atributos de clase soló que en este caso los métodos de clase se asocian a la clase y no a los objetos,
los objetos si pueden acceder a estos métodos.

🔹 1. Métodos de instancia
    -Son los más comunes.
    -Reciben self como primer parámetro, que representa a la instancia (objeto).
    -Pueden acceder y modificar atributos de instancia y también ver atributos de clase.
    -Necesitas crear un objeto para usarlos.

🔹 2. Métodos de clase
    -Se definen con el decorador @classmethod.
    -Reciben cls como primer parámetro, que representa a la clase y no al objeto.
    -Pueden acceder y modificar atributos de clase, pero no los de instancia.
    -Se pueden llamar directamente desde la clase, sin necesidad de crear objetos.
"""
# Creacion de clase Animal
class Animals:
    # Creación de variable de contador
    contador_animal = 0
    # Creación de método constructor de instancia
    def __init__(self,nombre_especie,sexo,tamaño):
        # Asignar id mediante el contador
        Animals.contador_animal += 1
        self.id = Animals.contador_animal
        self.nombre_especie = nombre_especie
        self.sexo = sexo
        self.tamaño = tamaño

    '''
    Metodos de clase @Classmethod y @Staticmethod:
    🔹 1. @classmethod
        -Recibe cls como primer parámetro.
        -cls representa la clase misma, no un objeto.
        -Puede acceder y modificar atributos de clase, pero no atributos de instancia.
        -Se usa cuando quieres trabajar con la clase en general.

    🔹 2. @staticmethod
        -No recibe ni self ni cls automáticamente.
        -Es como una función normal dentro de una clase, que está ahí solo por organización.
        -No puede modificar atributos ni de clase ni de instancia (a menos que se los pases como argumentos manualmente).
        -Se usa cuando la función tiene relación lógica con la clase, pero no necesita acceder a sus datos.
    '''

    @staticmethod # Método estatico de clase
    def get_contador_animal():
        print(f'Animales en la clase (staticmethod): {Animals.contador_animal}')

    @classmethod # Método de clase
    def get_contador_clase(cls):
        print(f'Animales en la clase (classmethod): {cls.contador_animal}')


if __name__ == '__main__':
    # Crear el primer objeto de la clase
    animal_1 = Animals('Perro','Macho','Mediano')
    # Imprimir el valor del contador con el método estático
    animal_1.get_contador_animal()
    # Imprimir el valor del contador con el método de clase
    animal_1.get_contador_clase()
    # Imprimir el valor desde la instancia de la clase
    print(f'Animales en la clase (Instancia): {animal_1.contador_animal}')