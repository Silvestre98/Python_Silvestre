'''
Las variables pueden tener un alcance global o local dependiendo de donde y como se declaren, las variables globales son aquellas
que están disponibles a lo largo de todo el programa, mientras que las variables locales sólo están disponibles dentro del bloque
de código o la función donde fueron declaradas.
'''

# Variable global ->> Definida fuera de cualquier metodo o función.
contadorGlobal = 0

def incrementar_contador ():
    # Declaramos una varible local ->> Definida dentro de una función.
    contadorLocal = 0

    # Usar variable global dentro de la función.
    global contadorGlobal # La palabra reservada "Global" me indica que usaré la variable declarada fuera de la función.

    # Incrementar la variable local
    contadorLocal +=1
    # Incrementar la variable global
    contadorGlobal +=1
    return print(f'Contador local: {contadorLocal} -- Contador global: {contadorGlobal}')

incrementar_contador() # Se manda a llamar multiples veces para observar como la local es volatil y la global no lo es ya que conserva sus modificaciones.
incrementar_contador()
incrementar_contador()