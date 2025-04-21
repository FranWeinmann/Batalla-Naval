import random
import sys, subprocess

#  Limpia la consola dependiendo del sistema operativo. 
def clearScreen():
    operatingSystem = sys.platform
    if operatingSystem == "win32":
        subprocess.run("cls", shell=True)
    elif operatingSystem in ["linux", "darwin"]:
        subprocess.run("clear", shell=True)

# Función para mostrar el tablero
def mostrar_tablero(tablero, filas, columnas, mostrar_barcos=False):
    print("   ", end="")
    for col in range(columnas):
        print(f"{col:2} ", end="")  # Numeración de las columnas
    print()

    for i in range(filas):
        print(f"{i:2} ", end="")  # Numeración de las filas
        for j in range(columnas):
            if tablero[i][j] == "X":
                celda = "X"
            elif tablero[i][j] == "~":
                celda = "~"
            elif tablero[i][j] in ["B", "D", "T"]:  # Configuración que habilita barcos que ocupen 1, 2 o 3 espacios
                celda = "B" if mostrar_barcos else "."
            else:
                celda = "."
            print(f" {celda} ", end="")  # Se muestra el casillero
        print()
    print()

# Desición al finalizar el juego
def fin():
    print('1. Volver a jugar\n2. Menú\n3. Finalizar el juego')
    userOption = int(input('Elija una opción: '))
    if userOption == 1:
        un_jugador() 
    elif userOption == 2:
        main()
    elif userOption == 3:
        print("Gracias por jugar.")
        quit()
    else:
        print("Opción inválida.")
        fin()


def un_jugador():
    print('Decida las dimensiones del tablero de juego')
    # Ingresamos cantidad de filas y columnas
    filas = int(input("Ingrese la cantidad de filas: "))
    columnas = int(input("Ingrese la cantidad de columnas: "))

    # Creamos el tablero
    tablero = []
    for _ in range(filas):
        fila = [0] * columnas
        tablero.append(fila)
    # Definimos la cantidad de barcos y de chances
    cantidad_barcos = max(1, (filas * columnas) // 10)
    maxChances = (filas * columnas) // 2
    print(f"Tienes {maxChances} oportunidades para encontrar {cantidad_barcos} barcos.")

    # Generamos barcos que ocupan 1 espacio cada uno
    barcos_generados = 0
    while barcos_generados < cantidad_barcos:
        fila_random = random.randint(0, filas - 1)
        columna_random = random.randint(0, columnas - 1)
        if tablero[fila_random][columna_random] == 0:
            tablero[fila_random][columna_random] = "B"
            barcos_generados += 1

    # Empieza el juego
    chances = 0
    barcos_encontrados = 0
    while chances < maxChances and barcos_encontrados < cantidad_barcos:
        print(f"\nIntento {chances + 1} de {maxChances}")
        mostrar_tablero(tablero, filas, columnas)

        while True:
            try:
                userRow = int(input("Ingrese la fila a la cual quiere atacar: "))
                userColumn = int(input("Ingrese la columna a la cual quiere atacar: "))
                if 0 <= userRow < filas and 0 <= userColumn < columnas:
                    break
                else:
                    print("Esa posición está fuera del tablero. Intenta nuevamente.")
            except ValueError:
                print("Por favor, ingresa solo números válidos.")

        if tablero[userRow][userColumn] == "B":
            print("Has acertado en un barco.")
            tablero[userRow][userColumn] = "X"
            barcos_encontrados += 1
        elif tablero[userRow][userColumn] == "X":
            print("Ya habías atacado ahí y había un barco.")
        elif tablero[userRow][userColumn] == "~":
            print("Ya habías atacado ahí y era agua.")
        else:
            print("No había barco en esa posición.")
            tablero[userRow][userColumn] = "~"

        chances += 1

    # Mostramos el tablero final con barcos restantes si no ganó
    print("\nTablero final:")
    mostrar_tablero(tablero, filas, columnas, mostrar_barcos=(barcos_encontrados < cantidad_barcos))

    if barcos_encontrados == cantidad_barcos:
        print("¡Felicidades! Encontraste todos los barcos.")
    else:
        print("Fin del juego. No encontraste todos los barcos.")
        print(f"Encontraste {barcos_encontrados} de {cantidad_barcos} barcos.")
    
    fin()

# Menú principal
def main():
    clearScreen()
    print("██████╗  █████╗ ████████╗ █████╗ ██╗     ██╗      █████╗   ███╗  ██╗ █████╗ ██╗   ██╗ █████╗ ██╗     ")
    print("██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██║     ██║     ██╔══██╗  ████╗ ██║██╔══██╗██║   ██║██╔══██╗██║     ")
    print("██████╦╝███████║   ██║   ███████║██║     ██║     ███████║  ██╔██╗██║███████║╚██╗ ██╔╝███████║██║     ")
    print("██╔══██╗██╔══██║   ██║   ██╔══██║██║     ██║     ██╔══██║  ██║╚████║██╔══██║ ╚████╔╝ ██╔══██║██║     ")
    print("██████╦╝██║  ██║   ██║   ██║  ██║███████╗███████╗██║  ██║  ██║ ╚███║██║  ██║  ╚██╔╝  ██║  ██║███████╗")
    print("╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝  ╚═╝  ╚══╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝")
    print("")
    print("1. Un Jugador    2. Dos Jugadores    3. Salir")
    answer = int(input("Opción elegida: "))

    if answer == 1:
        un_jugador()
    elif answer == 2:
        dos_jugadores()
    elif answer == 3:
        print("Has salido del juego.")
        quit()
    else:
        print("Opción inválida. Por favor, elige entre 1 y 4.")
        main()

def dos_jugadores():
    clearScreen()
    print('Decida las dimensiones del tablero de juego')

    filas = int(input("Ingrese la cantidad de filas: "))
    columnas = int(input("Ingrese la cantidad de columnas: "))
    maxBarcos = int(input('Elija la máxima cantidad de barcos que podrá elegir cada jugador: '))

    # Crear tableros para los dos jugadores
    tablero_jugador1 = [[0 for _ in range(columnas)] for _ in range(filas)]
    tablero_jugador2 = [[0 for _ in range(columnas)] for _ in range(filas)]

    tablero_disparos_j1 = [[0 for _ in range(columnas)] for _ in range(filas)]
    tablero_disparos_j2 = [[0 for _ in range(columnas)] for _ in range(filas)]

    def colocar_barcos(tablero, jugador, maxBarcos):
        cantidad_barcos = 0
        barcos = []

        while cantidad_barcos < maxBarcos:
            clearScreen()
            print(f"Turno del Jugador {jugador} - Colocación de barcos ({cantidad_barcos + 1}/{maxBarcos})")
            mostrar_tablero(tablero, filas, columnas, mostrar_barcos=True)
            try:
                espacio_ocupado = int(input("Ingrese la cantidad de espacios que ocupará el barco (1, 2 o 3 espacios): "))
                if espacio_ocupado not in [1, 2, 3]:
                    print("Solo se pueden colocar barcos de 1, 2 o 3 espacios.")
                    input("Presiona Enter para continuar...")
                    continue

                fila = int(input("Ingrese la fila donde desea colocar el barco: "))
                columna = int(input("Ingrese la columna donde desea colocar el barco: "))

                if not (0 <= fila < filas and 0 <= columna < columnas):
                    print("Posición fuera del tablero.")
                    input("Presiona Enter para continuar...")
                    continue

                simbolo = {1: "B", 2: "D", 3: "T"}[espacio_ocupado]

                if espacio_ocupado == 1:
                    if tablero[fila][columna] == 0:
                        tablero[fila][columna] = simbolo
                        barcos.append([(fila, columna)])
                        cantidad_barcos += 1
                    else:
                        print("Espacio ocupado. Intente en otra posición.")
                else:
                    direccion = input("Ingrese la dirección (L=Izq, R=Der, U=Arriba, D=Abajo): ").upper()
                    if direccion not in ["L", "R", "U", "D"]:
                        print("Dirección inválida.")
                        input("Presiona Enter para continuar...")
                        continue

                    coordenadas = []
                    for i in range(espacio_ocupado):
                        if direccion == "L":
                            nueva_fila, nueva_col = fila, columna - i
                        elif direccion == "R":
                            nueva_fila, nueva_col = fila, columna + i
                        elif direccion == "U":
                            nueva_fila, nueva_col = fila - i, columna
                        elif direccion == "D":
                            nueva_fila, nueva_col = fila + i, columna

                        if not (0 <= nueva_fila < filas and 0 <= nueva_col < columnas):
                            print("El barco no cabe en esa dirección.")
                            break
                        if tablero[nueva_fila][nueva_col] != 0:
                            print("Espacio ocupado. Intente en otra posición.")
                            break
                        coordenadas.append((nueva_fila, nueva_col))
                    else:
                        for f, c in coordenadas:
                            tablero[f][c] = simbolo
                        barcos.append(coordenadas)
                        cantidad_barcos += 1

            except ValueError:
                print("Entrada inválida. Por favor ingrese números válidos.")

            input("Presiona Enter para continuar...")

        return barcos

    # Función para verificar si el barco se destruyó
    def barco_destruido(barco, tablero):
        return all(tablero[f][c] == "X" for f, c in barco)

    barcos_j1 = colocar_barcos(tablero_jugador1, 1, maxBarcos)
    clearScreen()
    barcos_j2 = colocar_barcos(tablero_jugador2, 2, maxBarcos)
    clearScreen()

    barcos_restantes_j1 = maxBarcos
    barcos_restantes_j2 = maxBarcos

    jugador_actual = 1
    while barcos_restantes_j1 > 0 and barcos_restantes_j2 > 0:
        clearScreen()
        print(f"Turno del Jugador {jugador_actual}")

        if jugador_actual == 1:
            tablero_propio = tablero_jugador1
            tablero_oponente = tablero_jugador2
            tablero_disparos = tablero_disparos_j1
            barcos_oponente = barcos_j2
        else:
            tablero_propio = tablero_jugador2
            tablero_oponente = tablero_jugador1
            tablero_disparos = tablero_disparos_j2
            barcos_oponente = barcos_j1

        print("Tu tablero:")
        mostrar_tablero(tablero_propio, filas, columnas, mostrar_barcos=True)
        print("Tablero de disparos:")
        mostrar_tablero(tablero_disparos, filas, columnas)

        while True:
            try:
                fila = int(input("Ingrese la fila que desea atacar: "))
                columna = int(input("Ingrese la columna que desea atacar: "))
                if 0 <= fila < filas and 0 <= columna < columnas:
                    if tablero_disparos[fila][columna] in ["X", "~"]:
                        print("Ya disparaste a esa posición. Elige otra.")
                    else:
                        break
                else:
                    print("Posición inválida.")
            except ValueError:
                print("Entrada inválida. Solo números.")

        if tablero_oponente[fila][columna] in ["B", "D", "T"]:
            print("¡Impacto!")
            tablero_oponente[fila][columna] = "X"
            tablero_disparos[fila][columna] = "X"

            impactado = (fila, columna)
            for barco in barcos_oponente:
                if impactado in barco and barco_destruido(barco, tablero_oponente):
                    print("¡Barco destruido!")
                    barcos_oponente.remove(barco)
                    if jugador_actual == 1:
                        barcos_restantes_j2 -= 1
                    else:
                        barcos_restantes_j1 -= 1
                    break
        else:
            print("Agua.")
            tablero_disparos[fila][columna] = "~"
            if tablero_oponente[fila][columna] == 0:
                tablero_oponente[fila][columna] = "~"

        input("Presiona Enter para continuar...")
        jugador_actual = 2 if jugador_actual == 1 else 1

    clearScreen()
    if barcos_restantes_j1 == 0:
        print("¡Jugador 2 ha ganado!")
    else:
        print("¡Jugador 1 ha ganado!")

    fin()
    

# Inicia el juego
main()