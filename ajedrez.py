from piezas_ajedrez import movimientos_pieza, posicion_del_rey, rey_es_comido, rey_esta_en_jaque

# tipos de piezas:
REY = "R"
REINA = "RA"
CABALLO = "C"
ALFIL = "A"
TORRE = "T"
PEON = "P"

# colores de piezas:
BLANCO = "B"
NEGRO = "N"
#   marcas de casillero
ASTERISCO = "*"



def crear_tablero():
    tablero = {}
    tablero[(0,0)] = (TORRE,    BLANCO)
    tablero[(0,1)] = (CABALLO,  BLANCO)
    tablero[(0,2)] = (ALFIL,    BLANCO)
    tablero[(0,3)] = (REINA,    BLANCO)
    tablero[(0,4)] = (REY,      BLANCO)
    tablero[(0,5)] = (ALFIL,    BLANCO)
    tablero[(0,6)] = (CABALLO,  BLANCO)
    tablero[(0,7)] = (TORRE,    BLANCO)
    for i in range(8):
        tablero[1,i] = (PEON, BLANCO)
    tablero[(7,0)] = (TORRE,    NEGRO)
    tablero[(7,1)] = (CABALLO,  NEGRO)
    tablero[(7,2)] = (ALFIL,    NEGRO)
    tablero[(7,3)] = (REINA,    NEGRO)
    tablero[(7,4)] = (REY,      NEGRO)
    tablero[(7,5)] = (ALFIL,    NEGRO)
    tablero[(7,6)] = (CABALLO,  NEGRO)
    tablero[(7,7)] = (TORRE,    NEGRO)
    for i in range(8):
        tablero[6,i] = (PEON, NEGRO)
    return tablero

def representacion_piezas(nombre_pieza):
   # https://qwerty.dev/chess-symbols-to-copy-and-paste/
    if nombre_pieza is None:
        return " "

    convercion = {
        (TORRE,    BLANCO):"♜",
        (CABALLO,  BLANCO):"♞",
        (ALFIL,    BLANCO):"♝",
        (REINA,    BLANCO):"♛",
        (REY,      BLANCO):"♚",
        (PEON,     BLANCO):"♟",
        (TORRE,    NEGRO):"♖",
        (CABALLO,  NEGRO):"♘",
        (ALFIL,    NEGRO):"♗",
        (REINA,    NEGRO):"♕",
        (REY,      NEGRO):"♔",
        (PEON,     NEGRO):"♙",
        (ASTERISCO, BLANCO):"*",
        (ASTERISCO, NEGRO): "*"
    }
    return convercion[nombre_pieza]

def convercion_para_frontend(posicion_front):
    fila = ord(posicion_front[0]) -49
    if fila > 7 or fila < 0: 
        return print("posicion erronea")     
    
    columna = ord(posicion_front[1]) - 97 
    if columna > 7 or fila < 0: 
        return print("posicion erronea") 
        
    return fila, columna
    



movimientos_posibles = []
def chequear_movimiento_1(tablero,posicion1,jugador):
    #revisa que alla un pieza en casillero a mover
    if posicion1 not in tablero:
        print("no hay pieza en el casillero")
        return False

    pieza_ataque = tablero.get(posicion1)
    color_ataque = pieza_ataque[1]
    #revisa si eljijio pieza de acuerdo al color del turno
    if jugador != color_ataque:
        print("elija un pieza del color",jugador)
        return False
    else:
        global movimientos_posibles
        #revisa los movimietos pósibles segun la posicion elejida
        movimientos_posibles = movimientos_pieza(tablero, posicion1)
        if len(movimientos_posibles) > 0 :
            print_tablero(tablero,movimientos_posibles)
            return True
        else:
            print("la pieza no tiene movimientos posibles")
            return False    

def chequear_movimiento_2(tablero,posicion1,posicion2,jugador):
   
    pieza_ataque = tablero.get(posicion1)
    color_ataque = pieza_ataque[1]
    #revisa si hay pieza en casillero destino y si es del oponente
    if posicion2 in tablero:
        pieza_destino = tablero.get((posicion2))
        color_destino = pieza_destino[1] #aca indice para obtener color
        if color_ataque == color_destino:
            print("no puede comer su propia pieza")
            return False

    if posicion2 in movimientos_posibles:   #movimientos_pieza(tablero, posicion1):
        return True
    else:
        print("posicion invalida para esa pieza")
        return False

    return True


def print_tablero(tablero,posiciones_posibles = []):
    letras ="abcdefgh" #letras para el print de las filas
    print()
    print("  ", end="")
    for n in range(8):
        print(f"  {letras[n]} ",end="")  # MARTO: preguntame por esta notacion f"" para strings
    print()
    for fila in range(7,-1,-1):
        print(" ", " ——-" * 8)
        print(fila +1 , end=" ")
        for col in range(8):
            posicion = (fila,col)
            pieza = tablero.get((fila,col))
            simbolo = representacion_piezas(pieza)
            if posicion in posiciones_posibles:
                aste = "*"
            else:
                aste = " "
            print(f"|{aste}{simbolo} ", end="")
        print("|")
    print(" ", " ———" * 8)
    print()



  



def jaque_mate(tablero,color_jugador):
    posicion_rey = posicion_del_rey(tablero,color_jugador)
    if rey_esta_en_jaque(tablero,posicion_rey):
        mov_del_rey = movimientos_pieza(tablero,posicion_rey,True,True)
        print(mov_del_rey)
        if len(mov_del_rey) < 1:
           return True
    return False        


    #3 para todos los movimientos posibles en todas las piezas el rey queda siempre amenazado.
    # para las posiciones de mis piezas, generar un tablero_alternativo
    # que con cada posicion posible de todas mis piezas, mande a ver
    # si el rey esta en jaque o no.
     
    # piezas = piezas color del rey
    # for pieza in piezas: 
    #   movimientos = movimientos_pieza
    #   if len(movimientos) > 0 :
    #       return False       
    #
    #  return True
    #    
    # #TODO: caso de ahogado.    
    
    
