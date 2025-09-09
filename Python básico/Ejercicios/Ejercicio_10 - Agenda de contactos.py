"""
Crear agenda de contatos utilizando un diccionario de python con la siguiente estructura

agenda={
        nombre:{
            telefono
            email
            direccion
            }
    }
"""

agenda ={
    'Silvestre': {
        'telefono':'5544332211',
        'email':'silvestrelml@gmail.com',
        'direccion':'Santa Elena'
    },
    'Eduardo':{
        'telefono':'99887766',
        'email':'duarte@gmail.com',
        'direccion':'Tultepec'},
    'Isabel':{
        'telefono':'5566556655',
        'email':'isabel@gmail.com',
        'direccion':'Cuautitlan Izcalli'
    }
}
print(agenda)

# Acceder a la información de un contacto en especifico
'''Primero mandamo a llamar al diccionario que almacena todo (agenda), despues ingresamos el valor del usuario que deseamos llamar (eduardo) 
y por ultimo el campo que deseamos (email)'''

print(f'''Informacion de Eduardo\n
Telefon: {agenda['Eduardo']['telefono']}
Correo electronico: {agenda['Eduardo']['email']}
Direccion: {agenda['Eduardo']['direccion']}
''')

#  Agregar un nuevo usuario, en caso de que el elemento ya exista dentro del diccionario solamente se reemplazará la información.
agenda['Ana']={
    'telefono':'5544332211',
    'email':'ana@gmail.com',
    'direccion':'Cuautitlan'
}
print(agenda)
# Eliminar elemento del diccionario
agenda.popitem() # Eliminar el ultimo elemento creado
print(agenda)

# Eliminar un elemento en especifico
agenda.pop('Eduardo')
print(agenda)

# Mostrar contatos de la agenda
for nombre, detalle in agenda.items():
    print(f'''
Nombre: {nombre}
    Telefono: {detalle.get('telefono')}
    Correo electronico: {detalle.get('email')}
    Dirección: {detalle.get('direccion')}''')


# Convinació n de listas con diccionario

listaDiccionarios = [
    {
        'nombre':'Regina',
        'apellido':'Flores',
        'edad':'21'
    },
    {
        'nombre':'Angel',
        'apellido':'Reyes',
        'edad':'22'
    }
]

# Acceder al diccionario desde la lista
# primero la posicion del la lista y despues la llave del diccionario que se desea imprimir
print(f"""
Nombre:{listaDiccionarios[0].get('nombre')}
""")
# Imprimiendo toda la información del segundo elemento de la lista
print(f'''
Nombre:{listaDiccionarios[1].get('nombre')}
Apellido:{listaDiccionarios[1].get('apellido')}
Edad:{listaDiccionarios[1].get('edad')}
''')