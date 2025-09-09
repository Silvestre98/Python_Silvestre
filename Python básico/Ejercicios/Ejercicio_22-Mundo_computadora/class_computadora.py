# Creación de la clase Computadora
from class_monitor import Monitor
from class_teclado import Teclado
from class_raton import Raton

class Computadora:
    # Contador de computadoras
    contador_compútadora = 0
    # Método constructor de computadoras
    def __init__(self,nombre,monitor,teclado,raton):
        Computadora.contador_compútadora +=1
        self.id_computadora = Computadora.contador_compútadora
        self.nombre = nombre
        self.monitor = monitor
        self.teclado = teclado
        self.raton = raton

    # Método str
    def __str__(self):
        return f'''{self.nombre}: {self.id_computadora}
{self.monitor}
{self.teclado}
{self.raton}'''

'''
# Prueba de código
teclado1 = Teclado('Logitech','USB')
raton1 = Raton('Terport','Bluetooth')
monitor1 = Monitor('Asus','AF14',24.7)
computadora1 = Computadora('Thunderobot',monitor1,teclado1,raton1)

print(computadora1)
'''