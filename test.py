from ajedrez import*
from piezas_ajedrez import*
from manejo_partidas import*
def tablero_de_prueba():
    
    tablero = {}
    tablero[(0,0)] = (TORRE,    BLANCO)
    tablero[(0,1)] = (CABALLO,  BLANCO)
    tablero[(0,2)] = (ALFIL,    BLANCO) 
    tablero[(0,3)] = (REINA,    BLANCO)
    tablero[(4,4)] = (REY,      BLANCO)
    tablero[(0,5)] = (ALFIL,    BLANCO)
    tablero[(0,6)] = (CABALLO,  BLANCO)
    tablero[(0,7)] = (TORRE,    BLANCO)
    #for i in range(8):
    tablero[1,3] = (PEON, BLANCO)
    
    tablero[(7,0)] = (TORRE,    NEGRO)
    tablero[(7,1)] = (CABALLO,  NEGRO)
    tablero[(7,2)] = (ALFIL,    NEGRO)
    tablero[(7,3)] = (REINA,    NEGRO)
    tablero[(2,6)] = (REY,      NEGRO)
    tablero[(7,5)] = (ALFIL,    NEGRO)
    tablero[(7,6)] = (CABALLO,  NEGRO)
    tablero[(5,7)] = (TORRE,    NEGRO)
    """for i in range(8):
        tablero[6,i] = (PEON, NEGRO)"""
    tablero[(2,2)]  = (PEON,     NEGRO)
    
    return tablero
# TABLEROS
tablero_inicio= crear_tablero()
tablero_vacio = {}
tab_prue = tablero_de_prueba()

#esta funcion es solo para probar las otras...grafica dado una posicion de pieza de inicio.
#y la funcion q le damos segun la píeza a probar



def probar_funcion(tablero ,lista_posiciones):
    tablero = tablero

    for tupla in lista_posiciones:
        if casillero_esta_libre(tablero,tupla):
            tablero[tupla]= (ASTERISCO, BLANCO)

    print_tablero(tablero)

# instruciones para probar las funciones de movimietnos de piezas




tablero_inicio = tab_prue
print_tablero(tablero_inicio)
numero_de_jugada = 0
tablero = tablero_inicio.copy()
jugador = BLANCO

""" while True:
    

    print("turno de jugador",jugador)
    posicion1 = input("Posicion de la pieza a mover(columna/fila): ")
    posicion1 = convertir_de_frontend(posicion1)
    if posicion1 == None:
        continue
    check_1 = chequear_movimiento_1(tablero,posicion1,jugador)
    if not check_1:
        continue

    posicion2 = input("Posicion de destino de la pieza(columna/fila/): ")
    posicion2 = convertir_de_frontend(posicion2)
    if posicion2 == None:
        continue
    if chequear_movimiento_2(tablero,posicion1,posicion2,jugador):
        mover(tablero,posicion1,posicion2)
        print_tablero(tablero)
        numero_de_jugada += 1
        if jaque_mate(tablero,jugador):
            print("el", jugador, "esta esta en JAQUE MATE, gano el oponente")
            break
        
        if jugador == BLANCO:
            jugador = NEGRO
        else:
            jugador = BLANCO      """
        

guardar_partida("B",tab_prue)
