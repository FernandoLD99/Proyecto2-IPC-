
import datetime
from flask import Flask, request
import json

Usuario = []
Books = []
Prestamos = []

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    hola = "Hello world1"
    return hola

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

@app.route('/usuarios', methods=['GET'])
def verUsuarios():
    U = Usuario
    return json.dumps(U)

@app.route('/login', methods=['POST'])
def login():
    body = request.get_json()
    for i in range (len(Usuario)):
        if Usuario[i]['user_nickname']==body['user_nickname']:
            if Usuario[i]['user_password']==body['user_password']:
                return json.dumps({"status":200, "msg": Usuario[i]['id_user']})
    return json.dumps({"status":400, "msg": "credenciales incorrectas"})            

#{
#   "id_book": 1
#   "book_title": "name_book"
#   "book_type": "libro"
#   "author": "nombre"
#   
#
#
#
#}
@app.route('/book', methods=['POST'])
def crearLibro():
    body = request.get_json()
    if body is None:
        return json.dumps({"status":400, "msg":"solicittud incorrecta"})
    for i in range(len(Books)):
        if Books[i]['id_book'] == body['id_book']:
            return json.dumps({"status":400, "msg":"Este libro ya esta resgistrado"})
    if body ['id_book'] != None and body ['book_title']!= None \
    and body['author']!= None \
    and body['book_count']!= None \
    and body['book_aviable']!= None \
    and body['book_year']!= None \
    and body['book_editorial']!= None:
        Books.append({
            'id_book': body['id_book'],
            'book_title': body['book_title'],
            'author': body['author'],
            'book_count': body['book_count'],
            'book_aviable': body['book_aviable'],
            'book_year': body['book_year'],
            'book_editorial': body['book_editorial']
        })
        return json.dumps({"status": 201, "msg":"Libro registrado"})
    return json.dumps({"status": 400, "msg":"Solicitud incorrecta"})

@app.route('/book/<int:id>', methods=['POST'])
def actualizarLibro(id):
    body = request.get_json()
    for i in range (len(Books)):
        if Books[i]['id_book']==id: 
            if body ['book_title']!= None\
            and body['author']!= None \
            and body['book_count']!= None \
            and body['book_aviable']!= None \
            and body['book_year']!= None \
            and body['book_editorial']!= None:
                Books[i].Delete()
                Books.append({
                'id_book': body['id_book'],
                'book_title': body['book_title'],
                'author': body['author'],
                'book_count': body['book_count'],
                'book_aviable': body['book_aviable'],
                'book_year': body['book_year'],
                'book_editorial': body['book_editorial']
        })
                
            return json.dumps({"status":200, "msg": "Libro actualizado con exito", 'Libro': Books[i]})  
                
            return json.dumps({"status":400, "msg": "Faltan datos para actualizar el libro"})
                        

        
    return json.dumps({"status":400, "msg": "No se encontro el libro"})


@app.route('/book', methods=['GET'])
def verLibro():
    body = request.get_json()
    if body is None:
        return json.dumps({"status":400, "msg":"solicitud incorrecta"})
    if body['id_book'] !=None:
        for i in range(len(Books)):
          if Books[i]['id_book'] == body['id_book']:
            return json.dumps(Books[i])
        return json.dumps({"status":400, "msg":"id no encontrada"})

    return json.dumps({"status":400, "msg": "No se encontro el libro"})

@app.route('/loan', methods = ['POST'])
def registrarPrestamo():
    body = request.get_json()
    libroExiste = False
    for i in range(len(Books)):
         if Books[i]['id_book'] == body['id_book']:
            Libro = Books[i]
            break
    if Libro == None:
        return json.dumps({"status": 400, "msg": "Libro no existe"})
    User = None
    for i in range(len(Usuario)):
        if Usuario[i]['id_user'] == body['id_user']:
            User = Usuario[i]
            break
    if User == None:
        return json.dumps({"status": 401, "msg": "No autorizado"})
    id = len(Prestamos) + 1
    now = datetime.date.today()
    Prestamos.append({
        "id_loan": id,
        "id_usuario": body['id_user'],
        "id_book": body['id_book'],
        "date_inital": now
    })
    return json.dumps({"status": 200, "msg": "Prestamos realizado"}) 

@app.route('/loan/penalty', methods = ['GET'])
def calcularMulta():
    body = request.get_json()
    for i in range(len(Prestamos)):
          if Prestamos[i]['id_loan'] == body['id_loan'] :
            return json.dumps(Prestamos[i])
    return json.dumps({"status":400, "msg":"id del prestamo incorrecta"})



def diasHastaFecha(day1, month1, year1, day2, month2, year2):
    
    # Función para calcular si un año es bisiesto o no
    
    def esBisiesto(year):
        return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
    
    # Caso de años diferentes
    
    if (year1<year2):
        
        # Días restante primer año
        
        if esBisiesto(year1) == False:
            diasMes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        else:
            diasMes = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
     
        restoMes = diasMes[month1] - day1
    
        restoYear = 0
        i = month1 + 1
    
        while i <= 12:
            restoYear = restoYear + diasMes[i]
            i = i + 1
    
        primerYear = restoMes + restoYear
    
        # Suma de días de los años que hay en medio
    
        sumYear = year1 + 1
        totalDias = 0
    
        while (sumYear<year2):
            if esBisiesto(sumYear) == False:
                totalDias = totalDias + 365
                sumYear = sumYear + 1
            else:
                totalDias = totalDias + 366
                sumYear = sumYear + 1
    
        # Dias año actual
    
        if esBisiesto(year2) == False:
            diasMes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        else:
            diasMes = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
        llevaYear = 0
        lastYear = 0
        i = 1
    
        while i < month2:
            llevaYear = llevaYear + diasMes[i]
            i = i + 1
    
        lastYear = day2 + llevaYear
    
        return totalDias + primerYear + lastYear
    
    # Si estamos en el mismo año
    
    else:
        
        if esBisiesto(year1) == False:
            diasMes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        else:
            diasMes = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
        llevaYear = 0
        total = 0
        i = month1
        
        if i < month2:
            while i < month2:
                llevaYear = llevaYear + diasMes[i]
                i = i + 1
            total = day2 + llevaYear - 1
            return total 
        else:
            total = day2 - day1
            return total