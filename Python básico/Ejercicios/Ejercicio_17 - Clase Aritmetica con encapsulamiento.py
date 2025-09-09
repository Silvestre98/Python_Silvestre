# Usando la clase de Aritmetica del ejercicio pasado aplica los metodos Set y Get,
# asi como la privacidad de los atributos ya sean privados, públicos o protegidos

class Aritmetica:
    # Método de asignación de valores
    def __init__(self,number1,number2):
        # Proteger los atributos
        self._number1 = number1
        self._number2 = number2

# Aplicando el encapsulamiento
# Getter y Setter para cada atributo
    # Número 1
    # Get
    @property
    def numero1(self):
        return print(f'El número 1 es: {self._number1}')
    # Set
    @numero1.setter
    def numero1(self,nuevo_numero1):
        self._number1 = nuevo_numero1

    # Número 2
    # Get
    @property
    def numero2(self):
        return print(f'El número 2 es: {self._number2}')
    # Set
    @numero2.setter
    def numero2(self,nuevo_numero2):
        self._number2 = nuevo_numero2

# Métodos Aritmeticos
    # Método de suma
    def Suma_(self):
        resultado = self._number1 + self.number2
        return print(f'Suma: {self._number1} + {self._number2} = {resultado}')
    # Método de resta
    def Resta_(self):
        resultado = self._number1 - self.number2
        return print(f'Resta: {self._number1} - {self._number2} = {resultado}')
    # Método de division
    def Division_(self):
        resultado = self._number1 / self._number2
        return print(f'Division: {self._number1} / {self._number2} = {resultado}')
    # Método de multiplicación
    def Multiplicacion_(self):
        resultado = self._number1 * self._number2
        return print(f'Multiplicacion: {self._number1} * {self._number2} = {resultado}')

# Llamada a los metodos
if __name__ == '__main__':
# Cracion del objeto de Aritmetica
    valores_opraciones = Aritmetica(2,3)
# Accediendo a la infomación de cada uno de los numeros
    print('Acceder a los valores de las variables')
    valores_opraciones.numero1
    valores_opraciones.numero2

# Modificar valores
    print('\nModificando de las variables')
    valores_opraciones.numero1 = 9
    valores_opraciones.numero2 = 10

# Mostrar cambios
    print('\nAcceder a los valores modificados')
    valores_opraciones.numero1
    valores_opraciones.numero2