from modelos.prestamos import Prestamos


class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []
        self.prestamos = []

    def registrar_libro(self, libro):
        if self.buscar_libro(libro.isbn) is not None:
            print("El libro ya esta en la lista")
            return False
        self.libros.append(libro)
        print(f"El libro '{libro.titulo}' ha sido registrado.")
        return True

    def buscar_libro(self, isbn):
        for l in self.libros:
            if l.isbn == isbn:
                return l
        return None

    def buscar_por_titulo(self, texto):
        encontrados = []
        for l in self.libros:
            if texto.lower() in l.titulo.lower():
                encontrados.append(l)
        return encontrados

    def listar_libros(self):
        if len(self.libros) == 0:
            print("No hay libros registrados.")
            return
        print("LISTADO DE LIBROS:")
        for l in self.libros:
            print(f"- {l}")

    def registrar_usuario(self, usuario):
        for u in self.usuarios:
            if u.email == usuario.email:
                print("Ya existe un usuario con ese email")
                return False
        self.usuarios.append(usuario)
        print(f"{usuario.nombre} ha sido registrado con el id {usuario.id}.")
        return True

    def buscar_usuario(self, id_usuario):
        for u in self.usuarios:
            if u.id == id_usuario:
                return u
        return None

    def realizar_prestamo(self, isbn, id_usuario):
        libro = self.buscar_libro(isbn)
        if libro is None:
            print("No existe ningun libro con ese ISBN")
            return False

        usuario = self.buscar_usuario(id_usuario)
        if usuario is None:
            print("No existe ningun usuario con ese id")
            return False

        if not libro.disponible:
            print(f"El libro '{libro.titulo}' ya esta prestado")
            return False

        prestamo = Prestamos(usuario, libro)
        libro.disponible = False
        self.prestamos.append(prestamo)
        print(f"Prestamo realizado: {prestamo}")
        return True

    def registrar_devolucion(self, isbn):
        for p in self.prestamos:
            if p.libro.isbn == isbn and p.activo:
                p.devolver()
                print(f"Devolucion registrada: {p}")
                return True
        print("No hay ningun prestamo activo de ese libro")
        return False
