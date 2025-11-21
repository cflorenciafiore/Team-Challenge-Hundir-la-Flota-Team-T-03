import numpy as np
from variables import *
import random

class Tablero: # La clase Tablero manejará toda la lógica de un tablero. Cada objeto Tablero representa el tablero de un jugador, sus barcos y disparos. Ej: jugador = Tablero(1) crea un tablero para el jugador 1.
    
    def __init__(self, id_jugador, filas=10, cols=10):
        self.id = id_jugador # Almacena el ID del jugador. Ej: 1 para jugador, 2 para máquina
        self.filas = filas  # Número de filas del tablero
        self.cols = cols  # Número de columnas del tablero
        self.agua = "~" # Símbolo para agua
        self.barco = "O" # Símbolo para barco
        self.disparo_perdido = "!" # Símbolo para disparo perdido
        self.disparo_acertado = "X" # Símbolo para disparo acertado
        
        self.tablero_oculto = np.full((filas, cols), self.agua, dtype=str) # Crea un tablero oculto (el que tendrá los barcos) lleno de agua. Ej: 10x10 lleno de "~"
        self.tablero_visible = np.full((filas, cols), self.agua, dtype=str) # Crea un tablero visible (el que ve el enemigo) lleno de agua. Ej: 10x10 lleno de "~"
        self.barcos = {} # Almacena las posiciones de los barcos. Ej: {"b4_1":[(0,0),(0,1),(0,2),(0,3)]}

    def colocar_barcos(self): # Esta función colocará la flota (la que definimos en la variable "flota") en el tablero aleatoriamente (en horizontal o vertical sin superponerse)
        for nombre, tamaño in flota.items(): # Recorre cada barco y su tamaño. Ej: "b4_1", 4
            colocado = False # Indica que el barco no está colocado todavía
            while not colocado: # Repite lo siguiente hasta que el barco se coloque correctamente
                orientacion = random.choice(["H", "V"]) # Escoge la orientación entre horizontal o vertical aleatoriamente
                if orientacion == "H": # Si escoge la orientación horizontal...
                    x = random.randint(0, self.filas-1) # Escoge una fila aleatoria desde la primera (0) hasta la última (self.filas-1)
                    y = random.randint(0, self.cols - tamaño) # Escoge una columna aleatoria desde la primera (0) hasta la última posible (es decir, la última restando el tamaño del barco para que el barco horizontal quepa dentro del tablero) (self.cols - tamaño)
                    if all(self.tablero_oculto[x, y+i] == self.agua for i in range(tamaño)): # El if verifica si todas las casillas en las que se quiere colocar el barco están vacías. Ej: si el barco b1_3 se coloca en la fila x=4 y columna inicial y=4, verifica tablero_oculto[2,4], [2,5], [2,6] y todas deben ser agua "~"
                            # El for recorre cada casilla del barco para colocarla en el tablero. Ej: barco b1_3: i = 0, 1 y 2 (columna 4, 5 y 6)
                            for i in range(tamaño):
                                self.tablero_oculto[x, y+i] = self.barco # Coloca la casilla del barco en la posición correspondiente, marcándola con "O". Ej: tablero_oculto[2,4] = "O", tablero_oculto[2,5] = "O", tablero_oculto[2,6] = "O"
                            colocado = True # Cambia colocado a True para salir del bucle while not, porque ya se colocó correctamente. Si no se hubiera podido colocar en la primera vuelta porque "choca" con otros elementos, el buble se repetería hasta que se pueda
                else:  # Si escoge la orientación vertical...
                    x = random.randint(0, self.filas - tamaño) # Escoge una fila aleatoria desde la primera (0) hasta la última posible (es decir, la última restando el tamaño del barco para que el barco vertical quepa dentro del tablero) (self.filas - tamaño)
                    y = random.randint(0, self.cols-1) # Escoge una columna aleatoria desde la primera (0) hasta la última (self.cols-1)
                    if all(self.tablero_oculto[x+i, y] == self.agua for i in range(tamaño)):
                        for i in range(tamaño):
                            self.tablero_oculto[x+i, y] = self.barco
                        colocado = True

    def mostrar_tablero_propio(self): # Muestra el tablero del jugador (sus barcos y disparos)
    # Ej: si tablero_oculto tiene un barco en (0,0),(0,1),(0,2),(0,3) y agua en el resto, se verá:
    # [['O', 'O', 'O', 'O', '~', '~', '~', '~', '~', '~'],
    #  ['~', '~', '~', '~', '~', '~', '~', '~', '~', '~'], ...]
        print(self.tablero_oculto)

    def mostrar_tablero_enemigo(self): # Muestra el tablero que ve el enemigo (sólo los disparos)
    # Ej: si se disparó a (0,0) y no había barco, tablero_visible[0,0]='!', se verá:
    # [['!', '~', '~', '~', '~', '~', '~', '~', '~', '~'], ...]
        print(self.tablero_visible)

    def recibir_disparo(self, x, y): # Registra un disparo recibido por este tablero, cambia el tablero_oculto y devuelve resultado
        if self.tablero_oculto[x, y] == self.barco: # Hay un barco
            self.tablero_oculto[x, y] = self.disparo_acertado # Marca la casilla como 'X' porque el disparo acertó
            return "Tocado" # Ej: disparo en (0,0) que tenía barco: tablero_oculto[0,0]='X' y devuelve "Tocado"
        else:
            self.tablero_oculto[x, y] = self.disparo_perdido # No hay barco. Marca la casilla como '!' porque el disparo falló
            return "Agua" # Ej: disparo en (1,1) que no tenía barco: tablero_oculto[1,1]='!' y devuelve "Agua"

    def procesar_disparo(self, x, y): # Registra el disparo que este jugador hace al enemigo. Cambia tablero_visible y devuelve resultado
        if self.tablero_oculto[x, y] == self.barco:
            self.tablero_visible[x, y] = self.disparo_acertado # Marca la casilla en el tablero visible del enemigo como 'X'
            return "Tocado" # Ej: disparo a (0,0) que tenía barco: tablero_visible[0,0]='X' y devuelve "Tocado"
        else:
            self.tablero_visible[x, y] = self.disparo_perdido  # Marca la casilla en el tablero visible del enemigo como '!'
            return "Agua" # Ej: disparo a (1,1) sin barco: tablero_visible[1,1]='!', devuelve "Agua"

    def juego_terminado(self):
        if self.barco in self.tablero_oculto: # Si hay al menos un "O" en el tablero...
            return False # Ej: tablero_oculto = [["O","X","~"],["~","~","O"]]: devuelve False porque quedan barcos indicando que el juego no ha terminado
        else: # Si no hay ningún "O" en el tablero...
            return True # Ej: tablero_oculto = [["X","X","X"],["~","~","~"]]: devuelve True porque todos los barcos están hundidos indicando que el juego termina
