"""Se solicita crear una aplicación de salud y fitness que solicite los siguientes datos:
1.- Pasos
* Nombre del usuario
* Pasos caminados en el día

2.-
Ademas definiremos las siguientes constantes

META_PASOS_DIARIOS = 10000
CALORIAS_PASO = 0.04 ->> Valor aproximado en kilocalorias

3.-
Con los valores anteriores debemos calcular las calorias quemadas según los pasos caminados

calorias_quemadas = pasos_diarios * CALORIAS_PASO

4.-
Y Verificar la meta de los pasos diarios

meta_pasos_alcanzada = pasos_diarios >= META_PASOS_DIARIOS
    imprimir el siguiente texto si se alcanzo la meta de los pasos
Si    "Meta alcanzada felicidades los pasos que diste el dia de hoy es de: {meta_pasos_alcanzada}"
No    "Meta de pasos no alcanzada, pero tus pasos fueron de {meta_pasos_alcanzada}"
"""

# Inicio del programa

# 1.- Pedir Nombre del usuarios y sus pasos del día

nombreUsuario = input("¿Cual es tu nombre completo?: ")
pasosUsuario = float(input("¿Cuantos pasos diste el dia de hoy?: "))

# 2.- Definición de variables constantes

META_PASOS_DIARIOS = 10000 # Metas de pasos diarios
CALORIAS_PASO = 0.04 # Calorias quemadas por pasos aproximado

# 3.- Calcular las calorias quemadas según los pasos caminados

calorias_quemadas = CALORIAS_PASO * pasosUsuario
print (f'Calorias quemadas en total el dia de hoy {calorias_quemadas}')

# 4.- Varificar la meta de pasos dados el dia de hoy

verificar_pasos = "Felicidades "+nombreUsuario+" cumpliste la meta de pasos Diarios" \
                    if pasosUsuario >= META_PASOS_DIARIOS else \
                  "Lo siento por desgracia hoy con cumpliste con tu meta de pasos diarios, sigue intentandoló"
print(verificar_pasos)
