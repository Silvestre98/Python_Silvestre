# Tuplas o Tuple ->> (a,b,c) ó a,b,c

"""
Las Tuplas son similares a las listas con excepción que no son mutables, por lo que al crearse la tupla es imposible modificarla de algún modo,
pero sí pueden llegar a ser heterogeneas.
Suelen ser utilizadas para crear colecciones que no debén tener modificaciónes atrávez del tiempo.
"""
# Sintaxis
mi_tupla = ('a','b','c') # ->> Creación de tupla con parentesis.
mi_tupla_sin_parentesis = 'a','b','c' # ->> Creación de tupla sin parentesis.

# Ejemplos de tuplas
tupla_int = (1,2,3,4,5)
tupla_str = 'Hola','mundo'
tupla_float = (3.1416,2.71828,.333)
tupla_mixta = 'Hola',1,3.1416,'x',False,[1,2,3]
tupla_un_elemento = 1, # En este caso se pueden llegar a crear una tupla de un solo elemento, pero se le debe poner la coma, ya que esta no es opcional.
tupla_vacia = () # Definir tupla vacia

# Desempaquetanto Tuplas o Unpacking tuple
'''Me permite asignar los elementos que contiene mi tupla a distintas variables para poderlos manipularlos.'''

# Tupla a desempaquetar
producto = ('P001','Camisa',20.00) # Tupla a desempaquetar

# Variables donde se desmpaquetaran las tuplas
codigo,descripcion,precio = producto # Desempaquetando la tupla en cada una de estas variables, el contenido se almacenará justo como está dentro de la tupla.

#Comprobar que se desempaqueto correctamente
print(f'Tupla sin desempaquetar: \n{producto}') # Tupla sin desempaquetar

print(f'''
Tupla desempaquetada:
 Codigo:      {codigo}
 Descripción: {descripcion}
 Precio:      {precio}
      ''')