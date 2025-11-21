def crear_tablero(filas_tablero=10, cols_tablero=10, agua="~"): # Crea un tablero vacío de tamaño filas x columnas con agua
    tablero = np.full((filas_tablero, cols_tablero,), agua) # El tablero es de 10x10 lleno de "~"
    return tablero

def tablero_bonito(tablero): # No entiendo esta función
    filas_tablero, cols_tablero = tablero.shape
    print("\n   " + " ".join([chr(65 + i) for i in range(cols_tablero)]))
    print("  " + "─" * (cols_tablero * 2))
    for i in range(filas_tablero):
        print(f"{i+1:2}│" + " ".join(tablero[i]) + "│")
    print("  " + "─" * (cols_tablero * 2))

def pedir_coordenadas_usuario(): # Le pide al jugador que ingrese coordenadas (x,y) del 1 al 10 y las convierte a índices 0-9
    while True:
        entrada = input("Introduce coordenadas tipo x,y (1-10): ")
        try:
            x_str, y_str = entrada.split(",")
            x = int(x_str) - 1
            y = int(y_str) - 1
            if 0 <= x < filas_tablero and 0 <= y < cols_tablero:
                return x, y # Ej: el usuario escribe "3,5": devuelve (2,4)
            else:
                print("Coordenadas fuera de rango. Intenta de nuevo.")
        except:
            print("Formato incorrecto. Usa x,y del 1 al 10.")

def pedir_coordenadas_maquina(): # Genera coordenadas aleatorias para que la máquina dispare
    x = np.random.randint(0,10)
    y = np.random.randint(0,10)
    return x, y # Ej: devuelve (7,3)
