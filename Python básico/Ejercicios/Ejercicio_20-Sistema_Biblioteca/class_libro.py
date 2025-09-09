# Creación de la clase de libro

class Libro:
    # Método constructor
    def __init__(self,tituloLibro:str,autorLibro:str,generoLibro:str):
        # Creación de atributos
        self._tituloLibro = tituloLibro
        self._autorLibro = autorLibro
        self._generoLibro = generoLibro

    # Métodos de encapsulamiento get
    @property
    def tituloLibro(self):
        return self._tituloLibro

    @property
    def autorLibro(self):
        return self._autorLibro

    @property
    def generoLibro(self):
        return self._generoLibro