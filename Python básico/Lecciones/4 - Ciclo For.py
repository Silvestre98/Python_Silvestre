# Ciclo For
print("Ciclo For o en español Para")

# Ejemplo de funcionamiento
cadena_txt = "Hola mundo"

# Recorre cada uno de los caracteres de la cadena de texto uno por uno, también se podría decir que los recorre cada uno por medio de la iteración
for i in cadena_txt:
    print(i, end=" ")

# Ejercicio de For - Suma iterada
print("\nSuma iterada del rango de 1 - 10\n")

rango_suma = range(1,11)
sumaTotal = 0

for i in rango_suma:
    sumaTotal += i
print(sumaTotal)