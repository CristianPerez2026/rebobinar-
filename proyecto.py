
print("================================")
print("       BIENVENIDOS A CRONOS")
print("================================")


# ============================================================
# CLASE PADRE / SUPERCLASE
# ============================================================

class Personaje:

    def __init__(self, nombre):
        self.nombre = nombre
        self.vida = 100
        self.ataque = 20
        self.inventario = []
        self.puntaje = 0

    def atacar(self, enemigo):
        dano = self.ataque
        enemigo["vida"] -= dano

        print("\n", self.nombre, "atacó al enemigo.")
        print("Daño realizado:", dano)

    def mostrar_info(self):
        print("\n==============================")
        print("      INFORMACIÓN")
        print("==============================")
        print("Nombre:", self.nombre)
        print("Vida:", self.vida)
        print("Ataque:", self.ataque)
        print("Puntaje:", self.puntaje)
        print("Inventario:", self.inventario)


# ============================================================
# CLASE HIJA / SUBCLASE
# ============================================================

class Heroe(Personaje):

    def atacar(self, enemigo):
        # POLIMORFISMO:
        # Se sobrescribe el método atacar() de la clase padre.
        dano = self.ataque + 10
        enemigo["vida"] -= dano

        print("\n⚔️", self.nombre, "atacó con su espada.")
        print("Daño realizado:", dano)


# ============================================================
# FUNCIÓN DE COMBATE
# ============================================================

def combate(personaje, enemigo):

    print("\n================================")
    print("            COMBATE")
    print("================================")

    print("Enemigo:", enemigo["nombre"])

    while personaje.vida > 0 and enemigo["vida"] > 0:

        print("\n------------------------------")
        print("Tu vida:", personaje.vida)
        print("Vida del enemigo:", enemigo["vida"])
        print("------------------------------")

        print("1. Atacar")
        print("2. Mostrar información")
        print("3. Usar poción")

        opcion = input("\nElige una opción: ")

        if opcion == "1":

            # POLIMORFISMO
            personaje.atacar(enemigo)

            if enemigo["vida"] > 0:

                personaje.vida -= enemigo["ataque"]

                print(
                    enemigo["nombre"],
                    "te atacó y causó",
                    enemigo["ataque"],
                    "de daño."
                )

        elif opcion == "2":

            personaje.mostrar_info()

        elif opcion == "3":

            if "Poción" in personaje.inventario:

                personaje.vida += 30

                if personaje.vida > 100:
                    personaje.vida = 100

                personaje.inventario.remove("Poción")

                print("\n❤️ Usaste una poción.")
                print("Tu vida ahora es:", personaje.vida)

            else:

                print("\n⚠️ No tienes pociones.")

        else:

            print("\n⚠️ Opción no válida.")

    if personaje.vida > 0:

        print("\n🎉 ¡Has derrotado a", enemigo["nombre"], "!")

        personaje.puntaje += 100

        personaje.inventario.append("Fragmento Cronos")

        print("🏆 +100 puntos")
        print("Has conseguido un Fragmento Cronos.")

        return True

    else:

        print("\n💀 Has sido derrotado.")
        return False


# ============================================================
# FUNCIÓN JUGAR
# ============================================================

def jugar():

    print("\n================================")
    print("       ¡INICIANDO CRONOS!")
    print("================================")

    nombre = input("\nEscribe el nombre de tu personaje: ")

    # Solo existe UN personaje jugable
    personaje = Heroe(nombre)

    personaje.inventario.append("Poción")

    print("\n¡Bienvenido,", personaje.nombre, "!")
    print("Tu misión es recuperar los Fragmentos Cronos.")

    input("\nPresiona ENTER para comenzar...")

    # Lista de épocas
    epocas = [
        "Edad de Piedra",
        "Egipto Antiguo",
        "Edad Media",
        "Futuro"
    ]

    # Lista de enemigos
    enemigos = [
        {
            "nombre": "Guerrero de Piedra",
            "vida": 50,
            "ataque": 10
        },
        {
            "nombre": "Guardián Egipcio",
            "vida": 60,
            "ataque": 12
        },
        {
            "nombre": "Caballero Oscuro",
            "vida": 70,
            "ataque": 14
        },
        {
            "nombre": "Robot del Futuro",
            "vida": 80,
            "ataque": 16
        }
    ]

    # Recorrer las épocas
    for i in range(len(epocas)):

        print("\n================================")
        print("          ÉPOCA")
        print("================================")

        print("Has viajado a:", epocas[i])

        enemigo = enemigos[i]

        resultado = combate(personaje, enemigo)

        if not resultado:

            print("\n================================")
            print("            GAME OVER")
            print("================================")

            print("Puntaje final:", personaje.puntaje)

            input("\nPresiona ENTER para volver al menú...")
            return

        if i < len(epocas) - 1:

            print("\nEl portal temporal se está abriendo...")

            input("Presiona ENTER para continuar...")

    # ========================================================
    # FINAL DEL JUEGO
    # ========================================================

    print("\n================================")
    print("       🕰️ ¡VICTORIA! 🕰️")
    print("================================")

    print("\n", personaje.nombre)
    print("has conseguido todos los Fragmentos Cronos.")

    print("\nFragmentos obtenidos:",
          personaje.inventario.count("Fragmento Cronos"))

    print("🏆 Puntaje final:", personaje.puntaje)

    print("\n¡Has salvado el tiempo!")

    input("\nPresiona ENTER para volver al menú...")


# ============================================================
# FUNCIÓN PRINCIPAL
# ============================================================

def main():

    while True:

        print("\n====================")
        print("   MENÚ PRINCIPAL")
        print("====================")

        print("Jugar")
        print("Salir")

        opcion = input(
            "\nElige una opción (jugar o salir): "
        ).lower()

        if opcion == "jugar":

            jugar()

        elif opcion == "salir":

            print("\n¡Gracias por jugar CRONOS!")
            print("¡Hasta pronto!")

            break

        else:

            print(
                "\n⚠️ Opción no válida."
                " Por favor, ingresa jugar o salir."
            )


# ============================================================
# EJECUTAR EL PROGRAMA
# ============================================================

if __name__ == "__main__":
    main()

