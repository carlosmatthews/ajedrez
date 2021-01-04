#!/usr/bin/env python3

from ajedrez import partida, print_tablero, convertir_de_frontend, chequear_movimiento_1, chequear_movimiento_2, representacion_jugador
from manejo_partidas import elegir_partida, guardar_partida

# FIXME: el tema de cargar una partida con partida = cargar_partida() trae problemas porque no se actualiza aca y siempre queda el tablero nuevo
elegir_partida()
print_tablero(partida.tablero)

while True:
    
    print("turno de jugador", partida.jugador)
    posicion1 = input("Posicion de la pieza a mover (columna/fila): ")
    posicion1 = convertir_de_frontend(posicion1)
    if posicion1 == None:
        continue
    
    chequeo_pos_1, mensaje, movimientos_posibles =  chequear_movimiento_1(partida.tablero, posicion1, partida.jugador)
    if not chequeo_pos_1:     
        print(mensaje) # mensaje de error
        continue

    posicion2 = input("Posicion de destino de la pieza(columna/fila/): ")
    posicion2 = convertir_de_frontend(posicion2)
    puede_mover, mensaje = chequear_movimiento_2(partida.tablero, posicion1, posicion2, movimientos_posibles)
    if puede_mover:
        partida.mover(posicion1,posicion2)
        guardar_partida(partida)
        print_tablero(partida.tablero)
        if not partida.continua_juego:
            print("JAQUE MATE, ganaron las ", representacion_jugador(partida.ganador))
            break
    else:
        print(mensaje)  # mensaje de error
