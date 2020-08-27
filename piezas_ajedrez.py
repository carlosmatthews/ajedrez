from ajedrez import representacion_piezas
from ajedrez import print_tablero
#####esta parte despues se borrar es para facilitar mientras se escribe######
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
    
def casillero_esta_libre(posicion,tablero):
    if posicion not in tablero:
        return True

    
def mover_peon(posicion):
    mov_1 = (posicion[0]+1,posicion[1])   
    mov_2 = (posicion[0]-1,posicion[1])

    movimientos_posibles = [mov_1,mov_2]   
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

def mover_torre(posicion):
    fila = posicion[0]
    columna = posicion[1]
    movimientos_posibles= []
    
    for n  in range(8):
        movimientos_posibles.append((n,columna))
        movimientos_posibles.append((fila,n))
    indice_posicion_actual = movimientos_posibles.index(posicion)
    del movimientos_posibles[indice_posicion_actual]
    indice_posicion_actual = movimientos_posibles.index(posicion)
    del movimientos_posibles[indice_posicion_actual]

    return movimientos_posibles



def mover_alfil(posicion,tablero):
    fila = posicion[0]
    columna = posicion[1]
    movimientos_posibles = []
    # diagonal 1
    rango_1 = min(posicion)+1
    for n in range(1,rango_1):
        if casillero_esta_libre((fila-n,columna-n),tablero):
            movimientos_posibles.append((fila-n,columna-n))
        else:
            break
    #diagonal 2
    rango_2 = min(fila, 7-columna)+1
    for n in range(1,rango_2+1):
        if casillero_esta_libre((fila-n,columna+n),tablero):    
            movimientos_posibles.append((fila-n,columna+n))
        else:
            break
    #diagonal 3
    rango_3 = min(6-fila,columna) +1
    for n in range (rango_3):
        if casillero_esta_libre((fila+n,columna-n),tablero):
            movimientos_posibles.append((fila+n,columna-n)) 
        else:
            break
    #diagonal 4 
    rango_4 = min(6-fila,7-columna) +1  
    for n in range (1,rango_4):   
        if casillero_esta_libre((fila+n,columna+n),tablero):
            movimientos_posibles.append((fila+n,columna+n))
        else:
            break
    #filtrado de posicion no validas
    """for e in movimientos_posibles:
        if e[0] > 7 or e[1] > 7 :
            posicion_nula = movimientos_posibles.index(e)
            del movimientos_posibles[posicion_nula]
        if e[0] < 0 or e[1] < 0:
            posicion_nula = movimientos_posibles.index(e)
            del movimientos_posibles[posicion_nula]"""
    
    print(movimientos_posibles)
    return movimientos_posibles

# hacer funciones faltantes
def mover_rey(posicion):
   return print("todo rey")
def mover_reina(posicion):
    return print("todo reina")


dicc_movimientos ={
    PEON : mover_peon,
    TORRE : mover_torre,
    CABALLO : mover_caballo,
    ALFIL : mover_alfil,
    REINA : mover_reina,
    REY : mover_rey
    }


#esta funcion es solo para probar las otras...grafica dado una posicion de pieza de inicio.
#y la funcion q le damos segun la íeza a probar
def probar_mov(lista_posiciones):
    tablero = {}
  
    for tupla in lista_posiciones:
        tablero[tupla]=(PEON,BLANCO)

    print_tablero(tablero)
# instruciones para probar las funciones de movimietnos de piezas 
tablero_inicio= crear_tablero()
alfil = mover_alfil((3,4),tablero_inicio)

probar_mov(alfil)
print_tablero(tablero_inicio)