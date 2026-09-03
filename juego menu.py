print ("Bienvenidos a cronos")
def jugar():
    print("\n--- ¡Iniciando el Juego! ---")
    # Aquí puedes colocar la lógica de tu juego
    input()


def main():
    while True:
        print("\n====================")
        print("   MENÚ PRINCIPAL")
        print("====================")
        print("Jugar")
        print("Salir")

        opcion = input("\nElige una opción (jugar o salir): ")

        if opcion == "jugar":
            jugar()
        elif opcion == "salir":
            print("\n¡Gracias por jugar! Hasta pronto.")
            break
        else:
            print("\n⚠️ Opción no válida. Por favor, ingresa jugar o salir.")


# Ejecutar el programa
if __name__ == "__main__":
    main()