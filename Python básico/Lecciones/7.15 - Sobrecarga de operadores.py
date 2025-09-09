# Sobrecarga de constructores
'''
La sobrecarga de operadores significa que puedes redefinir cómo se comportan los operadores
cuando se usan con objetos de tus propias clases.

Métodos especiales para sobrecargar operadores

Algunos de los más comunes:

    __add__(self, other) → +
    __sub__(self, other) → -
    __mul__(self, other) → *
    __truediv__(self, other) → /
    __eq__(self, other) → ==
    __lt__(self, other) → <
    __gt__(self, other) → >
    __len__(self) → len(obj)
    __str__(self) → str(obj) o print(obj)
'''
# Sobrecarga de operador Add
# Creación de la clase
class Fruta:
    # Inicializador
    def __init__(self, nombre):
        self.nombre = nombre
    # Sobreescritura de método suma
    def __add__(self, otro):
        return self.nombre + otro.nombre

fruta_1 = Fruta('Piña')
fruta_2 = Fruta('Manzana')

print(fruta_1 + fruta_2) # Me genera la concatenación

# Visualizar método add
# obj1     +    obj2
# fruta_2.__add__(fruta_1)
