 # Listas ->> [1,2,3]

""" Las Listas se definen con corchetes [].
Las Listas son colección ordenada y mutable de elementos, una LISTA puede contener diferentes 
tipos de elementos [Str, Int, Float, Bool y Var]. """

# Sintaxis
mi_lista = ['elemento1', 'elemento2', 'elemento3']

# Ejemplo
Lista_Integer = [1,2,3,4,5]
Lista_Strings = ["manzana","piña","sandia","banana"]
Lista_Mixta = [1,"Manzana",3.0,[4,5],True]
Lista_Listas = [[1,2],['a','b'],[3.1416,2.71828],['palabra','palabra2']]

# Definir lista vacia
listaVacia = []

# Operaciones posibles con lista

# 1.- Largo o longitud de la lista.
print(f'Longitud de lista: {len(Lista_Integer)}\n')

# 2.- Acceder a los elemento de la lista por índices.
print(f'Acceder al índice 4 de la Lista: {Lista_Integer[4]}')

# 3.- Acceder a los elementos de la lista por medio de índices negativos.
#   [1, 2, 3, 4, 5] ->> lista
#   -5 -4 -3 -2- 1  ->> ïndices negativos, se usan si se quiere acceder de forma más rápida a los últimos valores de la lista.
print(f'Acceder por medio índice negativos -1 de la Lista: {Lista_Integer[-1]}')

# 4.- Modificar elementos de la lista.
print(f'\nAntes de modificar: {Lista_Integer}')
Lista_Integer[2] = 30
print(f'Despúes de modificar: {Lista_Integer}\n')

# 5.- Agregar elementos a la lista.
Lista_Integer.append(6)
print(f'Agregando elementos a la lista: {Lista_Integer} ->> Se agrego el número 6\n')

# 6.- Añadir un nuevo elemento a la lista en un índice especificó.
Lista_Integer.insert(0,-1)
print(f'Inserción de elemento por medio del índice: {Lista_Integer} ->> Se inserto el -1 en la posición 0.\n')

# 7.- Eliminar elementos de una lista usando remove
# En este método no usa un índice como tal, sino que directamente se le pasa el valor que se desea eliminar de la lista.
Lista_Integer.remove(-1)
print(f'Eliminacion del -1 por medio del método remove: {Lista_Integer}')
# Eliminación de elemento por índice de la lista usando el método pop.
Lista_Integer.pop(2)
print(f'Eliminación del elemento de la lista usando método pop: {Lista_Integer} ->> se elimino el índice 2')
# Eliminación por medio de la palabra 'del' que se realiza por medio de índices.
del Lista_Integer[4]
print(f'Eliminacion de elemento por medio de "Del" {Lista_Integer} ->> se elimino el indice 4\n')

# 8.- Obtener Sublistas, son listas derivadas de otras listas
Sublista_Integer = Lista_Integer[0:2] # las sublistas se crean de la siguiente manera [índice inicial, índice final - 1]
print(f'La sublista es: {Sublista_Integer}\n')

# 9.- Ordenar los elementos de la lista de forma alfabetica.
print(f'Lista original {Lista_Strings}')
Lista_Strings.sort()
print(f'Lista ordenada {Lista_Strings}')
# Ordenar la lista de forma descendente
Lista_Strings.sort(reverse=True)
print(f'Lista ordenada de forma descendente {Lista_Strings}\n')


# Notas extras
# Remove
print("Notas Remove")
'''
El método remove tiene dos puntos a considerar:
  1.- Solo removerá un elemento de la lista, si en mi lista existen dos elementos iguales solamente uno será removido.
  2.- El elemento a remover será el primer elemento encontrado de Izquierda a Derecha.
     Ejemplo: 
     si tengo una lista de la siguiente forma [a,e,o,i,o,u] y quiero eliminar la 'o', y uso remove
     solamente me eliminará el primer elemento de la 'o' que seria el del índice 2.
'''
Lista = ['a','e','o','i','o','u']
print(f'Lista antes de Remove {Lista}')
Lista.remove('o')
print(f'Lista después de Remove {Lista}')