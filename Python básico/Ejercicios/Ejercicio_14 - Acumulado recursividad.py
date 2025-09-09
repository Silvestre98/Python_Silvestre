# 1.- Sumar todos los elementos de una lista
'''
Objetivo: Crea una función recursiva que reciba una lista de números y retorne la suma total.

🔸 Entrada: [1, 2, 3, 4]
🔸 Salida esperada: 10
'''
# Variables
listaNumeros = [1,2,3,4]

# Crear función
def suma_acumulada (lista):
    # Caso base
    if (len(listaNumeros) - i) == 0 :
        return 0
    # Caso recursivo

# 2.- Potencia con recursividad
'''
Objetivo: crear una función que me de la potencia de un número de forma recursiva.
'''

def potencia_recursiva (base:int,exponente:int):
    # Caso base
    if exponente == 0:
        return 1
    else:
        return base * (base, exponente - 1)