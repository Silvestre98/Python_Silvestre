# Atributos Dinámicos de Objetos
"""
Los atributos dinámicos son atributos que se le crean al objeto sin necesidad de que estos existan en su clase o plantilla
 de forma previa, por ejemplo:
"""
# Clase jugador
class Jugador:
    def __init__(self, nombre:str, clase:str, edad:int):
        self._nombre = nombre
        self._clase = clase
        self._edad = edad
    def mostrar_jugador(self):
        return print(f'''
La información del jugador es:
Nombre: {self._nombre}
Clase: {self._clase}
Edad: {self._edad}
''')

# Creación del objeto 1
jugador_1 = Jugador('Silvestre','Mago',27)

# Creación de Atributo dinámico:
setattr(jugador_1, 'Nuevo_atributo', 'Valor_nuevo_atributo')

# Creación del objeto 2
jugador_2 = Jugador('Ozzy','Hechizero supremo',76)

# Mostrar la informacion de ambos objetos:
# Podemos ver que ambos objetos tienen los mismos atributos, pero al objeto 1 le hace falta un atributo.
jugador_1.mostrar_jugador()
jugador_2.mostrar_jugador()

# Mostrar nuevo atributo

# Mostrar atributo directamente.
print(f'Nuevo atributo: {jugador_1.Nuevo_atributo}')

# Mostrar los atributos en forma de diccionario con el método magico de __dict__ .
print(f'Atributos el objetos 1: {jugador_1.__dict__}')