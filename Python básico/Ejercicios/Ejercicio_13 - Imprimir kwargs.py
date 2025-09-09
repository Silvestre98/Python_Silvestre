# Crear una función que me permita imprimirla información de una persona por medio de una función con kwargs

def imprimir_informacion_persona(**kwargs):
    print('Imprimiendo información')
    for key, values in kwargs.items(): # se recorre el kwargs y se le realiza el unpacking al diccionario.
        print(f'Key: {key} - Value: {values}')


# Mandar a llamar a la función
imprimir_informacion_persona(nombre='Silvestre',apellido='Lopez Vazquez',edad=27,grado='Ingeniero')

imprimir_informacion_persona()