"""
Sistema de envios, que me calcule el valor del envío de acuerdo a dos condicionales:
    1.- El peso del paquete
    2.- El tipo de envío internacional o nacional
        - Envío nacional = 10 x peso de paquete
        - Envío intenacional = 20 x peso de paquete
Al final se deberá imprimir el costo total del envío
"""

# 1.- Pedir el tipo de envío que desea realizar el cliente asi como el peso de su paquete.
pesoPaquete = float(input("¿Cual es el peso en kg de su paquete que desea enviar?: "))
tipoEnvio = input("¿El destino de su envío es nacional o internacional?: ")

# 2.- Definir constantes de peso
envioInternacional = 20
envioNacional = 10

# 3.- Crear función para el problema
def calcularEnvio (peso,tipoDeEnvio):
    if tipoEnvio.strip().lower() == "nacional":
        totalEnvio= envioNacional * pesoPaquete
        return print(f"El costo del envío del paquete con un peso de: {pesoPaquete} kg, es de: {totalEnvio}")
    elif tipoEnvio.strip().lower() == "internacional":
        totalEnvio = envioInternacional * pesoPaquete
        return print(f"El costo del envío del paquete con un peso de: {pesoPaquete} kg, es de: {totalEnvio}")
    else:
       return print("Error Fatal")

calcularEnvio(pesoPaquete,tipoEnvio)
