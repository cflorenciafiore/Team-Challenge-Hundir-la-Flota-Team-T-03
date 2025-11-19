filas_tablero = 10 # Definimos el número de filas del tablero. Ej: tablero 10x10 tendrá filas 0 a 9
cols_tablero = 10 # Definimos el número de columnas del tablero. Ej: tablero 10x10 tendrá columnas 0 a 9

flota = {
    "b4_1": 4, # Este sería un barco de 4 casillas llamado b4_1. Ej.: horizontal ocupa (0,0),(0,1),(0,2),(0,3)
    "b3_1": 3, # Este sería un barco de 3 casillas llamado b3_1. Ej.: vertical ocupa (2,5),(3,5),(4,5)
    "b3_2": 3, # Este sería otro barco de 3 casillas llamado b3_2. Ej: horizontal ocupa (6,2),(6,3),(6,4)
    "b2_1": 2, # Este sería un barco de 2 casillas llamado b2_1. Ej: horizontal ocupa (1,7),(1,8)
    "b2_2": 2, # Este sería otro barco de 2 casillas llamado b2_2. Ej: vertical ocupa (5,0),(6,0)
    "b2_3": 2, # Este sería otro barco de 2 casillas llamado b2_3. Ej: horizontal ocupa (8,3),(8,4)
    "b1_1": 1, # Este sería un barco de 1 casilla llamado b1_1. Ej: (0,9)
    "b1_2": 1, # Este sería otro barco de 1 casilla llamado b1_2. Ej: (4,5)
    "b1_3": 1, # Este sería otro barco de 1 casilla llamado b1_3. Ej: (7,8)
    "b1_4": 1, # Este sería otro barco de 1 casilla llamado b1_4. Ej: (9,0)
}

agua = "~"  # Representamos el agua en el tablero. Ej: casilla sin barco: "~"
barco = "O" # Representamos un barco en el tablero. Ej: casilla con barco: "O"
disparo_perdido = "!" # Representamos un disparo fallido. Ej: se dispara a (1,1) y no hay barco: "!"
disparo_acertado = "X" # Representamos un disparo acertado. Ej: se dispara a (0,0) y hay barco: "X"