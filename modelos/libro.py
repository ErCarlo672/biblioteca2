class Libro:
    def __init__(self, isbn, titulo, autor, anio, genero=None, disponible=True):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.genero = genero
        self.disponible = disponible

    def __eq__(self, otro):
        return self.isbn == otro.isbn

    def __str__(self):
        if self.disponible:
            estado = "Disponible"
        else:
            estado = "Prestado"
        return f"'{self.titulo}' de {self.autor} ({self.anio}) | Genero: {self.genero} | ISBN: {self.isbn} | Estado: {estado}"
