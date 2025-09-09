# Funciones recursivas

'''
Una función recursiva en Python es una función que se llama a sí misma para resolver un problema.
La idea es dividir un problema grande en subproblemas más pequeños, hasta llegar a un caso base que
se pueda resolver directamente (y que detiene la recursión).

Reglas de funciones recursivas
    1.- Una funcion recursiva se debe de llamar a si misma
        def funcion_r():
            Caso base
            funcion_r(Caso recursivo)

    2.- Cada vez que la funcion se llama asi misma deberá de irse
        acercando a un caso base para asi poder salir del bucle que se crea.
        def mi_funcion (n)
            si n == 1 Entonces ->> Caso base
                regresa n
            sino
             mi_funcion(n-1) ->> Caso recursivo
             
Conceptos clave de recursión:

    Caso base obligatorio: evita que la recursión sea infinita.

    Llamada recursiva: la función se llama a sí misma con un problema más pequeño.

    Pila de llamadas: cada llamada se apila hasta llegar al caso base, y luego se resuelve en orden inverso.
'''

# Crear función recursiva
def fun_recursiva(numero):
    # Caso base:
    if numero == 1:
        return print(numero, end=" ")
    # Caso recursivo:
    else:
        print(numero, end=" ")
        return fun_recursiva(numero - 1)

# Mandar a llamar a la función
fun_recursiva(3)