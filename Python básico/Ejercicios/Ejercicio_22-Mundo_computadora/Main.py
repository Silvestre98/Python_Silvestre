from class_raton import Raton
from class_teclado import Teclado
from class_monitor import Monitor
from class_dispositivoEntrada import dispositivosEntrada
from class_orden import Ordenes
from class_computadora import Computadora


# Prueba de código
teclado1 = Teclado('Logitech','USB')
raton1 = Raton('Terport','Bluetooth')
monitor1 = Monitor('Asus','AF14',24.7)
computadora1 = Computadora('Thunderobot',monitor1,teclado1,raton1)

teclado1 = Teclado('Terport','USB')
raton1 = Raton('Terport','Bluetooth')
monitor1 = Monitor('HP','AF14',24.7)
computadora2 = Computadora('Lenovo',monitor1,teclado1,raton1)

# Crear lista de computadoras
computadoras_lista  = [computadora1,computadora2]
orden_1 = Ordenes(computadoras_lista)
print(orden_1) # No imprime jajajajaja
