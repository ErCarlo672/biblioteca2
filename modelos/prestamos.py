
from datetime import date

class Prestamos:
    def __init__(self, Usuario, Libro, fecha_prestamo=None,fecha_devolucion=None ):
        self.Usuario = Usuario
        self.Libro = Libro
        self.fecha_prestamo = (fecha_prestamo if fecha_prestamo is not None else date.today())
        self.fecha_devolucion = fecha_devolucion

    @property
    def activo(self):
        return self.fecha_devolucion is None

    def __str__(self):
        estado_devolucion = (
            self.fecha_devolucion if self.fecha_devolucion else "Pendiente"
        )
        return (
            f"Préstamo: '{self.Libro}' prestado a {self.Usuario} "
            f"Inicio: {self.fecha_prestamo} | Devolución: {estado_devolucion}"
        )

    