print("**** Dibujar Triangulo ****")

numeroFilas = int(input("Proporciona el número de filas: "))

 # Iterar sobre cada fila del triángulo
for fila in range(1,numeroFilas + 1):
    """
    Lógica de calculo de los espacios
        Multiplicar mi cadena "espacio en blanco" por el número de filas menos la fila en la que me encuentro:
          Ejemplo si me encuentro en la fila 1 me debería de dar suponiendo que quiero 3 filas solamente,
          numero de filas -> 3 - fila en la que me encuentro -> 1 = 2 ->> debería de imprimir 2 espacios en blanco
          3 - 2 = 1 ->> en el caso de las fila 2, debería imprimir un espacio
           Demostración:
              *    ---> Fila 1
             ***   ---> Fila 2
           *****  ---> Fila 3
    """
    espaciosBlancos = " " * (numeroFilas - fila)
    """
    Lógica de calculo de los asteriscos
        Sería de igual manera multiplicar mi cadena "asterisco" pero se multiplicará por la siguiente formula (2 * fila - 1)
        donde:
         2 es la cantidad de veces que se deberá multiplicar mi '*'
         fila es la fila en la que se encuentra la iteración del programa
         -1 le quitará un asterisco a producto final de la formula para asi poder tener la cantidad correcta de arsteriscos en la impresión.
    """
    asteriscos = '*' * (2 * fila - 1)
    """
    Imprimir todo el programa 
    """
    print(f'{espaciosBlancos}{asteriscos}')