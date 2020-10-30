#!/usr/bin/env python3

# Este server se ejecuta haciendo: python server.py
# Y despues lo accedes en el navegador en esta direccion: http://localhost:8000/

import json
from flask import Flask

app = Flask(__name__, static_url_path="/frontend")

@app.route('/')
def index():
    return 'Hello'


@app.route('/carli')
def carli():
    return 'Hello carli'

@app.route('/marto')
def marto():
    return 'Hello marto'

@app.route('/dicc')
def dicc():
    diccionario = {}
    diccionario["cero"]= 0
    diccionario["uno"] = 1
    diccionario["dos"] = 2

    return json.dumps(diccionario)    
    
    


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
