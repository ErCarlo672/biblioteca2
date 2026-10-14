class Usuario:
    def __init__(self, id, nombre, apellidos,email ):
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email

    def __str__(self):
        return f"Usuario(id={self.id}, nombre='{self.nombre} {self.apellidos}', email='{self.email}')"

mi_usuario = Usuario(
    id=1,
    nombre="Carlos",
    apellidos="García Pérez",
    email="carlos.garcia@email.com",
)

# Imprimir el usuario en consola
print(mi_usuario)