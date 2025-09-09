# Importación de clase empleado
from class_empleado import Empleado


# Creación de la clase empresa
class Empresa:

    # Definición de constructor
    def __init__(self,nombre_empresa:str):
        self._nombre_empresa = nombre_empresa
        self._numero_empleado = [] # Se define como una lista vacía el atributo de número de empleados

    # Definir método de contratar empleado
    def contratar_empleado(self,nombre, departamento):
        empleado = Empleado(nombre,departamento) # Mandar a llamar el método de la clase empleado para crear el nuevo empleado
        self._numero_empleado.append(empleado) # Añadir el nuevo empleado a la lista

    # Definir método para saber el número total de empleados
    def obtener_numero_total_empleados_departamento(self, departamento):
        contador_empleados_departamento = 0
        for empleado in self._numero_empleado:
            if empleado._departamento_empleado == departamento:
                contador_empleados_departamento +=1
        return contador_empleados_departamento