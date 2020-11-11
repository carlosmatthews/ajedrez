import os
import json


def elegir_partida():
    if os._exists("partida.json"):
        while True:
            inicio = int(input("ingrese 1 para continuar una partida o 0 para nueva partida: "))       

            if inicio == 0:
                return False
            if inicio == 1:
                return True
            else:
                continue

def serializar_tablero(tablero):
    tablero_serializado = []
    for (fila,col), (pieza, color) in tablero.items():
        tablero_serializado.append([fila, col, pieza, color])
    return tablero_serializado

def deserializar_tablero(tablero_serializado):
    tablero = {}
    for e in tablero_serializado:
        tablero[(e[0],e[1])]= (e[2],e[3])
    return tablero    


def guardar_partida(jugador, tablero):
    tablero_guardar = serializar_tablero(tablero)   
    data = {"turno":jugador,"tablero":tablero_guardar}
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
        
    tablero = deserializar_tablero(tablero_guardardo)
    return (jugador,tablero)


def leer_carpeta_de_guardados():
    
    with os.scandir("c:/Users/carlos/workspace/ajedrez") as ficheros:
        ficheros = [fichero.name for fichero in ficheros if fichero.is_file() and fichero.name.endswith('.json')]
    print(ficheros)
