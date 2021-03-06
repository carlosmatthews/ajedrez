from piezas_ajedrez import movimientos_pieza, posicion_del_rey, rey_esta_en_jaque, color_del_oponente, mover_en_tablero

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


class Partida:
    def __init__(self):
        self.juego_nuevo()

    def juego_nuevo(self):
        self.tablero = crear_tablero()
        self.jugador = BLANCO
        self.continua_juego = True
        self.ganador = None

    def cambio_turno(self):
        if self.jugador == BLANCO:
            self.jugador = NEGRO
        else:
            self.jugador = BLANCO

    def mover(self,posicion1,posicion2):
        mover_en_tablero(self.tablero, posicion1, posicion2)
        if jaque_mate(self.tablero, self.jugador):  # TODO: tambien puede terminar si hay empate
            self.continua_juego = False
            self.ganador = partida.jugador
        else:
            partida.cambio_turno()


partida = Partida()


def representacion_jugador(jugador):
    return "blancas" if jugador == BLANCO else "negras"


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


def convertir_de_frontend(posicion_front):
    posicion_front = posicion_front.upper()
    fila = ord(posicion_front[1]) - ord("1")
    if fila > 7 or fila < 0: 
        return print("posicion erronea")     
    
    columna = ord(posicion_front[0]) - ord("A")
    if columna > 7 or fila < 0: 
        return print("posicion erronea") 
        
    return fila, columna


def convertir_a_frontend(posicion):
    return chr(ord('A') + posicion[1]) + chr(ord('1') + posicion[0])


def chequear_movimiento_1(tablero,posicion1,jugador):
    #revisa que alla un pieza en casillero a mover
    if posicion1 not in tablero:
        mensaje = "no hay pieza en el casillero"
        return False, mensaje, None

    pieza_ataque, color_ataque = tablero.get(posicion1)
    # Revisa si eljijio pieza de acuerdo al color del turno
    if jugador != color_ataque:
        mensaje = "elija un pieza del color",jugador
        return False, mensaje, None
    else:
        # Revisa los movimietos pósibles segun la posicion elejida
        movimientos_posibles = movimientos_pieza(tablero, posicion1)
        if len(movimientos_posibles) > 0 :
            print_tablero(tablero,movimientos_posibles)  # TODO: sacar print de aca y ponerlo en el main, esto tb se usa en el server
            return True, None, movimientos_posibles
        else:
            mensaje = "la pieza no tiene movimientos posibles"
            return False, mensaje, None

def chequear_movimiento_2(tablero,posicion1,posicion2, movimientos_posibles):
    pieza_ataque = tablero.get(posicion1)
    color_ataque = pieza_ataque[1]
    #revisa si hay pieza en casillero destino y si es del oponente
    if posicion2 in tablero:
        pieza_destino = tablero.get((posicion2))
        color_destino = pieza_destino[1] #aca indice para obtener color
        if color_ataque == color_destino:
            mensaje = "no puede comer su propia pieza"
            return False, mensaje
        
    if posicion2 in movimientos_posibles:   #movimientos_pieza(tablero, posicion1):
        return True, None
    else:
        mensaje = "posicion invalida para esa pieza"
        return False, mensaje

    


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
    color_oponente = color_del_oponente(color_jugador)
    posicion_rey = posicion_del_rey(tablero,color_oponente)
    
    if rey_esta_en_jaque(tablero,posicion_rey):
        mov_del_rey = movimientos_pieza(tablero,posicion_rey,True,True)
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
    
    
