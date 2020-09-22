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
    posicion1 = input("Posicion de la pieza a mover(fila/columna): ")
    posicion1 = (posicion1 // 10),(posicion1 % 10 )
    check_1 = chequear_movimiento_1(tablero,posicion1,jugador)
    if not check_1:
        continue

    posicion2 = int(input("Posicion de destino de la pieza(fila/columna): "))
    posicion2 = (posicion2 // 10),(posicion2 % 10 )
   
    if chequear_movimiento_2(tablero,posicion1,posicion2,jugador):
        tablero = mover(tablero,posicion1,posicion2)
        print_tablero(tablero)
        numero_de_jugada += 1


def convercion_para_frontend(posicion_fornt):
    dic_front = {
        "a": 0,
        "b": 1,
        "c": 2,
        "d": 3,
        "e" :4,
        "f": 5,
        "g": 6,
        "h": 7
    }
    
    fila = (int(posicion_fornt[0])) -1
    columna =  dic_front.get(posicion_fornt[1])
  
    return fila, columna
    

print(convercion_para_frontend("6b"))



