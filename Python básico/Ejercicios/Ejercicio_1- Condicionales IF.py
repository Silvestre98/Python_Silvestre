# Casa de los espejos

"""
Supongamos que estás en un parque de diversiones y que quieres entrar a la casa de los espejos.

Sin embargo debes de cumplir con ciertas condiciones:
1.- Debes de tener más de 10 años
2.- No debes tener miedo a la oscuridad

Si cumples estas condiciones puedes entrar a la casa de los espejos

"""
# Pregunta inicial
respuesta = input('Hola deseas entrar a la casa de los espejos? (Si/No): ')


# Verificacion de respuesta
if respuesta.lower().strip() == 'si':
    print('Perfecto te haremos unas preguntas antes de ingresar de acuerdo.''\n'
          'Contianuremos con el cuestionario...')

    # Cuestionario
    pregu_1 = input('Tienes mas de 10 años? (Si/No): ')
    pregu_2 = input('Te da miedo la oscuridad? (Si/No): ')

    if pregu_1.lower().strip() == 'si' and pregu_2.lower().strip() == 'no':
        print('Perfecto puedes entrar.')
    else:
        print('Lo siento me temo que no puedes pasar, vuelve despues.')

elif respuesta.lower().strip() == 'no':
    print('Entendido hasta luego, que tengas una buena noche.')
else:
    print('Repuesta equivocada')
