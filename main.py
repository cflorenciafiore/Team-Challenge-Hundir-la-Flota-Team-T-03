#Importaciones necesarias
from variables import flota, agua, barco, disparo_perdido, disparo_acertado, filas_tablero, cols_tablero
from tablero import Tablero 
from funciones import * 

def juego (): #Mensaje de bienvenida e instrucciones del juego
    
    respuesta = input("Hola! Bienvenido al juego Hundir la Flota. Sabes cómo funciona este juego? (si/no)").strip().lower().replace("í","i") #Indicamos estas 3 funciones para quitar espacios, devolver todo a minúsculas y, #si el usuario introduce una tilde, se cambia por una i para que no dé
                                                                                                                                            
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
        return
    #Dos nuevas instancias de la clase "Tablero" que crean los tableros para ambos jugadores (el humano y la máquina)
    jugador = Tablero(1)
    maquina = Tablero(2)
    #Métodos de la clase "Tablero" que coloca los barcos de cada jugador (estará en tablero.py)
    jugador.colocar_barcos() 
    maquina.colocar_barcos()
    #Variable que controla de quién es el turno. Si es True = turno del jugador. Si es False = turno de la máquina
    turno_jugador = True
    #Es el bucle principal. El "While = True" hace que el juego continúe hasta que alguien gane (hasta que haya un "break")
    while True: #Empieza el turno del jugador

        if turno_jugador: #Muestra los tableros
            print("\nTu tablero:")
            jugador.mostrar_tablero_propio() #Es un método dentro de la clase "Tablero" (estará en tablero.py)
            print("\nTablero enemigo:")
            maquina.mostrar_tablero_enemigo() #Es otro método dentro de la clase "Tablero" (estará en tablero.py)

            x, y = pedir_coordenadas_usuario() #Es un método que pide las coordenadas al usuario (estará en funciones.py)

            resultado = recibir_disparos (maquina,x,y) #Envía las coordenadas al tablero de la máquina y comprueba si el disparo es"Agua","Tocado" o "Hundido"
            print ("Resultado:", resultado) #Muestra el resultado de qué pasó con el disparo
        
            if juego_terminado (maquina): #Comprobamos si la máquina ya no tiene barcos; es decir,revisamos si el jugador ha ganado
                print ("Has ganado! Enhorabuena!")
                break #Sale del bucle principal y se termina el juego

            turno_jugador = False #Damos turno a la máquina
        
        else: #Turno de la máquina
        
            print ("\n Turno de la máquina") 
        
            x,y = pedir_coordenadas_maquina() #Método que pide las coordenadas a la máquina (estará en funciones.py)

            resultado = procesar_disparo (jugador, x,y) #Comprueba si en x,y hay barco y actualiza el tablero propio del jugador, según sea "Tocado", "Hundido" o "Agua"
            print (f"La máquina dispara a {x}, {y}: {resultado}") #Devolvemos un string con el resultado
    
            if juego_terminado (jugador): #Comprobamos si, tras el disparo de la máquina, el jugador no tiene barcos
                print ("Has perdido :( la máquina ha hundido todos tus barcos.")
                break #Salimos del bicle principal y terminamos la partida

            turno_jugador = True #Si el juego no ha terminado, vuelve a ser el turno del jugador     

if __name__ == "__main__":
    juego() #Ejecutamos la función juego() al ser el archivo del programa principal

