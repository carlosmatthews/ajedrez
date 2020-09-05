from ajedrez import representacion_piezas
from ajedrez import print_tablero

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

def limites_del_tablero(posicion):
    return posicion[0] >= 0 and posicion[0] <= 7 and posicion[1] >=0 and posicion[1] <= 7
   
def la_pieza_es_oponente(tablero, posicion1,posicion2):
    origen = tablero.get(posicion1)
    destino = tablero.get(posicion2)
    return origen[1] != destino[1]

def destino_es_rey(tablero,posicion2):
    destino = tablero.get(posicion2)
    print(destino)
    if destino == None:
        return False
    
    if destino[0] == "REY":
        return True
    else:
        return False    

def generar_posiciones_posibles(tablero, posicion, direccion):
   
    posicion_nueva = (posicion[0] + direccion[0], posicion[1] + direccion[1])
    movimientos_posibles= []
    
    while True:
        if casillero_esta_libre(tablero, posicion_nueva):
            movimientos_posibles.append (posicion_nueva)
            posicion_nueva = (posicion_nueva[0]+ direccion[0],posicion_nueva[1] + direccion[1])
        else:  #chequea si una posicion valida esta ocupada por oponene, y si true la agrega a posiciones_posibles
            if la_pieza_es_oponente(tablero,posicion,posicion_nueva) and not destino_es_rey(tablero,posicion_nueva):
                movimientos_posibles.append (posicion_nueva)
                posicion_nueva = (posicion_nueva[0]+ direccion[0],posicion_nueva[1] + direccion[1])
                break
            else:    
                break
        
        if not limites_del_tablero(posicion_nueva):
            break
    return movimientos_posibles


def mover_peon(tablero, posicion): # TODO: moviento 2 casiileros 1er jugada
    movimientos_posibles = []
    turno = obtner_pieza(tablero,posicion)
    turno = turno[1]
    
    #movientos posibles 1 para adelante
    def uno_adelante(tablero, posicion):
        if limites_del_tablero(posicion) and casillero_esta_libre(tablero, posicion):
            movimientos_posibles.append(posicion)
    #movimientos posibles comer/diagonal
    def pos_comer_diag(tablero,posicion1, posicion2):
        if not casillero_esta_libre(tablero, posicion2) :
            if la_pieza_es_oponente(tablero, posicion1, posicion2): 
                movimientos_posibles.append(posicion2) 

    #blancas hacia adelante
    mov_blancas = (posicion[0]+1,posicion[1]) 
    #negras hacia adelante
    mov_negras = (posicion[0]-1,posicion[1])  
    
    #para blancas diagonal
    mov_3 = (posicion[0]+1,posicion[1]-1)
    mov_4 =(posicion[0]+1,posicion[1]+1)
    #para negras diagonal
    mov_5 = (posicion[0]-1,posicion[1]-1)
    mov_6 = (posicion[0]-1,posicion[1]+1)
    
    if turno == BLANCO: 
        uno_adelante(tablero,mov_blancas)
        pos_comer_diag(tablero,posicion,mov_3)
        pos_comer_diag(tablero,posicion,mov_4)
    
    else:
        uno_adelante(tablero,mov_negras)  
        pos_comer_diag(tablero,posicion,mov_5)
        pos_comer_diag(tablero,posicion,mov_6)   
         
    return movimientos_posibles



def mover_caballo(posicion): # TODO: filtrar que no se salga del tablero
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

    movimientos_posibles = [mov_1,mov_2,mov_3,mov_4,mov_5,mov_6,mov_7,mov_8]

    return movimientos_posibles
    
def mover_torre(tablero,posicion):
    izquierda = generar_posiciones_posibles(tablero,posicion,(0,-1))
    derecha = generar_posiciones_posibles(tablero,posicion,(0,+1))
    arriba = generar_posiciones_posibles(tablero,posicion,(-1,0))
    abajo = generar_posiciones_posibles(tablero,posicion,(+1,0))
    
    movimientos_posibles= izquierda + derecha + arriba + abajo
                
    return movimientos_posibles


def mover_alfil(tablero, posicion):

    iz_arriba = generar_posiciones_posibles(tablero,posicion,(-1,-1))
    der_arriba = generar_posiciones_posibles(tablero,posicion,(-1,+1))
    iz_abajo = generar_posiciones_posibles(tablero,posicion,(+1,-1))
    der_abajo = generar_posiciones_posibles(tablero,posicion,(+1,+1))
    movimientos_posibles = iz_arriba + iz_abajo + der_arriba + der_abajo
    
    return movimientos_posibles


def mover_rey(tablero, posicion):
   fila = posicion[0]
   columna = posicion[1]
   movimientos_posibles = []
   adelantar = [(0,+1),(0,-1),(+1,0),(-1,0),(-1,-1),(+1,+1),(-1,+1),(+1,-1)]
   for e in adelantar:
       if casillero_esta_libre(tablero,(fila +e[0],columna+e[1])) and limites_del_tablero((fila +e[0],columna+e[1])):
            movimientos_posibles.append((fila +e[0],columna+e[1]))
   
   return movimientos_posibles

def mover_reina(tablero, posicion): 
    movimientos_posibles = []
    adelantar = [(0,+1),(0,-1),(+1,0),(-1,0),(-1,-1),(+1,+1),(-1,+1),(+1,-1)]
    for e in adelantar:        
            linea_de_posiciones = generar_posiciones_posibles(tablero,posicion,e)
            movimientos_posibles = movimientos_posibles + linea_de_posiciones
            print(movimientos_posibles)
    
    return movimientos_posibles


dicc_movimientos ={
    PEON : mover_peon,
    TORRE : mover_torre,
    CABALLO : mover_caballo,
    ALFIL : mover_alfil,
    REINA : mover_reina,
    REY : mover_rey
    }


