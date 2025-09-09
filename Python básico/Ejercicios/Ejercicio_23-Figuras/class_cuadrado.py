# Importacion de clases
from class_figuraGeometrica import *
from class_color import Color

# Cracion de clase Cuadrado
class Cuadrado(FiguraGeometrica,Color):
    # Inicializador
    def __init__(self, lado:int, color:str):
        # Inicializar atributos de las clases heredadas
        FiguraGeometrica.__init__(self,lado,lado)
        Color.__init__(self,color)

    # STR
    def __str__(self):
        return f'Cuadrado -> Ancho: {self.alto} y Alto: {self.ancho}'

    # Área
    def areaCuadrado(self):
        area = self.ancho * self.alto
        return area