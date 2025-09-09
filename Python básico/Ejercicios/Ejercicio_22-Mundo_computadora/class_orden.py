# Crear clase de orden

class Ordenes:
    # Contador de ordenes
    contador_ordenes = 0
    # Método constructor de ordenes
    def __init__(self,computadoras):
        Ordenes.contador_ordenes += 1
        self.id_orden = Ordenes.contador_ordenes
        self.computadoras_lista = computadoras

    # Método para agregar computadoras a mi lista
    def agregar_computadoras(self,computadora):
        self.computadoras.append(computadora)

    # Método str
    def __str__(self):
        computadoras_str = ''
        for computadora_iterada in self.computadoras_lista:
            computadoras_str += '\n' + computadora_iterada.__str__()
        return f'''Orden {self.id_orden}
        Computadoras: {computadoras_str}'''