#!/usr/bin/env python3
# Este server se ejecuta haciendo: python server.py
# Y despues lo accedes en el navegador en esta direccion: http://localhost:8000/

import json
from flask import Flask
from flask import request
from manejo_partidas import serializar_tablero,guardar_partida, serializar_partida
from ajedrez import partida, crear_tablero, chequear_movimiento_1,chequear_movimiento_2,\
jaque_mate

import piezas_ajedrez

app = Flask(__name__, static_url_path="/frontend")


@app.route("/reiniciar")
def reiniciar():
    partida.juego_nuevo()
    partida_serializada = guardar_partida(partida)
    return partida_serializada



#/movimientos?fila=0&col=1
@app.route("/movimientos")     
def movimientos():
    fila = int(request.args.get("fila"))
    col = int(request.args.get("col"))
    puede_mover, mensaje, mov_posibles = chequear_movimiento_1(partida.tablero, (fila, col), partida.jugador)
    if puede_mover:
        return json.dumps({'mov_posibles': mov_posibles})
    else:
        return json.dumps({'error': mensaje})


@app.route('/partida')
def enviar_partida():
    return serializar_partida(partida)


#parametros  #?fila=0,col=0&fila2=5,col2=4')
@app.route("/mover")        
def mover():
    fila  = int(request.args.get("fila"))
    col   = int(request.args.get ("col"))
    fila2 = int(request.args.get("fila2"))
    col2  = int(request.args.get("col2"))
    piezas_ajedrez.mover(partida.tablero,(fila,col),(fila2,col2))
    
    #esto va dentro de la fun mover original
    partida.continua_juego = not jaque_mate(partida.tablero, partida.jugador)
    if not partida.continua_juego:
        partida.ganador = piezas_ajedrez.color_del_oponente(partida.jugador)
    else:
        partida.ganador = None
    partida.cambio_turno() # esto va en mover
    partida_serializada = guardar_partida(partida)
    return partida_serializada

    

    
@app.route('/')
def main():
    return "ajedrez server"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)

