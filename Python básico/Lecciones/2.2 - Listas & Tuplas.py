# Combinación de listas y tuplas.

# Declarar colección de tuplas.
producto1 = 'D-21','Camisa', 100.00
producto2 = ('F-21','Falda',150.00)
producto3 = 'H-22', 'Chamarra', 200.00

# Definir lista donde se almacenarán las tuplas de los productos.
listaProductos_1 = [producto1,producto3,producto2] # ->> Creación de la lista con la tupla.

listaProductos_2 =[ # Esta es la segunda forma en la que se puede almacenar una colección de tuplas en una lista.
    ('D-23','Zapatos caballero',700),
    ('C-12','Calcetas',150),
    ('H-43','Corbata',120)]

# Unpacking de las tuplas por medio de un For
totalPrecio = 0

for i in listaProductos_2:
    #Unpaking de los productos.
    codigo, descripcion_producto, precio = i # Variables que la contendrán
    totalPrecio += precio

    #Imprimir cada una de las tuplas
    print(f''' 
        Unpacking de la tupla: {i}
        Codigo: {codigo}
        Descricion: {descripcion_producto}
        Precio: {precio}
    ''')
print(f'Precio total: {totalPrecio}')