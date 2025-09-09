'''
Crear un programa que me pueda contar cuantos objetos se han creado usando la clase
'''

class Persona:
    # Se crea la variable de atributo de clase que en este caso es mi contador
    contador_persona = 0
    # Definición de atributos de clase
    def __init__(self, nombre, apellido):
        # Contador de clase se manda a llamar con el mismo nombre de la clase, ya que este no pertenece al método y sino a la misma clase.
        Persona.contador_persona += 1
        # Asignación de los atributos
        self.id = Persona.contador_persona
        self.nombre = nombre
        self.apellido = apellido
    # Mostrar en consola los atributos de los objetos de la clase
    def mostrar_persona(self):
        print(f'Datos persona: {self.id}, {self.nombre}, {self.apellido}')

# Creación de los objetos
persona_1 = Persona('Silvestre','Lopez')
persona_2 = Persona('Morgan','Perrito')

# Mostrar información de los objetos567
persona_1.mostrar_persona()
persona_2.mostrar_persona()

# Imprimir el valor del contador de persona de la Clase
print(f'Número de personas en la clase: {Persona.contador_persona}')