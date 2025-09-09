# Importacion de clases
from class_figuraGeometrica import *
from class_color import *

# Creación de la clase Rectangulo
class Rectangulo(FiguraGeometrica, Color):

    # Inicializador
    def __init__(self, ancho:int, alto:int, color:str):
        # Inicializar atributos de las clases heredadas
        FiguraGeometrica.__init__(self,ancho,alto)
        Color.__init__(self,color)

    # str
    def __str__(self):
        return f'Rectangulo -> Ancho = {self.ancho} y Alto = {self.alto}'

    # Área
    def areaRectangulo(self):
        area = self.ancho * self.alto
        return area