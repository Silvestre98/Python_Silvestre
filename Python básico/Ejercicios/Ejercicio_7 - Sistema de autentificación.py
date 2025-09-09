"""
Crear un programa que sirva para auntentificar las claves de acceso de un usuario, se deben de definir las claves correctas de forma previa, el sistema debe de indentificar si existe algún
error a la hora de comprobar las claves y en que parte se originó el error, identificando los errores con detalle por ejemplo:
    - Sin error -> Bienvenido al sistema
    - Error password -> Error de password
    - Error usuario -> Error de usuario
    - Error de ambos campos -> Error de claves
"""

# 1.- Definir claves de usuario

USER_VALIDO = "Silvestre"
PASSWORD_VALIDO = "1234"

# 2.- Crear inicio de sistema
print("Inicio de Sesión")
inicio_usuario = input("Introducir su usuario: ")
contrase_usuario= input("Introducir contraseña: ")

# 3.- Validar claves del usuario
def validar_usuario(usuario,contrasenia):
    if (inicio_usuario == USER_VALIDO) and (contrase_usuario == PASSWORD_VALIDO):
        print(f"Bienvenido al Sistema {inicio_usuario}.")
    elif (inicio_usuario == USER_VALIDO) and (contrase_usuario != PASSWORD_VALIDO):
        print(f"Error de password")
    elif (inicio_usuario != USER_VALIDO) and (contrase_usuario == PASSWORD_VALIDO):
        print(f"Error de usuario")
    elif (inicio_usuario != USER_VALIDO) and (contrase_usuario != PASSWORD_VALIDO):
        print("Error de claves")
    else:
        print("Error fatal")

validar_usuario(inicio_usuario,contrase_usuario)