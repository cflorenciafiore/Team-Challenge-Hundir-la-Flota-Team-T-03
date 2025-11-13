<<<<<<< Updated upstream
from variables import *
from tablero import Tablero 
from funciones import *

def main ():

    respuesta = input("Hola! Bienvenido al juego Hundir la Flota. Sabes cómo funciona este juego? (si/no)").lower()
    if respuesta == "no":
        print ('''Instrucciones del juego: El objetivo del juego es hundir todos los barcos del enemigo antes de que él lo haga.
        El juego empieza teniendo cada uno de vosotros un tablero con unos barcos en posiciones que la otra persona no conoce.
        Tienes que decir a qué coordenada quieres impactar, como por ejemplo: Coordenada (1,2) o coordenada (3,5).
        Si aciertas, la otra persona dirá Tocado o Hundido. Sino, dirá Agua.
        Los turnos se alternan hasta que uno de los jugadores ya no tenga barcos.
        Gana la persona que hunda la flota primero. A por todas!''')
    elif respuesta == "si":
        print ("Pulsa Enter para empezar la partida")
    else:
        print ("Perdona, vuelve a introducir tu respuesta")
        

    jugador = Tablero(1)
    maquina = Tablero(2)

    jugador.colocar_barcos()
    maquina.colocar_barcos()

    turno_jugador = True

    while True:
        if turno_jugador:
            print("\nTu tablero:")
            jugador.mostrar_tablero_propio()
            print("\nTablero enemigo:")
            maquina.mostrar_tablero_enemigo()

            x, y = pedir_coordenadas_usuario()

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
=======
>>>>>>> Stashed changes
