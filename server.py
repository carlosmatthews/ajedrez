#!/usr/bin/env python3
# Este server se ejecuta haciendo: python server.py
# Y despues lo accedes en el navegador en esta direccion: http://localhost:8000/

import json
from flask import Flask
from flask import request
from manejo_partidas import serializar_tablero,guardar_partida, serializar_partida
from ajedrez import partida, crear_tablero, chequear_movimiento_1,chequear_movimiento_2, jaque_mate

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
    posicion = int(request.args.get("fila")), int(request.args.get("col"))
    puede_mover, mensaje, mov_posibles = chequear_movimiento_1(partida.tablero, posicion, partida.jugador)
    if not puede_mover:
        return json.dumps({'error': mensaje})
    return json.dumps({'mov_posibles': mov_posibles})


@app.route('/partida')
def enviar_partida():
    return serializar_partida(partida)


#parametros  #?fila=0,col=0&fila2=5,col2=4')
@app.route("/mover")        
def mover():
    posicion1 = int(request.args.get("fila")), int(request.args.get ("col"))
    posicion2 = int(request.args.get("fila2")), int(request.args.get("col2"))

    puede_mover, mensaje, mov_posibles = chequear_movimiento_1(partida.tablero, posicion1, partida.jugador)
    if not puede_mover:
        return json.dumps({'error': mensaje})

    puede_mover, mensaje = chequear_movimiento_2(partida.tablero, posicion1, posicion2, mov_posibles)
    if not puede_mover:
        return json.dumps({'error': mensaje})

    partida.mover(posicion1, posicion2)
    partida_serializada = guardar_partida(partida)
    return partida_serializada
    
@app.route('/')
def main():
    return "ajedrez server"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)

