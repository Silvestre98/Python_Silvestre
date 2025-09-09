# Creación de clase color
class Color:
    # Inicializador
    def __init__(self, color:str):
        self._color = color

    # Get y Set
    @property
    def color(self):
        return f'Color = {self._color}'
    @color.setter
    def color(self,nuevo_color):
        self._color = nuevo_color