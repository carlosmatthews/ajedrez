from ajedrez import*
from piezas_ajedrez import*

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
    tablero[(2,7)] = (REY,      NEGRO)
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
        tablero[tupla]= (ASTERISCO, BLANCO)

    print_tablero(tablero)

# instruciones para probar las funciones de movimietnos de piezas



#probar_funcion(tablero_de_prueba(),posiciones)


"""f = movimientos_rey(tab_prue,(4,4))
c = rey_es_comido(tab_prue,(4,4),f)"""
"""
cava = movimientos_torre   (tab_prue,(0,0))
print(cava)
probar_funcion(tab_prue,[2,1])
"""

#print(movimientos_posibles_piezas(tab_prue,(0,4)))

#print(tab_prue.get((0,4)))

p = movimientos_peon(tab_prue,(1,3), False)

print(p)
probar_funcion(tab_prue, p)
