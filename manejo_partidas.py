import os
import json
from ajedrez import crear_tablero, BLANCO

def elegir_partida():
    if os._exists("partida.json"):
        while True:
            inicio = int(input("ingrese 1 para continuar una partida o 0 para nueva partida: "))       

            if inicio == 0:
                return crear_tablero(), BLANCO
            if inicio == 1:
                return cargar_partida()# tablero, jugador,continua juego, ganador
            else:
                continue
    else:
        return crear_tablero(), BLANCO            




def serializar_tablero(tablero):
    tablero_serializado = []
    for (fila,col), (pieza, color) in tablero.items():
        tablero_serializado.append([fila, col, pieza, color])
    return tablero_serializado

def deserializar_tablero(tablero_serializado):
    tablero = {}
    for fila, col, pieza, color in tablero_serializado:
        tablero[fila,col] = (pieza,color)
    return tablero    


def guardar_partida(jugador, tablero, continua_juego,ganador):
    tablero_guardar = serializar_tablero(tablero)   
    data = {"turno":jugador,"tablero":tablero_guardar, "continua_juego": continua_juego, \
        "ganador": ganador }
    cadena = json.dumps(data)
    fichero = open("partida.json","w")
    fichero.write(cadena)
    fichero.close()


def cargar_partida():
    with open("partida.json") as fichero:
        line = fichero.readline()
        fichero.close()
        data = json.loads(line)
        tablero_guardardo = data["tablero"]
        jugador = data["turno"]
        continua_juego = data["continua_juego"]
        ganador = data["ganador"]
    tablero = deserializar_tablero(tablero_guardardo)
    return (tablero, jugador, continua_juego, ganador)


def leer_carpeta_de_guardados():
    
    with os.scandir("c:/Users/carlos/workspace/ajedrez") as ficheros:
        ficheros = [fichero.name for fichero in ficheros if fichero.is_file() and fichero.name.endswith('.json')]
    print(ficheros)
