from unidecode import unidecode

# Ejercicio 1: Versión de Python 3.12.7

lista_libros = []
opciones_menu = ["B", "C", "P", "D", "E", "O", "S"]

libro1 = {"titulo": "La Celestina",
 "autor": "Fernando de Rojas",
 "ISBN": "9788420676159",
 "stock": 5,
 "unidades_prestadas": 0,
 "puntuacion_media": 0,
 "lista_opiniones": {
     "nickname": "Jorge",
     "puntuacion": 5,
     "comentario": "Bastante recomendable. Me emocionó"
 }
}

libro2 = {"titulo": "Don Quijote de la Mancha",
 "autor": "Miguel de Cervantes",
 "ISBN": "9788420672069",
 "stock": 3,
 "unidades_prestadas": 1,
 "puntuacion_media": 0,
 "lista_opiniones": {
     "usuario": "Pepito123",
     "puntuacion": 2,
     "comentario": "Regular"
 } 
}

libro3 = {"titulo": "Guía del Autoestopista Galáctico",
 "autor": "Douglas Adams",
 "ISBN": "9788433973108",
 "stock": 5,
 "unidades_prestadas": 2,
 "puntuacion_media": 0,
 "lista_opiniones": {
     "usuario": "Maria20_02",
     "puntuacion": 3,
     "comentario": "Más que decente"
 }
}

lista_libros.append(libro1)
lista_libros.append(libro2)
lista_libros.append(libro3)

def buscar_libro(cadena):
    for libro in lista_libros:
        if libro["ISBN"] == cadena:
            return libro
        elif unidecode(libro["titulo"]).lower() == unidecode(cadena).lower():
            return libro
    return None

def unidades_disponibles(libro):
    return libro["stock"] - libro["unidades_prestadas"]

def mostrar_libro(libro):
    mostrado = buscar_libro(libro)
    if mostrado != None:
        print(f"Título: {mostrado['titulo']}\n Autor: {mostrado['autor']}\n ISBN: {mostrado['ISBN']}\n Disponibles/Stock: {unidades_disponibles(mostrado)}/{mostrado['stock']}\n Puntuación media: {mostrado['puntuacion_media']}")

def crear_libro(titulo, autor, isbn):
    buscado = buscar_libro(isbn)
    if buscado != None:
        buscado["stock"] += 1
    else:
        nuevo_libro = {"titulo": titulo,
                       "autor": autor,
                       "ISBN": isbn,
                       "stock": 1,
                       "unidades_prestadas": 0,
                       "puntuación_media": 0,
                       "lista_opiniones": {}
                       }
        lista_libros.append(nuevo_libro)
        print(nuevo_libro)

def prestar_libro(isbn):
    prestado = buscar_libro(isbn)
    if prestado != None:
        if unidades_disponibles(prestado) == 0:
            return False
        else:
            prestado["unidades_prestadas"] += 1
            return True
    return False

def devolver_libro(isbn):
    devuelto = buscar_libro(isbn)
    if devuelto != None:
        if unidades_disponibles(devuelto) == devuelto["stock"]:
            return False
        else:
            devuelto["unidades_prestadas"] -= 1
            return True
    return False

def eliminar_libro(isbn):
    eliminado = buscar_libro(isbn)
    if eliminado != None:
        eliminado["stock"] -= 1
        if eliminado["stock"] == 0:
            lista_libros.remove(eliminado)
        return True
    else:
        return False

def mostrar_opiniones(isbn):
    buscado = buscar_libro(isbn)
    print(f"Lista de opiniones de {buscado["titulo"]}:\n Nickname: {buscado["lista_opiniones"]["usuario"] }\n Puntuación: {buscado["lista_opiniones"]["puntuacion"]}\n Comentario: {buscado["lista_opiniones"]["comentario"]}")

def menu():
    while(True):
        opcion = input(f"Indique la opción que desea realizar: \n [B]uscar\n [C]rear (pasando Título#Autor#ISBN13)\n [P]restar\n [D]evolver\n [E]liminar\n Mostrar [O]piniones\n [S]alir\n")
        if(opcion not in opciones_menu):
            print()
            continue
        match opcion:
            case "B":
                cadena = input("Introduce el ISBN o el título que quieres buscar: ")
                print(buscar_libro(cadena))
            case "C":
                titulo = input("Introduce el nombre del título: ")
                autor = input("Introduce el autor: ")
                isbn = input("Introduce el ISBN (13 dígitos y empieza por 978): ")
                crear_libro(titulo, autor, isbn)
            case "P":
                isbn = input("Introduce el ISBN del libro (13 dígitos y empieza por 978): ")
                if prestar_libro(isbn) == True:
                    print("Libro prestado con éxito")
                else:
                    print("El libro no se ha podido prestar")
            case "D":
                isbn = input("Introduce el ISBN del libro (13 dígitos y empieza por 978): ")
                if devolver_libro(isbn) == True:
                    print("Libro devuelto con éxito")
                else:
                    print("El libro no se ha podido devolver")
            case "E":
                isbn = input("Introduce el ISBN del libro (13 dígitos y empieza por 978): ")
                if eliminar_libro(isbn) == True:
                    print("Libro eliminado con éxito")
                else:
                    print("El libro no se ha podido eliminar")
            case "O":
                isbn = input("Introduce el ISBN del libro (13 dígitos y empieza por 978): ")
                mostrar_opiniones(isbn)
            case "S":
                break

menu()
