# Importar clase libro
from class_libro import Libro

# Creación de la clase de biblioteca
class Biblioteca:
    # Método constructor
    def __init__(self,nombreBiblioteca:str):
        # Creación de los atributos
        self._nombreBiblioteca = nombreBiblioteca
        self._listaLibros = [] # Lista vacía que almacenará los libros

    # Definición de los métodos
    # Agregar libro
    def agregarLibro(self,libro): # El objeto de libro se debe de crear en la seccion del main
        self._listaLibros.append(libro) # Agrego mi objeto mi lista de libros

    # Buscar libro por autor
    def buscarAutor(self,autor:str):
        for iteradorLibro in self._listaLibros: # Iterar lista de objetos
            if iteradorLibro._autorLibro.lower() == autor.lower(): # Revisar el match con el autor introducido si es correcto accede al 'if'
                print(f'''\nInformación del libro por autor
Titulo: {iteradorLibro._tituloLibro}
Autor: {iteradorLibro._autorLibro}
Género: {iteradorLibro._generoLibro}''') # Imprimir resultado
            else:
                return print('Autor no encontrado')

    # Buscar libro por género
    def buscarGenero(self,genero:str):
        for iteradorLibro in self._listaLibros:  # Iterar lista de objetos
            if iteradorLibro._generoLibro.lower() == genero.lower():  # Revisar el match con el genero introducido si es correcto accede al 'if'
                print(f'''\nInformación del libro por género
        Titulo: {iteradorLibro._tituloLibro}
        Autor: {iteradorLibro._autorLibro}
        Género: {iteradorLibro._generoLibro}''')  # Imprimir resultado
            else:
                return print('Autor no encontrado')

    # Buscar libro por titulo
    def buscarLibro(self,titulo:str):
        for iteradorLibro in self._listaLibros:  # Iterar lista de objetos
            if iteradorLibro._tituloLibro.lower() == titulo.lower():  # Revisar el match con el titulo introducido si es correcto accede al 'if'
                print(f'''Información del libro por título
        Titulo: {iteradorLibro._tituloLibro}
        Autor: {iteradorLibro._autorLibro}
        Género: {iteradorLibro._generoLibro}''')  # Imprimir resultado
            else:
                return print('Autor no encontrado')

    # Mostrar todos los libros
    def mostrarTodosLibros(self):
        print('\nMostrar todos los libros')
        for iteradorLibros in self._listaLibros:
            print(f'Información -> Título: {iteradorLibros._tituloLibro}, Autor: {iteradorLibros._autorLibro}, Género: {iteradorLibros._generoLibro}')

    # Eliminar libro
    def eliminarLibro(self,titulo,autor):
        for iteradorLibro in self._listaLibros:
            if (iteradorLibro._tituloLibro == titulo) and (iteradorLibro._autorLibro == autor):
                self._listaLibros.remove(iteradorLibro)
                print('Eliminación del libro completada')
            else:
                print('Error al eliminar el libro')

# Nota en los métodos que usamos para saber la información de un libro podemos crear un método especifico para mostrar esa información
# de esta manera se evitan tener código repetido.

    def mostrarInformacionLibro(self,libro):
        print(f'Información'
              f'Titulo: {libro._tituloLibro}'
              f'Autor: {libro._autorLibro}'
              f'Género: {libro._generoLibro}')