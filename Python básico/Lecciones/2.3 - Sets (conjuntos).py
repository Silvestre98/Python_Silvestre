# Sets o Conjuntos ->> { 1, 2, 3}

""" Son colecciones de datos no ordenados por lo que el concepto de índices es inexistente para estos, almacena elementos únicos, pueden contener elementos heterogeneos
y son mutables, son muy útiles cuando debemos asegurarnos de que no existan elementos duplicados en nuestra colección.

    - Los duplicados no existen en el set.
    - Si intentas agregarlos, se ignoran, no se guardan, no se lanza error.
"""

# Sintaxis.
mi_set = {9,8,7} # Creación de un conjunto.

# Ejemplos de sets.
set_a = {1,2,3,4}
set_b = {3,'Juan',True,6.5}
set_duplicados = {1,2,1,'a','b','c','a'} # Set con elementos duplicados.
print(set_duplicados,"\n") # A la salida del print no contendrá elementos duplicados.

# Definir un set vacio
set_vacio = set() # De esta forma se define un set vacio.

# Agregar elemento al set.
mi_set.add(3)
print(f'Se agrego el valor 3 al Set: {mi_set}\n')

# Eliminar elemento.
mi_set.remove(3) # A no estar ordenado no se podria eliminar un elemento atraves del índice como normalmente se realizaría.
print(f'Se elimino el valor de 3 del set: {mi_set}\n')

# Iterar el Set.
print('Iteración del set:')
for i in mi_set:
    print(i,end=" ")

# Comprobar si existe un elemento en el set
print(f"\n\nExiste el valor de 4 en el set?: {4 in mi_set}\n") # se comprueba la existencia de un valor dentro del set.

# Largo del set
print(f'Largo del set: {len(mi_set)}\n')

# Los sets soportan operaciones matemáticas como lo son la teoría de conjuntos
print('''
***************************************************************************************************************\n
Operaciones con los Sets\n''')

# Creación de conjuntos
a = {1,2,3,4}
b = {3,4,5,6}
print(f'''
Conjunto a = {a}
Conjunto b = {b}
''')
# Union de conjuntos
union = a|b
print(f'Union de conjuntos a y b: {union}\n')

# Intersecióm de conjuntos
interseccion = a & b
print(f'Intersección a y b: {interseccion}\n')

# Diferencia de los conjuntos
diferencia = a - b
print(f'Diferencia de a y b: {diferencia}')

diferencia2 = b - a
print(f'Diferencia de b y a: {diferencia2}')