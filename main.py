#!/usr/bin/env python3
from ajedrez import *
from piezas_ajedrez import mover, color_del_oponente
from manejo_partidas import elegir_partida, guardar_partida


tablero, jugador =  elegir_partida()

print_tablero(tablero)

while True:
    
    print("turno de jugador",jugador)
    posicion1 = input("Posicion de la pieza a mover(columna/fila): ")
    posicion1 = convertir_de_frontend(posicion1)
    if posicion1 == None:
        continue
    
    chequeo_pos_1, mensaje, movimientos_posibles =  chequear_movimiento_1(tablero,posicion1,jugador)
    if not chequeo_pos_1:     
        print(mensaje) # mensaje de error
        continue

    posicion2 = input("Posicion de destino de la pieza(columna/fila/): ")
    posicion2 = convertir_de_frontend(posicion2)
    chequeo_pos_2, mensaje = chequear_movimiento_2(tablero,posicion1,posicion2,jugador, movimientos_posibles)
    if chequeo_pos_2:
        mover(tablero,posicion1,posicion2)
        print_tablero(tablero)
        if jaque_mate(tablero,jugador):
            print("el", jugador, " JAQUE MATE, gano el :",str(color_del_oponente(jugador)))
            break
        if jugador == BLANCO:
            jugador = NEGRO
        else:
            jugador = BLANCO
    else:
        print(mensaje)  # mensaje de error          
    
    guardar_partida(jugador,tablero)        







