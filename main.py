#!/usr/bin/env python3
from ajedrez import*

tablero_inicio = crear_tablero()

print_tablero(tablero_inicio)
numero_de_jugada = 0
tablero = tablero_inicio.copy()
jugador = None

while True:
    if numero_de_jugada % 2 == 0 :
        jugador = BLANCO
    else:
        jugador = NEGRO

    print("turno de jugador",jugador)
    posicion1 = int(input("Posicion de la pieza a mover(fila/columna): "))
    posicion2 = int(input("Posicion de destino de la pieza(fila/columna): "))
    posicion1 = (posicion1 // 10),(posicion1 % 10 )
    posicion2 = (posicion2 // 10),(posicion2 % 10 )
   
    if chequear_movimiento(tablero,posicion1,posicion2,jugador):
        tablero = mover(tablero,posicion1,posicion2)
        print_tablero(tablero)
        numero_de_jugada += 1
