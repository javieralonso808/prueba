import random
import json

peliculas = {}

def generar_codigo():
    return random.randint(1, 1000)

def agregar_pelicula():
    cod = generar_codigo()
    nombre = input("Ingrese el nombre de la película: ")
    anio = int(input("Ingrese el año de la película: "))
    categoria = input("Ingrese la categoría de la película: ")
    director = input("Ingrese el director de la película: ")
    actores = []

    while True:
        agregar = input("¿Desea agregar un actor? (s/n): ")
        if agregar.lower() == 's':
            rut = input("Ingrese el RUT del actor: ")
            nombre_actor = input("Ingrese el nombre del actor: ")
            edad = int(input("Ingrese la edad del actor: "))
            actor = {
                "Rut": rut,
                "Nombre": nombre_actor,
                "Edad": edad
            }
            actores.append(actor)
        else:
            break

    pelicula = {
        "cod": cod,
        "nombre": nombre,
        "anio": anio,
        "categoria": categoria,
        "director": director,
        "actores": actores
    }

    peliculas[cod] = pelicula
    print("Película agregada exitosamente!")

def listar_peliculas():
    if not peliculas:
        print("No hay películas registradas.")
        return
    
    for cod, pelicula in peliculas.items():
        print(f"Código: {cod}")
        print(f"Nombre: {pelicula['nombre']}")
        print(f"Año: {pelicula['anio']}")
        print(f"Categoría: {pelicula['categoria']}")
        print(f"Director: {pelicula['director']}")
        print(f"Actores: {', '.join([actor['Nombre'] for actor in pelicula['actores']])}")
        print()

def buscar_pelicula():
    categoria = input("Ingrese la categoría de la película a buscar: ")
    encontradas = [pelicula for pelicula in peliculas.values() if pelicula['categoria'] == categoria]

    if not encontradas:
        print("No se encontraron películas en esa categoría.")
    else:
        for pelicula in encontradas:
            print(f"Código: {pelicula['cod']}")
            print(f"Nombre: {pelicula['nombre']}")
            print(f"Año: {pelicula['anio']}")
            print(f"Categoría: {pelicula['categoria']}")
            print(f"Director: {pelicula['director']}")
            print(f"Actores: {', '.join([actor['Nombre'] for actor in pelicula['actores']])}")
            print()

def guardar_peliculas():
    with open('peliculas.txt', 'w') as file:
        for pelicula in peliculas.values():
            file.write(f"Código: {pelicula['cod']}\n")
            file.write(f"Nombre: {pelicula['nombre']}\n")
            file.write(f"Año: {pelicula['anio']}\n")
            file.write(f"Categoría: {pelicula['categoria']}\n")
            file.write(f"Director: {pelicula['director']}\n")
            file.write(f"Actores:\n")
            for actor in pelicula['actores']:
                file.write(f"\tNombre: {actor['Nombre']}, RUT: {actor['Rut']}, Edad: {actor['Edad']}\n")
            file.write("\n")
    print("Películas guardadas en peliculas.txt")
