from modelos.libro import Libro
class Biblioteca :
    def __init__(self) -> None:
        self.libros =[]
        self.usuarios =[]
        self.prestamos =[]        

    def registrar_libro(self, libro):
        if self.buscar_libros(libro) is None:
            print('El libro ya esta en la lista')
        self.libros.append(libro)

    def buscar_libros (self, libro):
        for l in self.libros:
         #   if l.isbn == libro.isbn:
          #      return l
           # return None
            if libro.__eq__(libro):
                return libro
            return None