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


def mover_peon(posicion):
    mov_1 = (posicion[0]+1,posicion[1])
    mov_2 = (posicion[0]-1,posicion[1])

    movimientos_posibles = [mov_1,mov_2]
    return movimientos_posibles

def limites_del_tablero(posicion):
    if posicion[0] >= 0 and posicion[0] <= 7 and posicion[1] >=0 and posicion[1] <= 7:
        return True



def adelantar_un_casillero(tablero,posicion,direccion_tupla):
    fila = posicion[0] + direccion_tupla[0]
    columna = posicion[1] + direccion_tupla [1]
    movimientos_posibles= []
    
    while True:
        if casillero_esta_libre(tablero, (fila,columna)):
            movimientos_posibles.append ((fila ,columna))
            fila = fila + direccion_tupla[0]
            columna = columna + direccion_tupla[1]
        else:
            break
        
        if fila > 7 or columna > 7:
            break
        if fila < 0 or columna < 0:
            break
       
    return movimientos_posibles
        
def mover_caballo(posicion):
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
    izquierda = adelantar_un_casillero(tablero,posicion,(0,-1))
    derecha = adelantar_un_casillero(tablero,posicion,(0,+1))
    arriba = adelantar_un_casillero(tablero,posicion,(-1,0))
    abajo = adelantar_un_casillero(tablero,posicion,(+1,0))
    
    movimientos_posibles= izquierda + derecha + arriba + abajo
                
    return movimientos_posibles


def mover_alfil(tablero, posicion):

    iz_arriba = adelantar_un_casillero(tablero,posicion,(-1,-1))
    der_arriba = adelantar_un_casillero(tablero,posicion,(-1,+1))
    iz_abajo = adelantar_un_casillero(tablero,posicion,(+1,-1))
    der_abajo = adelantar_un_casillero(tablero,posicion,(+1,+1))
    movimientos_posibles = iz_arriba + iz_abajo + der_arriba + der_abajo
    
    return movimientos_posibles

# hacer funciones faltantes
def mover_rey(tablero, posicion):
   fila = posicion[0]
   columna = posicion[1]
   movimientos_posibles = []
   adelantar = [(0,+1),(0,-1),(+1,0),(-1,0),(-1,-1),(+1,+1),(-1,+1),(+1,-1)]
   for e in adelantar:
       if casillero_esta_libre(tablero,(fila +e[0],columna+e[1])) and limites_del_tablero((fila +e[0],columna+e[1])):
            movimientos_posibles.append((fila +e[0],columna+e[1]))
   
   return movimientos_posibles

"""def mover_reina(tablero, posicion):
    movimientos_posibles = []
    for n in range(-1,2):
        for m in range(-1,2):
            f = adelantar_un_casillero(tablero,posicion,(n,m))
            movimientos_posibles.append(f)
            print(n,m)
    return movimientos_posibles
"""

dicc_movimientos ={
    PEON : mover_peon,
    TORRE : mover_torre,
    CABALLO : mover_caballo,
    ALFIL : mover_alfil,
    REINA : mover_reina,
    REY : mover_rey
    }


