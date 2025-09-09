# Módulos

'''
Un módulo en Python es simplemente un archivo .py que contiene funciones, clases o variables que puedes importar y usar en otros archivos.
Puedes dividir tu código en varios archivos (módulos) y luego importarlos según sea necesario.
'''

# Importacion del modulo en especifico la funcion
#from Lecciones.3 - Modulo import suma_mod

# Importar el modulo completo
import Modulo

# Funcion de suma
def suma_mod (x,y):
    resultado = x+y
    return resultado


#  Formas comunes de importar:

# Importar todo el módulo
import math
print(math.pi)

# Importar solo una parte
from math import pi
print(pi)

# Importar con alias
import numpy as np
print(np.array([1, 2, 3]))