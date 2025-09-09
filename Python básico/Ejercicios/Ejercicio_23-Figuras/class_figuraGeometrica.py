# Creación de clase figura geometrica
class FiguraGeometrica:
    # Inicializador
    def __init__(self, alto:int, ancho:int):
        self._alto = alto
        self._ancho = ancho
    # __str__
    def __str__(self):
        return f'Alto = {self._alto}, Ancho = {self._ancho}'

    # Get y Set Alto
    @property
    def alto(self):
        return self._alto
    @alto.setter
    def alto(self,nuevo_alto):
        self._alto = nuevo_alto

    # Get y Set Ancho
    @property
    def ancho(self):
        return self._ancho
    @ancho.setter
    def ancho(self,nuevo_ancho):
        self._ancho = nuevo_ancho