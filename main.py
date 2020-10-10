#!/usr/bin/env python3
from ajedrez import *
from piezas_ajedrez import mover


tablero_inicio = crear_tablero()
print_tablero(tablero_inicio)
numero_de_jugada = 0
tablero = tablero_inicio.copy()
jugador = BLANCO

while True:
    

    print("turno de jugador",jugador)
    posicion1 = input("Posicion de la pieza a mover(columna/fila): ")
    posicion1 = convercion_para_frontend(posicion1)
    if posicion1 == None:
        continue
    check_1 = chequear_movimiento_1(tablero,posicion1,jugador)
    if not check_1:
        continue

    posicion2 = input("Posicion de destino de la pieza(columna/fila/): ")
    posicion2 = convercion_para_frontend(posicion2)
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
            jugador = BLANCO    
        
    






