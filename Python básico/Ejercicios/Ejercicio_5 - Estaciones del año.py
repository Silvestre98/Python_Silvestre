"""
Crear una aplicación que de acuerdo número del mes ingresado me de la estación del año a la que pertenece dicho mes:

- 1,2 o 12 ->> Invierno
- 3, 4 o 5 ->> Primavera
- 6, 7 o 8 ->> Verano
- 9, 10 o 11 ->> Otoño

"""
# Pedir número del mes a evaluar
numeroMes = input("Introduce el número del mes que deseas obtener su estación: ")

# Designar a que estación de año pertenece el número
if numeroMes == '1' or numeroMes == '2' or numeroMes == '12':
    print("La estación que corresponde a este mes es Invierno")
elif numeroMes == '3' or numeroMes == '4' or numeroMes == '5':
    print("La estación que corresponde a este mes es Primavera")
elif numeroMes == '6' or numeroMes == '7' or numeroMes == '8':
    print("La estación que corresponde a este mes es Verano")
elif numeroMes  == '9' or numeroMes == '10' or numeroMes == '11':
    print("La estación que corresponde a este mes es Otoño")
else:
    print("El valor introducido no es valido")