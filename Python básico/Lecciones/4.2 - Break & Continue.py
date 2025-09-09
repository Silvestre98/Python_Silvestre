# Break y Continue


# Ejemplo de Break
print("Break")
for numero in range(1,10,1):
    if numero % 2 == 0:
        print(numero)
        break # Rompe el programa, ya no continuará con las iteraciones porque el Break rompe el programa


'''
¿Qué hace?
Cuando el programa encuentra continue dentro de un bucle, salta la iteración actual y pasa directamente a la siguiente,
sin ejecutar el código que queda después de continue en esa vuelta.

- Continue no termina el bucle, solo omite el resto del código en esa vuelta.
- Es útil cuando quieres ignorar casos específicos y seguir iterando
'''
# Ejemplo de Continue
print("Continue")
for numero in range(1,10,1):
    if numero % 2 != 0: # Si el número es impar no se imprimirá, pero gracias al Continue saltará a la siguiente interación.
        continue # Sirve para saltar ciertas condiciones sin romper el bucle completo (a diferencia de break, que lo detiene).
    print(numero)

# Otro ejemplo de Continue
# En caso de encontrar vacios en la Lista no los imprimirá directamente los saltará y seguirá buscando valores correctos en la lista
nombres = ["Juan", "", "Ana", "Pedro", "", "Luis", " "]
for nombre in nombres:
    if nombre == "" or nombre == " ":
        continue  # Salta los vacíos
    print(f"Procesando: {nombre}")
