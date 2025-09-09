# Argumentos variables

'''
En python, los argumentos variables permiten que una función acepte un número arbitrario de elementos. Hay dos tipos principales:

    1.- Argumentos posicionales variables *args: Permite pasar múltiples argumentos posicionales
        a una función, recibiéndolos como una tupla dentro de la función.

    2.- Argumentos con palabra clave **kwargs: Recibe los argumentos en forma de diccionario ( llave - valor o key - value)

    Los arteriscos se usan para en la firma del metodos *
    *args ->> Argument - tupla
    **kwargs ->> Keyword argument - (key - value) lo maneja como diccionario
'''

# Argumentos variables con *args

def superoheroe_superpoderes (superheroe:str, nombre:str, *args): # los args se reciben como parametros pero los devolvera como una tupla.
    print(f'Superheroe: {superheroe} - {nombre} - {args}')        # los args deben ser el ultimo parametro en ser ingresados en la función.
    for superpoderes in args: # Se puede llegar a iterar la tupla de los args.
        print(f'Super poder de {superheroe}: {superpoderes}')

# Llamar a la función
superoheroe_superpoderes("Spider-man",'Peter Parker','Sentido aracnido','Lanzar telaraña','Super fuerza','Super agilidad')

# Es opcional mandar los argumentos variables
superoheroe_superpoderes('Ghost Rider', 'Jonny Blazze') # Como no le paso ningún argumento la tupla la retorna vacia.


# Argumentos variables con **kwargs

def superheroe_superpoderes2 (nombre,*args,**kwargs):
    print(f'Nombre: {nombre} - {args} - más información: {kwargs}')

superheroe_superpoderes2('Batman','Batifamilia','Liga de la justicia',nombre_civil='Bruce',apellido='Wayne',ciudad='Gotica')

# No es necesario pasar args ni kwargs
superheroe_superpoderes2('Silvestre')