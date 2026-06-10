from biblioteca import Biblioteca
from material import Libro, Revista
from socio import Socio
from excepciones import (MaterialNoDisponible, SocioNoEncontrado, MaterialNoEncontrado, PrestamoNoEncontrado)

#Punto de entrada

if __name__ == "__main__":
    biblioteca = Biblioteca("Biblioteca IFTS")
    print("Bienvenido al sistema de", biblioteca.nombre)

    finalizar = False
    while not finalizar:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            agregar_libro(biblioteca)
        elif opcion == "2":
            agregar_revista(biblioteca)
        elif opcion == "3":
            agregar_socio(biblioteca)
        elif opcion == "4":
            buscar_material(biblioteca)
        elif opcion == "5":
            listar_disponibles(biblioteca)
        elif opcion == "6":
            registrar_prestamo(biblioteca)
        elif opcion == "7":
            registrar_devolucion(biblioteca)
        elif opcion == "8":
            ver_prestamos_activos(biblioteca)
        elif opcion == "0":
            finalizar = True
            print("Hasta pronto!")
        else:
            print("Opcion no valida.")

def mostrar_menu():
    print("=============================================")
    print("   SISTEMA DE GESTIÓN DE BIBLIOTECA")
    print("=============================================")
    print("1. Agregar libro")
    print("2. Agregar revista")
    print("3. Agregar socio")
    print("4. Buscar material por titulo")
    print("5. Listar materiales disponibles")
    print("6. Registrar prestamo")
    print("7. Registrar devolucion")
    print("8. Ver prestamos activos")
    print("0. Salir")
    print("---------------------------------------------")

def agregar_libro(biblioteca):
    print("Nuevo Libro")
    titulo = input("Titulo: ")
    autor = input("Autor: ")
    año = input("Año de publicacion: ")
    isbn = input("ISBN: ")
    editorial = input("Editorial: ")
    libro = Libro(titulo, autor, año, isbn, editorial)
    biblioteca.agregar_material(libro)
    print("Libro agregado. ID asignado:", libro.id)

def agregar_revista(biblioteca):
    print("Nueva Revista")
    titulo = input("Titulo: ")
    autor = input("Autor: ")
    año = input("Año de publicacion: ")
    numero = input("Numero de edicion: ")
    categoria = input("Categoria: ")
    revista = Revista(titulo, autor, año, numero, categoria)
    biblioteca.agregar_material(revista)
    print("Revista agregada. ID asignado:", revista.id)

def agregar_socio(biblioteca):
    print("Nuevo Socio")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    dni = input("DNI: ")
    socio = Socio(nombre, apellido, dni)
    biblioteca.agregar_socio(socio)
    print("Socio registrado. ID asignado:", socio.id)


def buscar_material(biblioteca):
    texto = input("Ingrese parte del titulo a buscar: ")
    resultados = biblioteca.buscar_material_por_titulo(texto)
    if len(resultados) == 0:
        print("No se encontraron materiales.")
    else:
        print("Resultados:")
        i = 0
        while i < len(resultados):
            print(" ", resultados[i])
            i += 1


def listar_disponibles(biblioteca):
    disponibles = biblioteca.listar_materiales_disponibles()
    if len(disponibles) == 0:
        print("No hay materiales disponibles.")
    else:
        print("Materiales disponibles:")
        i = 0
        while i < len(disponibles):
            print(" ", disponibles[i])
            i += 1


def registrar_prestamo(biblioteca):
    if len(biblioteca.socios) == 0:
        print("No hay socios registrados.")
        return

    print("Socios registrados:")
    i = 0
    while i < len(biblioteca.socios):
        print(" ", biblioteca.socios[i])
        i += 1

    socio_id = int(input("ID del socio: "))

    disponibles = biblioteca.listar_materiales_disponibles()
    if len(disponibles) == 0:
        print("No hay materiales disponibles para prestar.")
        return

    print("Materiales disponibles:")
    i = 0
    while i < len(disponibles):
        print(" ", disponibles[i])
        i += 1

    material_id = int(input("ID del material: "))

    try:
        prestamo = biblioteca.registrar_prestamo(socio_id, material_id)
        print("Prestamo registrado con exito:")
        print(prestamo)
    except SocioNoEncontrado as e:
        print("Error:", e)
    except MaterialNoEncontrado as e:
        print("Error:", e)
    except MaterialNoDisponible as e:
        print("Error:", e)


def registrar_devolucion(biblioteca):
    activos = biblioteca.listar_prestamos_activos()
    if len(activos) == 0:
        print("No hay prestamos activos para devolver.")
        return

    print("Prestamos activos:")
    i = 0
    while i < len(activos):
        print(activos[i])
        i += 1

    prestamo_id = int(input("ID del prestamo a devolver: "))

    try:
        prestamo = biblioteca.registrar_devolucion(prestamo_id)
        print("Devolucion registrada.")
        print("Material disponible nuevamente:", prestamo.material.titulo)
    except PrestamoNoEncontrado as e:
        print("Error:", e)


def ver_prestamos_activos(biblioteca):
    activos = biblioteca.listar_prestamos_activos()
    if len(activos) == 0:
        print("No hay prestamos activos.")
    else:
        print("Prestamos activos:")
        i = 0
        while i < len(activos):
            print(activos[i])
            i += 1
