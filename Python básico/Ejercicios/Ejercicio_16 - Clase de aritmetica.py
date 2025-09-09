# Crear una clase que me permita realizar las opercaciones aritmeticas básicas.

class Aritmetica:
    # Método de asignacion de valores
    def valoresNumericos(self,number1,number2):
        #Atributos
        self.number1 = number1
        self.number2 = number2
    # Método de suma
    def Suma_(self):
        resultado = self.number1 + self.number2
        return print(f'Suma: {self.number1} + {self.number2} = {resultado}')
    # Método de resta
    def Resta_(self):
        resultado = self.number1 - self.number2
        return print(f'Resta: {self.number1} - {self.number2} = {resultado}')
    # Método de division
    def Division_(self):
        resultado = self.number1 / self.number2
        return print(f'Division: {self.number1} / {self.number2} = {resultado}')
    # Método de multiplicación
    def Multiplicacion_(self):
        resultado = self.number1 * self.number2
        return print(f'Multiplicacion: {self.number1} * {self.number2} = {resultado}')

# Llamada a los metodos
if __name__ == '__main__':
    numeros = Aritmetica()
    numeros.valoresNumericos(5,10)
    numeros.Suma_()
    numeros.Resta_()
    numeros.Division_()
    numeros.Multiplicacion_()

# Crear una clase con inicializador de metodo magico que realice las operaciones aritmetica de potencia

class Artimetica2:

     def __init__(self, numero1:int,numero2:int):
         self.numero1 = numero1
         self.numero2 = numero2

     def potencia(self):
        resultado = self.numero1 ** self.numero2
        return print(f'Potencia de {self.numero1} elevado veces {self.numero2} = {resultado}')

operacion = Artimetica2(2,3)
operacion.potencia()