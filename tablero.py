import numpy as np
import random

from variables import flota, agua, barco, disparo_perdido, disparo_acertado

class Tablero:
    # Clase que gestiona la lógica del tablero de Hundir la Flota
    
    def __init__(self, id_jugador=None, filas=10, cols=10):
        self.id_jugador = id_jugador
        self.filas = filas
        self.cols = cols
        self.agua = agua
        self.barco = barco
        self.disparo_perdido = disparo_perdido
        self.disparo_acertado = disparo_acertado
        
        self.tablero_oculto = np.full((filas, cols), self.agua, dtype=str)
        self.tablero_visible = np.full((filas, cols), self.agua, dtype=str)
        self.barcos = {}  # dict para almacenar las posiciones de cada barco

    def colocar_barcos(self):
        for nombre, eslora in flota.items():
            colocado = False
            while not colocado:
                #0 para horizontal, 1 para vertical
                orientacion = random.randint(0, 1)
                if orientacion == 0:
                    x = random.randint(0, self.filas - 1)
                    y = random.randint(0, self.cols - eslora)
                    posiciones = [(x, y + i) for i in range(eslora)]
                else:
                    x = random.randint(0, self.filas - eslora)
                    y = random.randint(0, self.cols - 1)
                    posiciones = [(x + i, y) for i in range(eslora)]
                
                # Verificar si las posiciones están libres
                solapa = False
                for pos in posiciones:
                    if self.tablero_oculto[pos] != self.agua:
                        solapa = True
                        break
                if not solapa:
                    for pos in posiciones:
                        self.tablero_oculto[pos] = self.barco
                    self.barcos[nombre] = posiciones
                    colocado = True

    def recibir_disparo(self, x, y):
        if not (0 <= x < self.filas and 0 <= y < self.cols):
            return "Coordenadas inválidas"
        
        celda = self.tablero_oculto[x, y]
        
        if celda == self.barco:
            self.tablero_oculto[x, y] = self.disparo_acertado
            self.tablero_visible[x, y] = self.disparo_acertado
            barco_hundido = False
            for nombre, posiciones in self.barcos.items():
                if (x, y) in posiciones:
                    # Comprobar si todas las posiciones del barco están acertadas
                    barco_hundido = all(self.tablero_oculto[pos] == self.disparo_acertado for pos in posiciones)
                    if barco_hundido:
                        return "Hundido"
                    else:
                        return "Tocado"
            return "Tocado"
        
        elif celda == self.agua:
            self.tablero_oculto[x, y] = self.disparo_perdido
            self.tablero_visible[x, y] = self.disparo_perdido
            return "Agua"
        
        else:
            return "Ya disparado"

    def hay_barcos_vivos(self):
        """
        checkea si queda algun barco vivo (celdas con 'O' en tablero_oculto).
        devuelve True si hay barcos vivos, False si no.
        """
        return np.any(self.tablero_oculto == self.barco)

    def get_tablero_visible(self):
        return self.tablero_visible

    def get_tablero_oculto(self):
        return self.tablero_oculto

    def mostrar_tablero_propio(self):
        self._imprimir_tablero(self.tablero_oculto)

    def mostrar_tablero_enemigo(self):
        self._imprimir_tablero(self.tablero_visible)

    def _imprimir_tablero(self, tablero):
        """
        metodo auxiliar para imprimir un tablero de forma guapa.
        """
        filas, cols = tablero.shape
        print("   " + " ".join([chr(65 + i) for i in range(cols)]))
        print("  " + "─" * (cols * 2 + 1))
        for i in range(filas):
            print(f"{i+1:2}│" + " ".join(tablero[i]) + "│")
        print("  " + "─" * (cols * 2 + 1))