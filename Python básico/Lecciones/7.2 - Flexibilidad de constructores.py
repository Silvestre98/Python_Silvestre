'''
La sobre carga de constructores viene cuando a una clase le creamos multiples constructores, por ejemplo:
    class Aritmetica:
        ->> Constructor 1 <<-
        def __init__(self,number1):
            self.number1 = number1

        ->> Constructor 2 <<-
        def __init__(self,number1,number2):
            self.number1 = number1
            self.number2 = number2

Pero en estos casos Python tomará la definición del ultimo constructor por lo que ignorara los demás, los que se puede hacer es para crear en este caso objetos
con un solo parámetro, es que en la definición del constructor le pasemos valores iniciales a los parámetros como por ejemplo: None o 0

        def __init__(self,number1 = none,number2 = none):
            self.number1 = number1
            self.number2 = number2
'''
class Aritmetica3:
    # Método de asignacion de valores
    def __init__(self,numero_1 = None,numero_2 = None):
        #Atributos
        self.numero_1 = numero_1
        self.numero_2 = numero_2

    def suma__(self):
        resultado = self.numero_1 + self.numero_2
        return print(f'Resultado de la suma {resultado}')

operacion = Aritmetica3(2)

# Tambien le podemos asignar un valor directamente al segundo parametro
operacion.numero_2 = 1

operacion.suma__()