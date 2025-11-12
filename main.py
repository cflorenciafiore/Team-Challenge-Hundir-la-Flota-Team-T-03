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