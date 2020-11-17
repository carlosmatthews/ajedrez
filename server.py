#!/usr/bin/env python3
# Este server se ejecuta haciendo: python server.py
# Y despues lo accedes en el navegador en esta direccion: http://localhost:8000/

import json
from flask import Flask
from flask import request
from manejo_partidas import serializar_tablero
from ajedrez import partida, crear_tablero, chequear_movimiento_1,chequear_movimiento_2,jaque_mate,cambio_de_turno
import piezas_ajedrez

app = Flask(__name__, static_url_path="/frontend")

tablero = partida["tablero"]
jugador = partida["turno"]
ganador = None


@app.route("/inicio")
#borrar
def inicio():
    global tablero
    tablero = crear_tablero()
    tablero_serializado = serializar_tablero(tablero)
    return json.dumps(tablero_serializado)



#/movimientos?fila=0&col=1
@app.route("/movimientos")     
def movimientos():
    fila = int(request.args.get("fila"))
    col = int(request.args.get("col"))
    chequeo = chequear_movimiento_1(tablero,(fila,col),jugador)
    if not chequeo:
        return json.dumps(chequeo[1])
    else:
        return json.dumps(chequeo[2])

        

@app.route('/tablero')
def enviar_tablero():
    tablero_serializado = serializar_tablero(tablero)
    tablero_json = json.dumps(tablero_serializado)
    return tablero_json


#parametros  #?fila=0,col=0&fila2=5,col2=4')
@app.route("/mover")        
def mover():
    fila  = int(request.args.get("fila"))
    col   = int(request.args.get ("col"))
    fila2 = int(request.args.get("fila2"))
    col2  = int(request.args.get("col2"))

    piezas_ajedrez.mover(tablero,(fila,col),(fila2,col2))
    #esto va dentro de la fun mover original
    continua_juego = not jaque_mate(tablero,jugador)
    if not continua_juego:
        ganador = piezas_ajedrez.color_del_oponente(jugador)
    else:
        ganador = None    
           
    cambio_de_turno(jugador)
    tablero_serializado = serializar_tablero(tablero)
    dic_partida = {"tablero" : tablero_serializado,"turno":jugador, "continua_juego":continua_juego, "ganador": ganador}
    
    return json.dumps(dic_partida) 

    

    
@app.route('/')
def main():
    return "hola sol"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)

