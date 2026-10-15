from datetime import date


class Prestamos:
    def __init__(self, usuario, libro, fecha_prestamo=None, fecha_devolucion=None):
        self.usuario = usuario
        self.libro = libro
        self.fecha_prestamo = (fecha_prestamo if fecha_prestamo is not None else date.today())
        self.fecha_devolucion = fecha_devolucion

    @property
    def activo(self):
        return self.fecha_devolucion is None

    def devolver(self):
        self.fecha_devolucion = date.today()
        self.libro.disponible = True

    def __str__(self):
        estado_devolucion = (
            self.fecha_devolucion if self.fecha_devolucion else "Pendiente"
        )
        return (
            f"'{self.libro.titulo}' prestado a {self.usuario.nombre} {self.usuario.apellidos} "
            f"| Inicio: {self.fecha_prestamo} | Devolucion: {estado_devolucion}"
        )
