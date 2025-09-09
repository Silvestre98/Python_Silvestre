# Compresión de listas o list comprehension

'''
La compresión de listas es una forma concisa y eficiente de crear listas a partir de otros iterables (listas, sets, tuplas o diccionarios),
permite filtrar elementos y aplicar expresiones a cada elemento de un iterable, de manera muy legible y en una sola linea de código.
'''

#Sintaxis
#[nueva_expresion for elemento in iterable if condicion]

'''
nueva_expresion: Es la expresion que define como se modifica o procesa cada elemento del iterable
elemento: Variable que representa cada elemento del iterable original
iterable: La sucesion o colección sobre la cual se itera
condicion: (opcional) Es una condición para filtrar los elementos del iterable
'''

# Ejemplo
listaNumeros = [1,2,3,4,5,6]
listaPares = [i for i in listaNumeros if i % 2 == 0]
''' 
for i: es la variable que recorrerá mi listaNumeros.
listaNumeros: es mi lista que la variable i irá recorriendo.
if: es la condicion que se deberá cumplir para que el elemento que esta siendo iterado se pueda unir a la nueva lista.
i: la i inicial hace referencia a los elementos que serán almacenados en la listaPares siempre y cuando cumplan la condición del if.
'''
print(listaPares)



# Compresion de listas con for anidados
''' Sirve para trabajar con estructuras anidadas como listas de listas (Matrices, Tablas, Arreglos bidimensionales, etc...)'''

# Ejemplo de aplanar una matriz
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Convertir en una sola lista
listaPlano = [num for fila in matriz for num in fila] # aqui se anidan los ciclos for
print(f'Matriz plana: {listaPlano}')

# Pares ordenados
letras = ['x','z','y']
numeros =[1,2,3]

# Crear los pares
paresOrdenados = [(i, j) for i in letras for j in numeros] # Convinar ambos arreglos
print(f'Pares Ordenados: {paresOrdenados}')



# Compresión de diccionarios
'''La sintaxis es muy parecida a la de listas, pero con clave:valor en lugar de solo un valor.'''

# Sintaxis
#{clave: valor for elemento in iterable if condición}

# Ejemplo 1: Crear un diccionario con numeros y los cuadrados de estos numeros

cuadradosDic = {i: i**2 for i in listaNumeros}
print(f'Compresion de diccionarios: {cuadradosDic}')

# Ejemplo 2: Filtrar y transformar un diccionario existente

# Creacion de diccionario
personas = {
    'Ana':22,
    'Juan':26,
    'Mateo':25,
    'Yanet':22,
    'Jaz':20,
    'Ricardo':27
}

# Filtrar menores que 25 años
menoresVenticinco = {nombre: edad for nombre, edad in personas.items() if edad<25}
# Con items se desempaquetará el diccionario en forma de tupla usando el unpacking
print(f'{menoresVenticinco}')