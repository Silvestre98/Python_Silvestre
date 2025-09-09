# Funciones

'''
Las funciones son bloques de código para realizar una tarea en particular,
Las funciones se pueden reutilizar en diferentes partes del programa.
'''

# Sintaxis
# 1.- Definición de la función (verbo o acción)
def nombre_funcion (parametro_1:str, parametro_2:str): # con 'str' especifico el tipo de datos que debería de recibir el parametro
    # 2.- Cuerpo de la función(es el bloque de código que ejecutara la funcion
    resultado = print(parametro_1, parametro_2)
    # 3.- Valor que devuelve la función (opcional)
    return resultado
# 4.- Llamada a la función
prueba = nombre_funcion('Hola','mundo')

# Funciones con argumentos por nombre

def imprimir_persona (nombre:str, apellido:str, edad:int):
    print(f'''Persona
    Nombre: {nombre}
    Apellido: {apellido}
    Edad: {edad}''')

# Llamar la función pasando los argumento de forma posicional ->> Se pasarán los argumento de acuerdo a la posición que se les dio en la función.
imprimir_persona('Silvestre','Lopez Vazquez',27)

# Mandar a llamar la función usando argumentos por nombre
imprimir_persona(edad=23,nombre='Jennifer',apellido='Tapia')

# Argumento con valores por default
def imprimir_persona2 (nombre='', apellido = '', edad = 0): # Se agregaron los valor por default al crear la función.
    print(f'''Persona
        Nombre: {nombre}
        Apellido: {apellido}
        Edad: {edad}''')

imprimir_persona2('Ozzy')