# Diccionario o Dictionary --> {key: value, key2: value2}

''' Los diccionarios son una colección de datos ordenada (apartir de la version 3.7 de python) y se almacenan en forma de llave:valor, es una estructura muy util
cuando necesitas asociar un conjunto de valores de claves o llaves que sirven como indices únicos.

        Los diccionarios no aceptan valores duplicados.
        Las llaves de los diccionarios deben de ser cadenas de texto y sus valores pueden ser de cualquier tipo de valor.
'''

# Sintaxis
mi_diccionario = {'clave1':'valor1','clave2':'valor2'} # Creación de un diccionario

# Ejemplo de diccionarios
dic_persona = {'nombre':'Silvestre','edad':'27 años','estatura':'180 cm','es_casado':False}
diccionario_vacio = {} # Diccionario vacio

# Operaciones básicas de los diccionarios.

# Mostrar diccionario completo
print(f'\nDiccionario original: {dic_persona}')

# Acceder a los elementos del diccionario de forma individual del diccionario.
print(f'Nombre: {dic_persona['nombre']}') # Se realiza mediante la llave
print(f'Edad: {dic_persona.get("edad")}') # Método get y con su llave
print(f'Estatura: {dic_persona.get('estatura')}\n')

# Modificar valores de los diccionarios
dic_persona['nombre'] = 'Juan'
print(dic_persona)

# Agregar nuevo elemento al diccionario
dic_persona['Profesión'] = "Ingeniero de Datos"

# Eliminar un elemento del diccionario ->> Se elimina la llave como el valor que estaba asociado
del dic_persona['es_casado'] # Usando 'del'
dic_persona.pop('estatura') #Usando metodo pop
dic_persona.popitem() # Remueve el ultimo valore creado en el diccionario
print(dic_persona)

# Iteración los elementos del diccionario, me dara las llaves y los valore del diccionario.
print('\nValores del diccionario por medio de items')
for llave, valor in dic_persona.items(): # Con items se desempaquetará el diccionario en forma de tupla usando el unpacking
    print(f'Llave: {llave}, Valor: {valor}')

#Obtener los valores del diccionario
print('\nValores del diccionarioa')
for valores in dic_persona.values():
    print(f'- Valor: {valores}')

#Obtener las llaves del diccionario
print(f'\nLlaves del diccionario')
for llaves in dic_persona.keys():
    print(f'- Llave: {llaves}')