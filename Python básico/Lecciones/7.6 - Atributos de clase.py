# Atributos de clase
'''
En esta lección veremos las diferencias entre atributos de clase y atributos de estancias:

🔹 1. Atributos de instancia
    -Son propios de cada objeto (instancia) de la clase.
    -Se definen casi siempre en el método __init__.
    -Cada objeto puede tener valores distintos en esos atributos.

🔹 2. Atributos de clase
    -Son compartidos por todas las instancias de la clase.
    -Se definen fuera de __init__, directamente dentro de la clase.
    -Si cambias el atributo de clase, cambia para todos los objetos (a menos que lo sobreescribas en uno).
'''

class Persona:
    # Creación de atributo de clase
    atributo_class = 0

    def __init__(self,atributo_instancia):
        # Creación de atributo de instancia
        self.atributo_instancia = atributo_instancia

# Programa principal
if __name__ == '__main__':

    # Mostrar valor del atributo de la clase
    print(f'''Atributos de clase
    atributo de clase = {Persona.atributo_class}''')

    # Modificar valor del atributo de la clase
    Persona.atributo_class = 10
    print(f'''Atributos de clase modificado
    atributo de clase = {Persona.atributo_class}''')

    # Crear objeto de clase persona
    persona1 = Persona(20)

    # Acceder a los atributos
    print(f'Atributo de clase desde un objeto de la clase: {persona1.atributo_class}')
    print(f'Atributo de instancia desde un objeto de la clase: {persona1.atributo_instancia}')
