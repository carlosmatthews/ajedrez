import json

def elejir_partida():
    while True:
        inicio = int(input("ingrese 1 para continuar una partida o 0 para nueva partida: "))       

        if inicio == 0:
            return False
        if inicio == 1:
            return True
        else:
            continue

def guardar_partida(jugador, tablero):
    tablero_guardar = {}
    for clave,valor in tablero.items():
        string_clave = (str(clave[0]),str(clave[1]))
        string_clave = ",".join(string_clave)
        tablero_guardar[string_clave] = valor

    data = {"turno":jugador,"partida":tablero_guardar}
    cadena = json.dumps(data)
    fichero = open("partida.json","w")
    fichero.write(cadena)
    fichero.close()

def cargar_partida():
        
    fichero = open("partida.json")
    line = fichero.readline()
    fichero.close()
    data = json.loads(line)
    tablero_guardardo = data["partida"]
    jugador = data["turno"]
    
    tablero = {}
    
    for clave,valor in tablero_guardardo.items():
        clave_list = clave.split(",")
        clave_list = (int(clave[0]),int(clave_list[1]))
        tablero[clave_list] = tuple(valor)    

    return (jugador,tablero)



