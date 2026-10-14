class Libro:
    def __init__(self, isbn, titulo, autor,anio, genero= None,disponible=True ):
        self.isbn = isbn
        self.titulo = titulo
        self.autor =autor
        self.anio= anio
        self.genero = genero
        self.disponible =disponible

    def __str__(self) -> str:
            if self.disponible:
                estado = "Disponible"
            else:
                estado = "Prestado"
            return f"'{self.titulo}' de {self.autor} ({self.anio}) | Género: {self.genero} | ISBN: {self.isbn} | Estado: {estado}"

        # Creación de una instancia (objeto) de la clase Libro:
mi_libro = Libro(
isbn="978-84-376-0494-7",
titulo="Cien años de soledad",
autor="Gabriel García Márquez",
anio=1967,
genero="Realismo mágico",
disponible=True,
    )

    # Imprimir el libro en consola
print(mi_libro)

def __eq__ (self, otro):
     return self.isbn == otro.isbn