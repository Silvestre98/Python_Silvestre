# Creación de clase empleados

class Empleado:

    # Atributo de clase ->> Contador de empleados
    contador_empleados = 0

    def __init__(self,nombre_empleado:str,departamento_empleado:str):
        # Contador del numero de empleados
        Empleado.contador_empleados += 1
        # Atributos de la clase empleados
        self._nombre_empleado = nombre_empleado
        self._departamento_empleado = departamento_empleado

    # Método de clase para imprimir el número total de empleados
    @classmethod
    def obtenerTotalEmpleados (cls):
        return print(f'Número total de empleados: {cls.contador_empleados}')