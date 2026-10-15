class Usuario:
    contador = 0

    def __init__(self, nombre, apellidos, email):
        Usuario.contador += 1
        self.id = Usuario.contador
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email

    def __str__(self):
        return f"Usuario(id={self.id}, nombre='{self.nombre} {self.apellidos}', email='{self.email}')"
