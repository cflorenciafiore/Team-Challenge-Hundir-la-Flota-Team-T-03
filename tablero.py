import numpy as np
import random

class Tablero:
    # Clase que gestiona la lógica del tablero de Hundir la Flota
    
    def __init__(self, filas=10, cols=10):
        self.filas = filas
        self.cols = cols
        self.agua = "~"
        self.barco = "O"
        self.disparo_perdido = "!"
        self.disparo_acertado = "X"
        
        self.tablero_oculto = np.full((filas, cols), self.agua, dtype=str)
        self.tablero_visible = np.full((filas, cols), self.agua, dtype=str)
        self.barcos = {}