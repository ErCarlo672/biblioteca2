from modelos.libro import Libro
from modelos.prestamos import Prestamos
from modelos.usuario import Usuario
from servicios.biblioteca import Biblioteca

def menu ():
    print("=================================")
    print("      GESTIÓN DE BIBLIOTECA      ")
    print("=================================")
    print()
    print("1. Registrar libro")
    print("2. Registrar usuario")
    print("3. Buscar libro")
    print("4. Listar libros")
    print("5. Realizar préstamo")
    print("6. Registrar devolución")
    print("7. Mostrar préstamos activos")
    print("8. Mostrar préstamos de un usuario")
    print("9. Guardar datos")
    print("0. Salir")
    print()


def registrar_libro(biblioteca):
    isbn = input("Introduce el ISBN: ").strip()
    titulo = input("Introduce el título: ").strip()
    autor = input("Introduce el autor: ").strip()
    anio = input("Introduce el año: ").strip()

    libro = Libro(isbn,titulo,autor,anio)
    biblioteca.registrar_libro(libro)


def main():
    biblioteca = Biblioteca()

    while True:
        menu()
        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            print("\n--- REGISTRAR LIBRO ---")
            registrar_libro(biblioteca)
        elif opcion == "2":
            print("\n--- REGISTRAR USUARIO ---")

        elif opcion == "3":
            print("\n--- BUSCAR LIBRO ---")

        elif opcion == "4":
            print("\n--- LISTAR LIBROS ---")

        elif opcion == "5":
            print("\n--- REALIZAR PRÉSTAMO ---")

        elif opcion == "6":
            print("\n--- REGISTRAR DEVOLUCIÓN ---")

        elif opcion == "7":
            print("\n--- PRÉSTAMOS ACTIVOS ---")

        elif opcion == "8":
            print("\n--- PRÉSTAMOS DE UN USUARIO ---")

        elif opcion == "9":
            print("\n--- GUARDAR DATOS ---")

        elif opcion == "0":
            print("\nSaliendo del sistema... ¡Hasta pronto!")
            break

        else:
            print("\nOpción no válida. Por favor, introduce un número del 0 al 9.\n")

        
if __name__ == '__main__':
    main()