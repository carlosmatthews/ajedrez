import os
import json
from ajedrez import crear_tablero, BLANCO, partida, Partida


def elegir_partida():
    global partida

    if not hay_archivo_partida():
        partida.juego_nuevo()
        return

    while True:
        inicio = int(input("ingrese 1 para continuar una partida o 0 para nueva partida: "))
        if inicio == 0:
            partida.juego_nuevo()
            break
        if inicio == 1:
            cargar_partida() #cambio llamada a cargar partida..objeto
            break


def hay_archivo_partida():
    return os.path.exists("partida.json")


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

#borrar despues de que funciona metodo cargar partido en Objeto partida
def cargar_partida():
    with open("partida.json") as fichero:
        line = fichero.readline()
    #recive objeto p y modifica objeto partida sin return....    
    p = deserializar_partida(line)
    partida.tablero = p.tablero
    partida.jugador = p.jugador
    partida.continua_juego = p.continua_juego
    partida.ganador = p.ganador


def leer_carpeta_de_guardados():
    
    with os.scandir("c:/Users/carlos/workspace/ajedrez") as ficheros:
        ficheros = [fichero.name for fichero in ficheros if fichero.is_file() and fichero.name.endswith('.json')]
    print(ficheros)
