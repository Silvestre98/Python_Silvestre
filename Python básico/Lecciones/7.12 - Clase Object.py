# Clase Object
'''
Todas las clases heredan implícitamente de object, aunque tú no lo escribas.
Es la superclase base universal.

¿Qué nos da la clase object?
La clase object proporciona un conjunto de métodos básicos que todas las clases heredan, por ejemplo:
    __str__() → Convierte el objeto en una cadena legible.
    __repr__() → Representación oficial del objeto (útil para depuración).
    __eq__() → Compara igualdad (==).
    __hash__() → Calcula el hash del objeto (para usar en diccionarios y sets).
    __init__() → Inicializa objetos (aunque vacío en object).
'''
# Crear clase de ejemplo
class Fruta:
    # Constructor de la clase
    def __init__(self,nombre,color):
        self.nombre = nombre
        self.color = color
    # Sobreescribir método __str__
    def __str__(self):
        return f'''Información:\n
Nombre: {self.nombre}
Color: {self.color}
Direcc. memoria: {super.__str__(self)}''' # mando a llamar directamente al método de la clase Object gracias a la palabra "Super",
                                       # es la que me permite acceder directamente al método de la Superclase.

# Código de prueba
fruta = Fruta('Piña','Amarilla')
# El método __str__ se manda a llamar automaticamente desde print
print(fruta)
print(fruta.__str__()) # Mandar a llamar al método de __str__ de esta forma seria redundante.