
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



def obtner_pieza(tablero, posicion):
    pieza = tablero.get(posicion)
    tipo_de_pieza = pieza[0]
    color_pieza = pieza[1]
    return tipo_de_pieza, color_pieza


def casillero_esta_libre(tablero,posicion):
    if posicion not in tablero:
        return True

def dentro_del_tablero(posicion):
    return posicion[0] >= 0 and posicion[0] <= 7 and posicion[1] >=0 and posicion[1] <= 7
   
def la_pieza_es_oponente(tablero, posicion1,posicion2):
    origen = tablero.get(posicion1)
    destino = tablero.get(posicion2)
    return origen[1] != destino[1]

def destino_es_rey(tablero,posicion2):
    destino = tablero.get(posicion2)
    if destino == None:
        return False
    
    if destino[0] == "REY":
        return True
    else:
        return False    

def se_puede_comer(tablero, posicion, posicion2):
    if not casillero_esta_libre(tablero, posicion2):
        salida = la_pieza_es_oponente(tablero, posicion, posicion2) and not destino_es_rey(tablero, posicion2)
        return salida
    else:
        False
    

def generar_posiciones_posibles(tablero, posicion, direccion):
    movimientos_posibles= []
    posicion_nueva = posicion
    while True:
        posicion_nueva = (posicion_nueva[0] + direccion[0], posicion_nueva[1] + direccion[1])
        if not dentro_del_tablero(posicion_nueva):
            break

        if casillero_esta_libre(tablero, posicion_nueva):
            movimientos_posibles.append(posicion_nueva)
        else:  
            if se_puede_comer(tablero, posicion, posicion_nueva):
                movimientos_posibles.append(posicion_nueva)     
            break
    return movimientos_posibles


def movimientos_peon(tablero, posicion, posiciones_que_comen = False): 
    movimientos_posibles = []
    jugador = obtner_pieza(tablero,posicion)
    jugador = jugador[1] 
 
    #movientos posibles hacia adelante
    def para_adelante(tablero, movimiento):
        if dentro_del_tablero(movimiento) and casillero_esta_libre(tablero, movimiento):
            movimientos_posibles.append(movimiento)
    #movimientos posibles comer/diagonal
    def pos_comer_diag(tablero,posicion, movimiento):
        if dentro_del_tablero(posicion):
            if se_puede_comer(tablero,posicion,movimiento): 
                movimientos_posibles.append(movimiento) 
        
    if jugador == BLANCO:
        #blancas hacia adelante
        mov_adelante = (posicion[0]+1,posicion[1]) 
        #blancas 1er jugada
        primer_jugada = (posicion[0]+2,posicion[1])
        
    else:
        #negras hacia adelante
        mov_adelante = (posicion[0]-1,posicion[1])  
        #negras 1er jugada
        primer_jugada = (posicion[0]-2,posicion[1])   
        
    pos_comer_diag(tablero,posicion, (mov_adelante[0], mov_adelante[1]+1))
    pos_comer_diag(tablero,posicion, (mov_adelante[0], mov_adelante[1]-1))
    
    if not posiciones_que_comen:
        para_adelante(tablero,mov_adelante)    
        if posicion[0] == 1 and jugador == BLANCO  or jugador == NEGRO and \
        posicion[0] == 6:
            para_adelante(tablero,primer_jugada) #mov 1er jugada
            
    return movimientos_posibles



def movimientos_caballo(tablero,posicion, posiciones_que_comen = False): 
    fila = posicion[0]
    columna = posicion[1]
    mov_1 = (fila -2, columna -1)
    mov_2 = (fila -2, columna +1)
    mov_3 = (fila -1, columna -2)
    mov_4 = (fila -1, columna +2)
    mov_5 = (fila +1, columna -2)
    mov_6 = (fila +1,columna  +2)
    mov_7 = (fila +2, columna -1)
    mov_8 = (fila +2, columna +1)

    lista_movimientos = [mov_1,mov_2,mov_3,mov_4,mov_5,mov_6,mov_7,mov_8]
    movimientos_posibles = []
    
    #filtrado posiciones fuera del tablero , posciones ocupadas y si se puede comer
    for i in range(8):
        if dentro_del_tablero(lista_movimientos[i]):
            if casillero_esta_libre(tablero, lista_movimientos[i]):
                movimientos_posibles.append(lista_movimientos[i])
            else:
                if la_pieza_es_oponente(tablero,posicion,lista_movimientos[i]):
                    movimientos_posibles.append(lista_movimientos[i])                
            
    return movimientos_posibles
    
def movimientos_torre(tablero,posicion, posiciones_que_comen = False):
    izquierda = generar_posiciones_posibles(tablero,posicion,(0,-1))
    derecha = generar_posiciones_posibles(tablero,posicion,(0,+1))
    arriba = generar_posiciones_posibles(tablero,posicion,(-1,0))
    abajo = generar_posiciones_posibles(tablero,posicion,(+1,0))
    
    movimientos_posibles= izquierda + derecha + arriba + abajo
                    
    return movimientos_posibles

def movimientos_alfil(tablero, posicion, posiciones_que_comen = False):
    iz_arriba = generar_posiciones_posibles(tablero,posicion,(-1,-1))
    der_arriba = generar_posiciones_posibles(tablero,posicion,(-1,+1))
    iz_abajo = generar_posiciones_posibles(tablero,posicion,(+1,-1))
    der_abajo = generar_posiciones_posibles(tablero,posicion,(+1,+1))
    movimientos_posibles = iz_arriba + iz_abajo + der_arriba + der_abajo
    
    return movimientos_posibles




def movimientos_reina(tablero, posicion, posiciones_que_comen = False): 
    movimientos_posibles = []
    adelantar = [(0,+1),(0,-1),(+1,0),(-1,0),(-1,-1),(+1,+1),(-1,+1),(+1,-1)]
    for movimiento in adelantar:        
            linea_de_posiciones = generar_posiciones_posibles(tablero,posicion,movimiento)
            movimientos_posibles = movimientos_posibles + linea_de_posiciones
           
    
    return movimientos_posibles



def movimientos_rey(tablero, posicion, posiciones_que_comen=False): 
    movimientos_posibles = []
    adelantar = [(0,+1),(0,-1),(+1,0),(-1,0),(-1,-1),(+1,+1),(-1,+1),(+1,-1)]

    for movimiento in adelantar:
        posicion2 = (posicion[0] + movimiento[0], posicion[1] + movimiento[1])
        if not dentro_del_tablero(posicion2):
            continue
        if casillero_esta_libre(tablero, posicion2) or se_puede_comer(tablero, posicion, posicion2):
            movimientos_posibles.append(posicion2)
    
    return movimientos_posibles




#esta funcion elije la funcion para cada pieza segun la posicion 
def movimientos_pieza(tablero,posicion, posiciones_que_comen = False, filtrar_rey_en_jaque = True):
    pieza = tablero.get(posicion)
    tipo_de_pieza = pieza[0]
    color_jugador = pieza[1]

    dicc_fun_movimientos ={
        PEON : movimientos_peon,
        TORRE : movimientos_torre,
        CABALLO : movimientos_caballo,
        ALFIL : movimientos_alfil,
        REINA : movimientos_reina,
        REY : movimientos_rey
    }

    funcion_pieza = dicc_fun_movimientos.get(tipo_de_pieza)
    movimientos = funcion_pieza(tablero, posicion, posiciones_que_comen = posiciones_que_comen)
    #FIXME: ANALIZAR ESTO....

    if filtrar_rey_en_jaque :
        def filtrado_rey_a_salvo(movimiento):
            tablero_con_movimientos = tablero.copy()
            mover (tablero_con_movimientos, posicion,movimiento) 
            posicion_rey = posicion_del_rey(tablero_con_movimientos,color_jugador)
            return not rey_esta_en_jaque(tablero_con_movimientos,posicion_rey)   
    
        movimientos = list(filter(filtrado_rey_a_salvo,movimientos))
         
    return movimientos   
  
   
#TODO: ver funciones lamda 
def rey_esta_en_jaque(tablero,posicion_rey):
    
    for posicion, pieza in tablero.items():
        if la_pieza_es_oponente(tablero,posicion,posicion_rey):
            movimientos_de_pieza = movimientos_pieza(tablero,posicion,posiciones_que_comen = True,filtrar_rey_en_jaque = False)
            if posicion_rey in movimientos_de_pieza:
                return True
    return False
        


def posicion_del_rey(tablero, jugador):
    for posicion,pieza in tablero.items():
        if pieza == (REY,jugador):
            return posicion
        

def mover(tablero, posicion1, posicion2):
    pieza = tablero.get(posicion1)
    tablero[posicion2] = pieza
    del tablero[posicion1]   


def piezas_de_un_color(tablero,color_jugador):
    lista_piezas= []
    for posicion, pieza in tablero.items:
        if pieza[1] == color_jugador:
            lista_piezas.insert((posicion,pieza))
    return lista_piezas


def color_del_oponente(color_jugador):
    if color_jugador == BLANCO:
        return NEGRO
    else:
        return BLANCO