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
    
def casillero_esta_libre(tablero,posicion):
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

def mover_torre(tablero,posicion):
    fila = posicion[0]
    columna = posicion[1]
    movimientos_posibles= []
    
    for n  in range(1,8-fila):
        if casillero_esta_libre(tablero, (fila + n,columna)):
            movimientos_posibles.append((fila + n,columna))
        else:
            break #todo comer pieza
    for n in range(1,8-columna):
        if casillero_esta_libre(tablero, (fila,columna + n)):
            movimientos_posibles.append((fila,columna + n))
        else:
            break #todo comer pieza
    for n  in range(fila+1):
        if casillero_esta_libre(tablero, (fila - n,columna)):
            movimientos_posibles.append((fila - n,columna))
        else:
            break #todo comer pieza
    for n in range(columna+1):
        if casillero_esta_libre(tablero, (fila,columna - n)):
            movimientos_posibles.append((fila,columna - n))
        else:
            break #todo comer pieza
                
    return movimientos_posibles



def mover_alfil(tablero, posicion):
    fila = posicion[0]
    columna = posicion[1]
    movimientos_posibles = []
    # diagonal 1
    rango_1 = min(posicion)+1
    for n in range(1,rango_1):
        if casillero_esta_libre(tablero, (fila-n,columna-n)):
            movimientos_posibles.append((fila-n,columna-n))
        else:
            break #todo comer pieza
    #diagonal 2
    rango_2 = min(fila, 7-columna)+1
    for n in range(1,rango_2+1):
        if casillero_esta_libre(tablero, (fila-n,columna+n)):    
            movimientos_posibles.append((fila-n,columna+n))
        else:
            break #todo comer pieza
    #diagonal 3
    rango_3 = min(6-fila,columna) +1
    for n in range (rango_3):
        if casillero_esta_libre(tablero,(fila+n,columna-n)):
            movimientos_posibles.append((fila+n,columna-n)) 
        else:
            break #todo comer pieza
    #diagonal 4 
    rango_4 = min(6-fila,7-columna) +1  
    for n in range (1,rango_4):   
        if casillero_esta_libre(tablero,(fila+n,columna+n)):
            movimientos_posibles.append((fila+n,columna+n))
        else:
            break #todo comer pieza

    
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
torre = mover_torre(tablero_inicio,(3,4))

probar_mov(torre)
print(torre)
print_tablero(tablero_inicio)