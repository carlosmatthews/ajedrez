#!/usr/bin/env python3
from ajedrez import *
from piezas_ajedrez import mover, color_del_oponente
from manejo_partidas import elegir_partida, guardar_partida


elegir_partida()

print_tablero(partida.tablero)

while True:
    
    print("turno de jugador", partida.jugador)
    posicion1 = input("Posicion de la pieza a mover(columna/fila): ")
    posicion1 = convertir_de_frontend(posicion1)
    if posicion1 == None:
        continue
    
    chequeo_pos_1, mensaje, movimientos_posibles =  chequear_movimiento_1(partida.tablero, posicion1, partida.jugador)
    if not chequeo_pos_1:     
        print(mensaje) # mensaje de error
        continue

    posicion2 = input("Posicion de destino de la pieza(columna/fila/): ")
    posicion2 = convertir_de_frontend(posicion2)
    chequeo_pos_2, mensaje = chequear_movimiento_2(partida.tablero, posicion1, posicion2, partida.jugador, movimientos_posibles)
    if chequeo_pos_2:
        mover(partida.tablero, posicion1, posicion2)
        print_tablero(partida.tablero)
        if jaque_mate(partida.tablero, partida.jugador):
            print("el", partida.jugador, " JAQUE MATE, gano el :",str(color_del_oponente(partida.jugador)))
            break
        partida.cambio_turno()
    else:
        print(mensaje)  # mensaje de error          
    
    guardar_partida(partida)







