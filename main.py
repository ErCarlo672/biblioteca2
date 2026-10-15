from modelos.libro import Libro
from modelos.usuario import Usuario
from servicios.biblioteca import Biblioteca


def pedir_entero(msg):
    while True:
        try:
            return int(input(msg).strip())
        except ValueError:
            print("Tiene que ser un numero entero, vuelve a intentarlo")


def menu():
    print("=================================")
    print("      GESTION DE BIBLIOTECA      ")
    print("=================================")
    print()
    print("1. Registrar libro")
    print("2. Registrar usuario")
    print("3. Buscar libro")
    print("4. Listar libros")
    print("5. Realizar prestamo")
    print("6. Registrar devolucion")
    print("7. Mostrar prestamos activos")
    print("8. Mostrar prestamos de un usuario")
    print("9. Guardar datos")
    print("0. Salir")
    print()


def registrar_libro(biblioteca):
    isbn = input("Introduce el ISBN: ").strip()
    titulo = input("Introduce el titulo: ").strip()
    autor = input("Introduce el autor: ").strip()
    anio = input("Introduce el anio: ").strip()
    genero = input("Introduce el genero: ").strip()

    libro = Libro(isbn, titulo, autor, anio, genero)
    biblioteca.registrar_libro(libro)


def registrar_usuario(biblioteca):
    nombre = input("Introduce el nombre: ").strip().title()
    apellidos = input("Introduce los apellidos: ").strip().title()
    email = input("Introduce el email: ").strip()

    usuario = Usuario(nombre, apellidos, email)
    biblioteca.registrar_usuario(usuario)


def buscar_libro(biblioteca):
    print("1. Buscar por ISBN\n2. Buscar por titulo")
    opcion = input("Opcion: ").strip()

    if opcion == "1":
        isbn = input("Introduce el ISBN: ").strip()
        libro = biblioteca.buscar_libro(isbn)
        if libro is None:
            print("No existe ningun libro con ese ISBN")
        else:
            print(libro)
    elif opcion == "2":
        texto = input("Introduce el titulo o parte de el: ").strip()
        encontrados = biblioteca.buscar_por_titulo(texto)
        if len(encontrados) == 0:
            print("No se ha encontrado ningun libro")
        else:
            for l in encontrados:
                print(f"- {l}")
    else:
        print("Opcion no valida.")


def realizar_prestamo(biblioteca):
    isbn = input("Introduce el ISBN del libro: ").strip()
    id_usuario = pedir_entero("Introduce el id del usuario: ")
    biblioteca.realizar_prestamo(isbn, id_usuario)


def registrar_devolucion(biblioteca):
    isbn = input("Introduce el ISBN del libro devuelto: ").strip()
    biblioteca.registrar_devolucion(isbn)


def main():
    biblioteca = Biblioteca()

    while True:
        menu()
        opcion = input("Selecciona una opcion: ").strip()

        if opcion == "1":
            print("\n--- REGISTRAR LIBRO ---")
            registrar_libro(biblioteca)

        elif opcion == "2":
            print("\n--- REGISTRAR USUARIO ---")
            registrar_usuario(biblioteca)

        elif opcion == "3":
            print("\n--- BUSCAR LIBRO ---")
            buscar_libro(biblioteca)

        elif opcion == "4":
            print("\n--- LISTAR LIBROS ---")
            biblioteca.listar_libros()

        elif opcion == "5":
            print("\n--- REALIZAR PRESTAMO ---")
            realizar_prestamo(biblioteca)

        elif opcion == "6":
            print("\n--- REGISTRAR DEVOLUCION ---")
            registrar_devolucion(biblioteca)

        elif opcion == "7":
            print("\n--- PRESTAMOS ACTIVOS ---")

        elif opcion == "8":
            print("\n--- PRESTAMOS DE UN USUARIO ---")

        elif opcion == "9":
            print("\n--- GUARDAR DATOS ---")

        elif opcion == "0":
            print("\nSaliendo del sistema... Hasta pronto!")
            break

        else:
            print("\nOpcion no valida.Introduce un numero del 0 al 9.\n")


if __name__ == '__main__':
    main()
