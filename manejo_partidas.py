import os
import json
from ajedrez import crear_tablero, BLANCO, partida, Partida


def elegir_partida():
    global partida
    leer_archivo = False
    if os._exists("partida.json"):
        while True:
            inicio = int(input("ingrese 1 para continuar una partida o 0 para nueva partida: "))
            if inicio == 0:
                break
            if inicio == 1:
                leer_archivo = True
                break
    if leer_archivo:
        partida = cargar_partida()
    else:
        partida.juego_nuevo()




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


def serializar_partida(partida):
    tablero_serializado = serializar_tablero(partida.tablero)
    data = {
        "jugador": partida.jugador,
        "tablero": tablero_serializado,
        "continua_juego": partida.continua_juego,
        "ganador": partida.ganador
    }
    return json.dumps(data)


def deserializar_partida(partida_serializada):
    data = json.loads(partida_serializada)
    tablero = deserializar_tablero(data["tablero"])
    p = Partida()
    p.tablero = tablero
    p.jugador = data["jugador"]
    p.continua_juego = data["continua_juego"]
    p.ganador = data["ganador"]
    return p


def guardar_partida(partida):
    cadena = serializar_partida(partida)
    fichero = open("partida.json", "w")
    fichero.write(cadena)
    fichero.close()
    return cadena


def cargar_partida():
    with open("partida.json") as fichero:
        line = fichero.readline()
    return deserializar_partida(line)


def leer_carpeta_de_guardados():
    
    with os.scandir("c:/Users/carlos/workspace/ajedrez") as ficheros:
        ficheros = [fichero.name for fichero in ficheros if fichero.is_file() and fichero.name.endswith('.json')]
    print(ficheros)
