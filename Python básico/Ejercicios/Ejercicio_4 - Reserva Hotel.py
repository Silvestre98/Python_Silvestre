"""
Se solicita crear un sistema de Reservación de un Hotel, se debe pedir la siguiente información al usuario:

+ Nombre completo
+ Días de estadia
+ Cuarto con vista al mar

El Hotel cuenta con la siguiente tarifa de cuarto

Cuarto sin vista al mar: $150.50 por dia
Cuarto con vista al mar: $190.50 por dia

El sistema debe de calcular el costo total de la estadía, dependiendo si escogió un cuarto con vista al mar o no, además de mostrar si es que escogió el cuarto con vista al mar.
"""

# 1.- Pedir información del cliente y de su estadía

nombreCliente = input("¿Cual es su nombre completo?: ")
diasEstadia = int(input("¿Cuantos días desea reservar?: "))
vista_al_Mar = input("¿Desea que su habitación tenga vista al mar?(Si/No): ")

#2.- Definir variables de costos por habitación

SIN_VISTA_MAR = 150.50
VISTA_MAR = 190.50

# 3.- Calcular el costo de estancia e indicar el concepto de la misma asi como ver si el cliente escogió vista al mar

vistaMar = True if vista_al_Mar.strip().lower()== "si" else False

totalEstadia = 0

if vistaMar:
    totalEstadia = diasEstadia * VISTA_MAR
else:
    totalEstadia = diasEstadia * SIN_VISTA_MAR

# Mostrar los detalles de la reservación
print(f'Nombre del huesped: {nombreCliente}\nDias de estancia: {diasEstadia}\nDesea vista a la playa: {vista_al_Mar}\nCosto total: {totalEstadia:.2f}')