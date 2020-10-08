#!/usr/bin/env python3
from ajedrez import *
from piezas_ajedrez import mover


tablero_inicio = crear_tablero()
print_tablero(tablero_inicio)
numero_de_jugada = 0
tablero = tablero_inicio.copy()
jugador = BLANCO

while True:
    if jaque_mate(tablero,jugador):
        print("el", jugador, "esta esta en JAQUE MATE, gano el oponente")

    
    if numero_de_jugada % 2 == 0 :
        jugador = BLANCO
    else:
        jugador = NEGRO

    print("turno de jugador",jugador)
    posicion1 = input("Posicion de la pieza a mover(fila/columna): ")
    posicion1 = convercion_para_frontend(posicion1)
    check_1 = chequear_movimiento_1(tablero,posicion1,jugador)
    if not check_1:
        continue

    posicion2 = input("Posicion de destino de la pieza(fila/columna): ")
    posicion2 = convercion_para_frontend(posicion2)
    if chequear_movimiento_2(tablero,posicion1,posicion2,jugador):
        mover(tablero,posicion1,posicion2)
        print_tablero(tablero)
        numero_de_jugada += 1

        
    






