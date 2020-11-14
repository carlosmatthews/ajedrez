#!/usr/bin/env python3
from ajedrez import *
from piezas_ajedrez import mover, color_del_oponente
from manejo_partidas import*

tablero_inicio = crear_tablero()
tablero = tablero_inicio.copy()
jugador = BLANCO

cargar_juego = elegir_partida()

if cargar_juego == True:
    partida = cargar_partida()
    jugador, tablero = partida

print_tablero(tablero)

while True:
    
    print("turno de jugador",jugador)
    posicion1 = input("Posicion de la pieza a mover(columna/fila): ")
    posicion1 = convertir_de_frontend(posicion1)
    if posicion1 == None:
        continue
    
    check_1 =  chequear_movimiento_1(tablero,posicion1,jugador)
    if not check_1[0]:     
        print(check_1[1]) # mensaje de error
        continue

    posicion2 = input("Posicion de destino de la pieza(columna/fila/): ")
    posicion2 = convertir_de_frontend(posicion2)
    if posicion2 == None:
        continue
    check_2 = chequear_movimiento_2(tablero,posicion1,posicion2,jugador, check_1)
    if check_2[0]:
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
        print (check_1[1])  # mensaje de error          
    
    guardar_partida(jugador,tablero)        

    





