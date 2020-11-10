#!/usr/bin/env python3

# Este server se ejecuta haciendo: python server.py
# Y despues lo accedes en el navegador en esta direccion: http://localhost:8000/

import json
from flask import Flask
from flask import request
from manejo_partidas import serializar_tablero
from ajedrez import partida, crear_tablero, chequear_movimiento_1,chequear_movimiento_2, movimientos_posibles
import piezas_ajedrez

app = Flask(__name__, static_url_path="/frontend")

tablero = partida["tablero"]
jugador = partida["turno"]

dic_error = {"error": "error en la ejecucion del movimiento"}


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
    fila = request.args.get("fila")
    col = request.args.get("col")
    if chequear_movimiento_1(tablero,(fila,col),jugador) == False:
        return json.dumps(dic_error)
    else:
        return json.dumps(movimientos_posibles)

        

@app.route('/tablero')
def enviar_tablero():
    tablero_serializado = serializar_tablero(tablero)
    tablero_json = json.dumps(tablero_serializado)
    return tablero_json

#parametros  #?fila=0,col=0&fila2=5,col2=4')
@app.route("/mover")        
def mover():
    fila = request.args.get("fila")
    col = request.args.get ("col")
    fila2 = request.args.get("fila2")
    col2 = request.args.get("col2")

    piezas_ajedrez.mover(tablero,(fila,col),(fila2,col2))
    tablero_serializado = serializar_tablero(tablero)
    dic_tablero = {"tablero" : tablero_serializado}
    return json.dumps(dic_tablero) 

    
      
    
    

    
@app.route('/dicc')
def dicc():
    diccionario = {}
    diccionario["cero"]= 0
    diccionario["uno"] = 1
    diccionario["dos"] = 2

    return json.dumps(diccionario)    
    
    
@app.route('/')
def main():
    return "hola sol"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)

