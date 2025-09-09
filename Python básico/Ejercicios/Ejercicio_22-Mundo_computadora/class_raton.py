from class_dispositivoEntrada import dispositivosEntrada

# Creación de la clase Raton

class Raton(dispositivosEntrada):
    # Contador de teclados
    contador_raton = 0

    # Método constructor de teclado
    def __init__(self, marca, tipo_entrada):
        Raton.contador_raton += 1
        self.id_raton = Raton.contador_raton
        super().__init__(marca,tipo_entrada) # Para no tener que volver a inicializar los atributos de nuevo
                                                    # invoco el método constructor de la Super clase
        # self.marca = marca
        # self.dispositivo_entrada = dispositivo_entrada

    def __str__(self):
        return f'Ratón -> ID: {self.id_raton}, marca: {self.marca}, tipo de entrada: {self.tipo_entrada}'
''' Se comenta el codigo para evitar que se ejecute en el main
# Prueba de clase
raton_1 = Raton('HP','USB')
raton_2 = Raton('Logitech','Inalambrico')

print(raton_1)
print(raton_2)
'''