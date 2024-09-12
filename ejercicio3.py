"""Crea un diccionario llamado "biblioteca" donde las claves sean los títulos de los libros y los valores sean diccionarios con la siguiente información:
"autor": nombre del autor
"año": año de publicación
"disponible": True si está disponible, False si está prestado"""

biblioteca = {
    "El señor de los anillos": {
        "autor": "J.R.R. Tolkien",
        "año": 1954,
        "disponible": True
    },
    "Cien años de soledad": {
        "autor": "Gabriel García Márquez",
        "año": 1967,
        "disponible": False
    },
    
     "Deja de ser tu": {
        "autor": "Joe Dispenza",
        "año": 2018,
        "disponible": True
    },
     
      "Padre rico, Padre Pobre": {
        "autor": "Robert Kiyosaki",
        "año": 1998,
        "disponible": False
    },
}

"""Escribe una función llamada "agregar_libro" que permita añadir nuevos libros a la biblioteca. La función debe pedir al usuario el título, autor y año del libro."""
def agregar_libro(biblioteca):
   
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    año = int(input("Ingrese el año de publicación: "))

    nuevo_libro = {
        "autor": autor,
        "año": año,
        "disponible": True
    }

    biblioteca[titulo] = nuevo_libro
    print(f"El libro '{titulo}' ha sido agregado a la biblioteca.")

agregar_libro(biblioteca)

""""Escribe una función llamada "prestar_libro" que cambie el estado de un libro a no disponible. La función debe pedir al usuario el título del libro."""

def prestar_libro(biblioteca):
    
    titulo = input("Ingrese el título del libro que desea prestar: ")

    if titulo in biblioteca:
        biblioteca[titulo]["disponible"] = False
        print(f"El libro '{titulo}' ha sido marcado como prestado.")
    else:
        print(f"El libro '{titulo}' no se encuentra en la biblioteca.")

prestar_libro(biblioteca)

""""Escribe una función llamada "devolver_libro" que cambie el estado de un libro a disponible. La función debe pedir al usuario el título del libro."""

def devolver_libro(biblioteca):
   

    titulo = input("Ingrese el título del libro que desea devolver: ")

    if titulo in biblioteca:
        biblioteca[titulo]["disponible"] = True
        print(f"El libro '{titulo}' ha sido marcado como devuelto.")
    else:
        print(f"El libro '{titulo}' no se encuentra registrado en la biblioteca.")

devolver_libro(biblioteca)


"""Escribe una función llamada "mostrar_libros" que imprima todos los libros de la biblioteca, incluyendo su información y disponibilidad."""

def mostrar_libros(biblioteca):
  

    for titulo, info_libro in biblioteca.items():
        print(f"Título: {titulo}")
        print(f"Autor: {info_libro['autor']}")
        print(f"Año: {info_libro['año']}")
        print(f"Disponible: {'Sí' if info_libro['disponible'] else 'No'}")
        print("-" * 20)

mostrar_libros(biblioteca)

"""Crea un menú utilizando un bucle while que permita al usuario realizar las siguientes acciones:
Agregar un nuevo libro
Prestar un libro
Devolver un libro
Ver todos los libros
Salir del programa"""

def menu_biblioteca():
    biblioteca = {}

    while True:
        print("\nMenú de la Biblioteca")
        print("1. Agregar un nuevo libro")
        print("2. Prestar un libro")
        print("3. Devolver un libro")
        print("4. Ver todos los libros")
        print("5. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == '1':
            agregar_libro(biblioteca)
        elif opcion == '2':
            prestar_libro(biblioteca)
        elif opcion == '3':
            devolver_libro(biblioteca)
        elif opcion == '4':
            mostrar_libros(biblioteca)
        elif opcion == '5':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, ingrese un número del 1 al 5.")

menu_biblioteca()


"""Implementa el menú de modo que llame a las funciones correspondientes según la opción elegida por el usuario."""

def menu_biblioteca():
    biblioteca = {}

    while True:
        print("\nMenú de la Biblioteca")
        print("1. Agregar un nuevo libro")
        print("2. Prestar un libro")
        print("3. Devolver un libro")
        print("4. Ver todos los libros")
        print("5. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == '1':
            agregar_libro(biblioteca)
        elif opcion == '2':
            prestar_libro(biblioteca)
        elif opcion == '3':
            devolver_libro(biblioteca)
        elif opcion == '4':
            mostrar_libros(biblioteca)
        elif opcion == '5':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, ingrese un número del 1 al 5.")

menu_biblioteca()



"""Utiliza un bucle for para mostrar los libros publicados en un año específico que el usuario ingrese."""

def mostrar_libros_por_año(biblioteca, año):
 
  print(f"Libros publicados en {año}:")
  for titulo, info_libro in biblioteca.items():
    if info_libro['año'] == año:
      print(f"- {titulo}")

año_buscado = int(input("Ingrese el año: "))
mostrar_libros_por_año(biblioteca, año_buscado)