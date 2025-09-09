# Clases y objetos
'''
Un objeto es una representación de una entidad de la vida real en nuestro programa.

Para crear un objeto primero necesitamos crear una clase o plantilla.

Una clase representa las características en común de nuestros objetos, es una abstracción.

Por ejemplo, si deseamos construir un edificio primero necesitamos crear los planos (clase) de este mismo los cuales se podría decir que son nuestra plantilla,
y despúes a partir de estos crear más edificios iguales (objetos).

Una clase se compone de atributos y métodos:

    - Los ATRIBUTOS son las características de nuestros objetos.
    - Los MÉTODOS son las acciones que pueden realizar nuestros objetos,
      en sí, estas acciones son funciones, pero cuando se asocian con una clase se les llama métodos.

Una vez que hemos definido nuestra clase, podemos crear objetos, a esto se le llama instanciar una clase.

Los objetos se crean con el nombre de la clase
'''

# Creación de clase
class Persona: # Usar 'class' para crear la clase
    # Definir Métodos
    def inicializar_persona(self, nombre, apellido): # Self sirve para poder acceder a los atributos y métodos de nuestra clase.
        # Creamos los atributos de la clase.
        self.nombre = nombre # Por buenas practícas el nombre del atributo es el mismo que el nombre de nuestro parámetro.
        self.apellido = apellido

    def mostrar_persona(self):
        print(f'''Persona:
        Nombre: {self.nombre}
        Apellido: {self.apellido}
        ''')

# Crear objetos usando nuestra plantilla de Persona.
if __name__ == '__main__':
    # Crear objeto vacio en memoria
    persona1 = Persona()
    # Asignar los atributos
    persona1.inicializar_persona('Silvestre','Lopez Vazquez')
    # Mostrar persona
    persona1.mostrar_persona()

# Ejercicio de creación de segundo objeto de persona
if __name__ == '__main__':
    # Crear objeto de persona 2
    persona2 = Persona()
    # Asignar valores a los atributos
    persona2.inicializar_persona('Ozzy','Osbourne')
    # Mostar persona 2
    persona2.mostrar_persona()

    persona3 = Persona()
    persona3.inicializar_persona('Dave','Mustaine')
    persona3.mostrar_persona()

# Antes de cualquier cosa se deben de inicializar los valores de cada uno de nuestros objetos antes de realizar cualquier acción con ellos.

"""
¿Qué es __name__?

Es una variable especial que Python define en cada módulo.
Si el archivo se ejecuta directamente (python archivo.py), entonces __name__ vale '__main__'.
Si el archivo se importa desde otro (import archivo), entonces __name__ vale 'archivo' (el nombre del módulo).

¿Qué hace if __name__ == '__main__':?

Compara ese valor.
Verdadero → ejecuta el bloque: estás corriendo el archivo como programa principal.
Falso → no ejecuta el bloque: el archivo fue importado y solo se cargan funciones/clases sin “hacer cosas” de inmediato.

Paso a paso del intérprete

Cargas mi_modulo.py.
Python pone __name__ = '__main__' si lo ejecutas; o __name__ = 'mi_modulo' si lo importas.
Ejecuta el código de arriba a abajo.
Llega al if __name__ == '__main__'::
Si es True, corre el código indentado (tu “programa”).
Si es False, lo salta (evitas efectos al importar).

¿Para qué sirve en la práctica?

Evitar que “se ejecute todo” al importar un módulo.

Dejar un punto de entrada claro para tu script/CLI:
"""