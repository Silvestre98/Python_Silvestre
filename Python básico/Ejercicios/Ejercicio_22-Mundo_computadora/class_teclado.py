from class_dispositivoEntrada import dispositivosEntrada

# Creación de la clase Teclado

class Teclado(dispositivosEntrada):
    # Contador de teclados
    contador_teclado = 0
    # Método constructor de teclado
    def __init__(self,marca,tipo_entrada):
        Teclado.contador_teclado += 1
        self.id_teclado = Teclado.contador_teclado
        super().__init__(marca,tipo_entrada)

# Método str para saber las especificaciones del teclado
    def __str__(self):
        return f'Teclado -> ID: {self.id_teclado}, marca: {self.marca}, tipo de entrada: {self.tipo_entrada}'

''' Se comenta el codigo para evitar que se ejecute en el main
# Prueba de clase
teclado1 = Teclado('Logitech','USB')
teclado2 = Teclado('Razer','USB')

print(teclado1)
print(teclado2)
'''