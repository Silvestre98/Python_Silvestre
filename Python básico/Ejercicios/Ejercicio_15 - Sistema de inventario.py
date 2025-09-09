print('+++ Sistema de inventarios +++')

# Inventario del almacen
lista_inventario = [
    {'id': 1, 'nombre': 'Camisa', 'precio': 25.99, 'cantidad': 50},
    {'id': 2, 'nombre': 'Pantalón', 'precio': 29.99, 'cantidad': 32},
    {'id': 3, 'nombre': 'Chamarra', 'precio': 40.99, 'cantidad': 19}
]

# Funcion mostrar Inventario
def mostrarInventario():
    print('--- Inventario del almacen ---')
    for producto in lista_inventario:
        print(f"Id:{producto.get('id')}, Nombre:{producto.get('nombre')}, "
              f"Precio:{producto.get('precio')}, Cantidad:{producto.get('cantidad')}")


# Agregar producto
def agregarProducto():
    print('Agregar nuevo producto')
    n_id = int(input('Id: '))
    n_nombre = input('Nombre: ')
    n_precio = float(input('Precio: '))
    n_cantidad = int(input('Cantidad: '))
    nuevo_producto = {'id': n_id, 'nombre': n_nombre,
                      'precio': n_precio, 'cantidad': n_cantidad}
    lista_inventario.append(nuevo_producto)
    print('Producto agregado correctamente')


# Buscar producto por id
def buscarProductoPorID():
    print('Buscar producto por id')
    id_buscar = int(input('Ingresa el id a buscar: '))
    for producto in lista_inventario:
        if producto.get('id') == id_buscar:
            print('\nInformación del producto encontrado:')
            print(f"""
    Id: {producto.get('id')}
    Nombre: {producto.get('nombre')}
    Precio: {producto.get('precio')}
    Cantidad: {producto.get('cantidad')}""")
            return
    print("Producto no encontrado.")


# Programa principal
if __name__ == '__main__':
    while True:
        print('''\n --- Menú ---
    1.- Mostrar inventario
    2.- Agregar producto
    3.- Buscar producto por id
    4.- Salir
        ''')
        opcion = int(input('Ingresa la opción que deseas seleccionar: '))

        if opcion == 1:
            mostrarInventario()
        elif opcion == 2:
            agregarProducto()
        elif opcion == 3:
            buscarProductoPorID()
        elif opcion == 4:
            print('Hasta luego')
            break
        else:
            print('Opción no válida, vuelve a intentarlo.')
