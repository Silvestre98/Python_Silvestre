'''
El encapsulamiento nos permite ocultar la información que almacena un objeto,
la información que almacena un objeto, también conocido como el estado del objeto

Para aplicar el concepto de encapsulamiento se deben aplicar dos características:
    a) Atributos protegidos o privados
        self._nombre ->> Atributo protegido
        self.__nombre ->> Atributo privado
    b) Crear los métodos conocidos como get (leer) y set(modificar)

El encapsulamiento permite evitar acceder directamente al estado a los valores de los atributos de nuestros objetos, a la
hora de elegir entre atributos privados o protegidos depende enormemente de las practicas de nuestros proyectos.
'''

class Coche:
    def __init__(self, marca, modelo, color):
        self.color = color # Atributo publico
        self._marca = marca # Atributo protegido ->> Si en dado caso el nombre del atributo especifica que es protegido o privado se deberá acceder
        self.__modelo = modelo # Atributo privado  | exclusivamente por medio de los métodos get y set, pero se aplican si estamos fuera de la clase.

    def conducir(self):
        return print(f'''
        Conduciendo:
        Color de carro: {self.color}
        Marca: {self._marca}
        Modelo: {self.__modelo}
    ''')
if __name__ == '__main__':
    # Creacion del coche
    auto = Coche('Mercedes','A15','Negro')
    auto.conducir()

    # No deberiamos acceder a los atributos que no sean publicos
    auto._marca = 'Volkswagen' # Esto no es una buena practica, atributo protegido.
    auto.color = 'Rojo'
    auto.__modelo = 'W12' # Ignoro la modificación que se le realizo al atributo.
    auto._Coche__modelo = 'Z15' # Forzar la modificación del atributo (Mala practica).
    auto.conducir()