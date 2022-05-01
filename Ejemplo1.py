

import json
from flask import  Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET'])

def hello():
    return 'Hello world'



ListaVehiculos = []

class Vehiculos:
    id = 0
    tipo = ""
    marca = ""

@app.route('/', methods=['POST'])
def hello_post():
    body = request.getJson()
    nombre = body['Nombre']
    contrasena = body['Contrasena']
    return 'hello {} {}'.format(nombre, contrasena)

@app.route('/vehiculos', methods=['POST'])
def crearVehiculo():
    
    body = request.get_json()
    id = body['id']
    tipo = body['tipo']
    nombre = body['nombre']
    
    for vehiculo in ListaVehiculos:
            if vehiculo.id == id:
                return{'msg': 'Esa vaina ya existe'}, 400


    vehiculo = Vehiculos
    vehiculo.id = id
    vehiculo.tipo = tipo 
    vehiculo.marca = nombre
    ListaVehiculos.append(vehiculo) 
    return {'msg': 'Vehiculo creado'}, 201

@app.route('/vehiculos', methods=['GET'])
def obtenerVehiculo():
    ListaJson = []
    for vehiculo in ListaVehiculos:
        ListaJson.append({'id': vehiculo.id, 'tipo': vehiculo.tipo,'marca': vehiculo.marca})
    return jsonify(ListaJson), 200

@app.route('/vehiculos/<id>', methods=['PUT'])
def vehiculos_actualizar(id):
    body = request.get_json()
    idint = int(id)
    tipo = body['tipo']
    nombre = body['nombre']
    for vehiculo in ListaVehiculos:
        if vehiculo.id == idint:
            vehiculo.nombre = nombre
            vehiculo.tipo = tipo
            return{'msg': 'Vehiculo modificado'}, 200
    return {'msg':'Vehiculo no registrado'}, 400

if __name__ == '__main__':
    app.run(debug = True, port = 5000)