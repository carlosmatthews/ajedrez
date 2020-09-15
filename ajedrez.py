from piezas_ajedrez import movimientos_pieza

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
        (TORRE,    BLANCO):"♖",
        (CABALLO,  BLANCO):"♘",
        (ALFIL,    BLANCO):"♗",
        (REINA,    BLANCO):"♕",
        (REY,      BLANCO):"♔",
        (PEON,     BLANCO):"♙",
        (TORRE,    NEGRO):"♜",
        (CABALLO,  NEGRO):"♞",
        (ALFIL,    NEGRO):"♝",
        (REINA,    NEGRO):"♛",
        (REY,      NEGRO):"♚",
        (PEON,     NEGRO):"♟",
        (ASTERISCO, BLANCO):"*",    
        (ASTERISCO, NEGRO): "*" 
    }
    return convercion[nombre_pieza]

def chequear_movimiento(tablero,posicion1,posicion2,jugador): 
    #revisa que alla un pieza en casillero a mover
    if posicion1 not in tablero:
        print("no hay pieza en el casillero")
        return False 
       
    pieza_ataque = tablero.get(posicion1)
    print(pieza_ataque)
    color_ataque = pieza_ataque[1]
    #revisa si eljijio pieza de acuerdo al color del turno
    if jugador != color_ataque:
        print("elija un pieza del color",jugador)         
        return False   
    
    #revisa si hay pieza en casillero destino y si es del oponente
    if posicion2 in tablero:
        pieza_destino = tablero.get((posicion2))
        color_destino = pieza_destino[1] #aca indice para obtener color
        if color_ataque == color_destino:
            print("no puede comer su propia pieza")
            return False
    #revisa los movimietos pósibles segun tipo de pieza
    if posicion2 in movimientos_pieza(tablero,posicion1):
        return True
    else:
        print("posicion invalida para esa pieza")
        return False



    return True




def mover(tablero, posicion1, posicion2):
    pieza = tablero.get(posicion1)
    tablero[posicion2] = pieza
    del tablero[posicion1] 
    
    return tablero        
   
    

def print_tablero(tablero):  
    print()
    print("  ", end="")
    for n in range(8):
        print(f"  {n} ",end="")  # MARTO: preguntame por esta notacion f"" para strings
    print()        
    for fila in range(8):
        print(" ", " ——-" * 8)
        print(fila, end=" ")      
        for col in range(8):
            pieza = tablero.get((fila,col))
            simbolo = representacion_piezas(pieza)
            print(f"| {simbolo} ", end="")
        print("|")    
    print(" ", " ———" * 8)
    print()

