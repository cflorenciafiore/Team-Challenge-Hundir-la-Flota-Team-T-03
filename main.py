# Archivo principal del juego "Hundir la Flota"

# Importaciones necesarias
# Alejandro debe crear la clase "Tablero" (*nombre de ejemplo) en tablero.py
from tablero import Tablero

# Arrate debe crear las funciones auxiliares en funciones.py. Por ej.: "pedir_coordenadas_usuario", "coordenadas_aleatorias", etc. (*nombres de ejemplo)
from funciones import *

# Yo ya creé las constantes en variables.py
from variables import *

def main():
    # Parte 1: Es el mensaje de bienvenida
    print("¡Bienvenido a Hundir la Flota!")
    print("Instrucciones: introduce coordenadas X, Y entre 0 y 9 para disparar.\n")

    # Parte 2: Son 2 nuevas instancias de la clase "Tablero" que crean los tableros para ambos jugadores (el humano y la máquina)
    jugador = Tablero(1)
    maquina = Tablero(2)

    # Parte 3: "colocar_barcos()" (*nombre de ejemplo) es un método de la clase "Tablero" que coloca los barcos de cada jugador (estará en tablero.py)
    jugador.colocar_barcos()
    maquina.colocar_barcos()

    # Parte 4: Es una variable que controla de quién es el turno: True = turno del jugador, False = turno de la máquina
    turno_jugador = True

    # Parte 5: Es el bucle principal. El "while = True" hace que el juego continúe hasta que alguien gane (hasta que haya un "break")
    while True:
        if turno_jugador:
            # Parte 6: Muestra los tableros
            print("\nTu tablero:") 
            jugador.mostrar_tablero_propio() # "mostrar_tablero_propio()" (*nombre de ejemplo*) es otro método dentro de la clase "Tablero" (estará en tablero.py)

            print("\nTablero enemigo:")
            maquina.mostrar_tablero_enemigo()) # "mostrar_tablero_enemigo()" (*nombre de ejemplo*) es otro método dentro de la clase "Tablero" (estará en tablero.py)

            # Parte 7: "pedir_coordenadas_usuario()" (*nombre ejemplo) es un método que pide las coordenadas al usuario (estará en funciones.py)
            x, y = pedir_coordenadas_usuario()

            # Parte 8:
