'''
Crear una aplicación que me permita realizar el crud de una lista de suscriptores,
las operaciones que debe de contener son las siguientes.

- Crear set de suscriptores inicial
- Pedir o agregar un nuevo suscriptor
- Comprobar que el suscriptor no exista en el set y sino existe agregarlo a la lista
- Eliminar un suscriptor
- Verificar la cantidad de suscriptores en la aplicación
- Mostrar todos los suscriptores
'''

# Creación del set original
suscripciones = {'silvestre@mail.com','lalo@mail.com','mitzi@mail.com'}

# Pedir o agregar un nuevo suscriptor

# Agregar y comprobar que no este ya agregado ->> está parte se podría mejorar usando una función recursiva pero qué flojera hacerla jajajaja.

agregar_suscriptor = input('Deseas agregar un nuevo suscritor (Si/No)?:')
if agregar_suscriptor.lower().strip() == 'si':
    nuevo_suscritor = input('¿Correo del nuevo suscritor?: ')
    if nuevo_suscritor in suscripciones:
        print('El correo que intenta registrar ya existe en la base.')
    else:
        suscripciones.add(nuevo_suscritor)
        print('El suscriptor fue agregado correctamente.')
else:
    print('Entendido no desea agregar nuevo suscritor.')

# Eliminar suscritor
eliminar_suscriptor = input('¿Desea eliminar suscritor (Si/No)?: ')
if eliminar_suscriptor.lower().strip() == 'si':
    print(f'Correos de cuentas: {suscripciones}')
    eliminar_cuenta = input('Introduzca la cuenta a eliminar: ')
    suscripciones.remove(eliminar_cuenta)
    if eliminar_cuenta in suscripciones:
        print('No se elimino la cuenta.')
    else:
        print('Se elimino la cuenta correctamente.')
else:
    print('Se continua sin eliminar un suscritor.')

# Verificar la cantidad de suscripciones
print(f'La cantidad de suscripciones que existenson {len(suscripciones)}')

# Mostrar todas las cuentas de las suscripciones.
print('Suscripciones activas')
for i in suscripciones:
    print(i)

    
# Código extra
# Funcion recursiva sobre agregar suscriptor
'''
def agregar_suscriptores(suscripciones):
    agregar_suscriptor = input('¿Deseas agregar un nuevo suscriptor (Si/No)?: ').strip().lower()

    if agregar_suscriptor == 'si':
        nuevo_suscriptor = input('¿Correo del nuevo suscriptor?: ').strip()

        if nuevo_suscriptor in suscripciones:
            print('El correo que intenta registrar ya existe en la base.')
        else:
            suscripciones.add(nuevo_suscriptor)
            print('El suscriptor fue agregado correctamente.')

        # Llamada recursiva para seguir preguntando
        agregar_suscriptores(suscripciones)

    elif agregar_suscriptor == 'no':
        print('Entendido, no se agregarán más suscriptores.')
    else:
        print('Respuesta inválida, intenta de nuevo.')
        agregar_suscriptores(suscripciones
'''