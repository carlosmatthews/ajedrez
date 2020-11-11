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
    tablero_serializado = {}
    # serializa diccionario para json, la clave deve ser string
    for (fila,columna), valor in tablero.items():
        string_clave = f"{fila},{columna}"
        tablero_serializado[string_clave] = valor
    return tablero_serializado



def deserializar_tablero(tablero_serailizado):
    
    tablero = {}
    
    for clave,valor in tablero_serailizado.items():
        clave_tupla = int(clave[1]),int(clave[4])
        tablero[clave_tupla] = tuple(valor)
        
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



