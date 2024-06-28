import peliculas

def menu():
    while True:
        print("1. Agregar película")
        print("2. Listar películas")
        print("3. Buscar película")
        print("4. Salir")
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                peliculas.agregar_pelicula()
            elif opcion == 2:
                peliculas.listar_peliculas()
            elif opcion == 3:
                peliculas.buscar_pelicula()
            elif opcion == 4:
                peliculas.guardar_peliculas()
                print("¡Gracias por usar el programa!")
                break
            else:
                print("Opción no válida, intente de nuevo.")
        except ValueError:
            print("Error: Ingrese un número válido.")

if __name__ == "__main__":
    menu()