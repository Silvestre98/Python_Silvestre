# Importación de clase empleado
from class_empleado import Empleado
from class_empresa import Empresa

print('*** Sistema de empleados')

# Crear instancia de la clase empresa
empresa1 = Empresa('Global Metoring')

# Contratar empleados
empresa1.contratar_empleado('Silvestre','TI')
empresa1.contratar_empleado('Jennyfer','Style list')
empresa1.contratar_empleado('Juan Jesus','TI')

# Obtener el total de empleados existen
print(f'Total de empleados: {Empleado.contador_empleados}')

# Obtener el totla de empleafos del departamento de TI
print(f'Total de empleados en el departamento de TI: {empresa1.obtener_numero_total_empleados_departamento('TI')}')