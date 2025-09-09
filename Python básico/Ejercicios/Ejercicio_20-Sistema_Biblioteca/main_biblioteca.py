# Prueba del sistema de biblioteca

# Importar clases
from class_libro import Libro
from class_biblioteca import Biblioteca

# Crear objeto de biblioteca
bibliotecaNacional = Biblioteca('Biblioteca Nacional')

# Definición de libro
libro1 = Libro('It','Stephen King','Terror')
libro2 = Libro('Carrie','Stephen King','Terror')
libro3 = Libro('El sabueso','Lovecraft','Terror')
libro4 = Libro('Se lo que estas pensando','John Verdon','Misterio')

# Agregar libros a la biblioteca
bibliotecaNacional.agregarLibro(libro1)
bibliotecaNacional.agregarLibro(libro2)
bibliotecaNacional.agregarLibro(libro3)
bibliotecaNacional.agregarLibro(libro4)

# Buscar libro por autor
autor2 = 'Stephen King'
# Usar método
bibliotecaNacional.buscarAutor(autor2)

# Buscar libro por genero
genero1 = 'Terror'
# Usar metodo
bibliotecaNacional.buscarGenero(genero1)

# Buscar libro por título
titulo1 = 'It'
# Usar método
bibliotecaNacional.buscarLibro(titulo1)

# Mostrar todos los libros
bibliotecaNacional.mostrarTodosLibros()