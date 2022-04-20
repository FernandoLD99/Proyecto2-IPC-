
from flask import Flask, request
import json

Usuario = []


app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return "Hello World!"

@app.route("/usuarios", methods=['POST'])
def crearUsuario():
    body = request.get_json()
    if body is None:
        return json.dumps({"status":400, "msg":"solicittud incorrecta"})
    for i in range(len(Usuario)):
        if Usuario[i]['id_user'] == body['id_user']:
            return json.dumps({"status":400, "msg":"Este usuario ya esta resgistrado"})
    if body ['id_user'] != None and body ['user_display_name']!= None \
    and body['user_nickname']!= None \
    and body['user_password']!= None:
        Usuario.append({
            'id_user': body['id_user'],
            'user_display_name': body['user_display_name'],
            'user_nickname': body['user_nickname'],
            'user_password': body['user_password'],
            'user_age': body['user_age'],
            'user_career': body['user_career'],
            'user_carnet': body['user_carnet']
        })
        return json.dumps({"status": 201, "msg":"usuario registrado"})
    return json.dumps({"status": 400, "msg":"Solicitud incorrecta"})
