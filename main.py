#Importaciones necesarias
import numpy as np
from variables import *
from tablero import Tablero
from funciones import *

def juego(): # Esta función es la principal, la que ejecutará la partida
    respuesta = input("Hola! Bienvenido al juego Hundir la Flota. Sabes cómo funciona este juego? (si/no)").strip().lower().replace("í","i")
    if respuesta == "no":
        print ('''Instrucciones del juego: El objetivo del juego es hundir todos los barcos del enemigo antes de que él lo haga.
        El juego empieza teniendo, cada uno de vosotros, un tablero con unos barcos en posiciones que la otra persona no conoce.
        Tienes que decir a qué coordenada quieres impactar, como por ejemplo: Coordenada (1,2) o coordenada (3,5).
        Si aciertas, la otra persona dirá Tocado o Hundido. Sino, dirá Agua.
        Los turnos se alternan hasta que uno de los jugadores ya no tenga barcos.
        Gana la persona que hunda la flota primero. A por todas!''')
    elif respuesta == "si":
        print ("Pulsa Enter para empezar la partida")
    else:
        print ("Perdona, vuelve a introducir tu respuesta")
        return

    jugador = Tablero(id_jugador=1) # Crea el tablero para el jugador
    maquina = Tablero(id_jugador=2) # Crea el tablero para la máquina

    jugador.colocar_barcos()  # Coloca los barcos del jugador aleatoriamente
    maquina.colocar_barcos()  # Coloca los barcos de la máquina aleatoriamente

    turno_jugador = True # Esta variable alterna los turnos

    while True: # Empieza el turno del jugador

        if turno_jugador:
            print("\nTu tablero:")
            jugador.mostrar_tablero_propio()
            print("\nTablero enemigo:")
            maquina.mostrar_tablero_enemigo()

            x, y = pedir_coordenadas_usuario() # Le pide coordenadas al jugador

            resultado = maquina.recibir_disparo(x,y) # Procesa el disparo en el tablero de la máquina
            print ("Resultado:", resultado)
        
            if maquina.juego_terminado(): # Si todos los barcos de la máquina están hundidos...
                print ("Has ganado! Enhorabuena!")
                break

            turno_jugador = False # Cambia el turno a la máquina
        
        else: 
            print ("\n Turno de la máquina")
        
            x, y = pedir_coordenadas_maquina() # La máquina genera un disparo aleatorio

            resultado = jugador.procesar_disparo(x,y) # Registra el disparo de la máquina en el tablero del jugador
            print (f"La máquina dispara a {x+1}, {y+1}: {resultado}")
    
            if jugador.juego_terminado():  # Si todos los barcos del jugador están hundidos...
                print ("Has perdido :( la máquina ha hundido todos tus barcos.")
                break

            turno_jugador = True # Cambia el turno al jugador

if __name__ == "__main__":
    juego()  # Ejecuta la partida al iniciar el script
