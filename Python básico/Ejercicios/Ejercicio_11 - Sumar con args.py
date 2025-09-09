# Crear un funcion que realice una suma usando argumentos variables

def suma_args (*args):
    resultado = 0 # Definir varible de resultado
    for i in args: # args es devuelto como una tupla por lo que se puede iterar
        resultado += i # suma acumulativa
    return print(f'El resultado de la suma es: {resultado}') # Devolver resultado

# Mandar a llamar a la función de suma 
suma_args(1,2,3,4,5)