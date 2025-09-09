# Creación de la clase Monitor
from numpy.ma.core import masked_print_option


class Monitor:
    # Contador de monitor
    contador_monitor = 0
    # Método constructor de la clase monitor
    def __init__(self,marca:str,modelo:str,tamanio:float):
        Monitor.contador_monitor += 1
        self._marca = marca
        self._modelo = modelo
        self._tamanio = tamanio
        self._id = Monitor.contador_monitor

    # Método str
    def __str__(self):
        return f'Monitor -> Marca: {self._marca} Modelo: {self._modelo} Tamaño: {self._tamanio}'

    # Get y Set marca
    @property
    def marca(self):
        return f'Marca del monitor: {self._marca}'
    @marca.setter
    def marca(self,nueva_marca):
        self._marca = nueva_marca

    # Get y Set modelo
    @property
    def modelo(self):
        return f'Modelo del monitor: {self._modelo}'

    @modelo.setter
    def modelo(self,nuevo_modelo):
        self._modelo = nuevo_modelo

    # Get y Set tamaño
    @property
    def tamanio(self):
        return f'Tamaño del monitor: {self._tamanio}'
    @tamanio.setter
    def tamanio(self,nuevo_tamanio):
        self._tamanio = nuevo_tamanio

''' Se comenta el codigo para evitar que se ejecute en el main
# Prueba de clase
monitor1 = Monitor('Asus','AF23',24.7)
print(monitor1)
'''