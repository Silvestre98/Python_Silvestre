# Manejo de Excepciones
'''
El manejo de excepciones en Python es la forma de controlar errores que ocurren durante la ejecución
del programa para que no se detenga bruscamente.

🔹 Concepto Básico
    Una excepción es un evento que ocurre cuando el programa encuentra un error en tiempo de ejecución.
    print(10 / 0)  # ZeroDivisionError

🔹 Sintaxis básica
    try:
    # Código que puede lanzar una excepción
except TipoDeError:
    # Qué hacer si ocurre ese error
'''
from sys import exception

from pyexpat.errors import messages

# Error de división entre Cero
# a =10/0
# print(a)

# Ejemplo de uso
try: # Envolvemos el posible error con el 'Try | Except'
    a = 10 / 0
    print(a)
except Exception as e: # Exception es la clase que se encargará de manejar los errores (Captura el error que se tuvo).
    print(f'Ocurrio un error: {e}\n') # En consola ya no sale el erro en rojo porque ya se está
                                    # manejando de manera adecuada el error.




# Ejemplo de posibles caso invalido y validos con diferentes tipos de variables
# No da error porque Python soporta la multiplicación de str por int, pero si daria error si se hiciera de str * str
try:
    a = 10
    b = '10'
    print(f'{a * b}\n')
except Exception as e:
    print(f'Error en: {e}')

# int / str → Error (TypeError), porque no está definido.
# str * str → Error (TypeError), porque no es posible multiplicar cadenas
# int * str → Válido, porque Python interpreta la multiplicación como "repetir la cadena N veces".




# Manejo de errores con Multiples Excepciones
try:
    a = 10
    b = '10'
    print(f'{a / b}')

except TypeError as e: # Manejo de error en tipo de variables
    print(f'TypeError - Error en: {e}\n')

except ZeroDivisionError as e: # Manejo de error en division entre cero
    print(f'ZeroDivisionError - Error en: {e}')

except Exception as e: # La clase de error más generica debería de ir al final para así poder revisar
                       # todas las excepciones anteriores.
    print(f'Exception - Error en: {e}')




# Bloques Else y Finally

# Else: En caso de no tener ninguna clase de error se ejecuta el bloque de código de else.
resultado = None
try:
    numero_1 = 10
    numero_2 = 20
    resultado = numero_1 + numero_2
    print(f'La suma de numero 1 y numero 2 = {resultado}')

except TypeError as e:
    print(f'TypeError - Error en: {e}')

except Exception as e:
    print(f'Exception - Error en: {e}')

else: # Se ejecuta sino ocurre ninguna Excepción
    print('Código correcto\n')


# Finally

# Finally: a diferencia de else este bloque de código siempre será ejecutado
resultado = None
try:
    numero_1 = 10
    numero_2 = '20'
    resultado = numero_1 + numero_2
    print(f'La suma de numero 1 y numero 2 = {resultado}')

except TypeError as e:
    print(f'TypeError - Error en: {e}')

except Exception as e:
    print(f'Exception - Error en: {e}')

finally: # Se ejecuta siempre sin importar que se ejecutará anteriormente un error
    print('Código Finally')




# Creación de clases de Excepciones personalizadas

# Se crea apartir de las clases Exception o BaseException, lo más común es usar la primera.
class Numeros_Identicos_Exception(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje) # Usar método de la clase padre
        # Tambien se puede hacer así
        # self.message = mensaje



# Usar mi clase de exception
try:
    a = int(input('Primer numero: '))
    b = int(input('Segundo numero: '))
    if a == b:
        raise Numeros_Identicos_Exception('Numeros identicos confirmado') # raise nos permite lanzar o arrojar una exception.

except TypeError as e:
    print(f'TypeError - Error en: {e}')

except Exception as e:
    print(f'Exception - Error en: {e}')