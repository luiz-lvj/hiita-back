from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import re
import psycopg2
from flask_cors import CORS
import os

app = Flask(__name__)
app.config['DEBUG'] = True

# Enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# Change this to your secret key (can be anything, it's for extra protection)
# app.secret_key = 'your secret key'

# Enter your database connection details below
def get_db_connection():
    conn = psycopg2.connect(host=os.environ['DB_HOST'],
                            database=os.environ['DB_NAME'],
                            user=os.environ['DB_USER'],
                            password=os.environ['DB_PASSWORD'])
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM username;')
    users = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify({'users': users})

# http://localhost:5000/HIITA/ok
@app.route('/HIITA/ping', methods=['GET', 'POST'])
def ping():
    msg = 'pong'
    
    return jsonify({'message': msg})

@app.route('/HIITA/backend_ping', methods=['GET', 'POST'])
def backend_ping():
    msg = 'pong'

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""SELECT *
                FROM pg_catalog.pg_tables
                WHERE schemaname != 'pg_catalog' AND 
                schemaname != 'information_schema';""")
    tables = cur.fetchall()
    cur.close()
    conn.close()
    
    return jsonify({'message': msg, 'tables': tables})

# http://localhost:5000/python/logout - this will be the logout page
@app.route('/HIITA/logout', methods=['GET', 'POST'])
def logout():

    data = request.get_json()
    error = True
    msg = ''
    if request.method == 'POST' and 'token' in data:
        error, msg = logout_call(data.token)
    else:
        msg = 'Request Method or token not informed'

    # Redirect to login page
    return jsonify({'error': error, 'message': msg})

def logout_call(token):
    error = True
    msg = 'Token Not Found'
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT token FROM SESSION WHERE TOKEN = %s', (token))
    token_verification = cur.fetchone()
    if token_verification:
        cur.execute('DELETE FROM SESSION WHERE TOKEN = %s', (token))
        conn.commit()
        msg = 'ACK'
        error = False

    cur.close()
    conn.close()
    return error, msg

# http://localhost:5000/pythonlogin/ - the following will be our login page, which will use both GET and POST requests
@app.route('/HIITA/login', methods=['GET', 'POST'])
def login():
    # Output message if something goes wrong...
    msg = ''
    data = request.get_json()
    print(data)
    error = True
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in data and 'password' in data:
        # Create variables for easy access
        username = data['username']
        password = data['password']
        # Check if account exists using MySQL
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT ID FROM USERNAME WHERE CPF = %s AND SENHA = %s', (username, password,))
        # Fetch one record and return result
        account = cur.fetchone()
        print(account)
        # If account exists in accounts table in out database
        if account:
            # Create session data, we can access this data in other routes
            cur.execute('INSERT INTO SESSION VALUES (DEFAULT, DEFAULT, DEFAULT, %s) RETURNING TOKEN', (account,))
            token = cur.fetchone()
            conn.commit()
            cur.close()
            conn.close()
            error = False
            # Redirect to home page
            return jsonify({'message': msg, 'error': error, 'token': token})
        else:
            cur.close()
            conn.close()
            # Account doesnt exist or username/password incorrect
            msg = 'CPF/Senha Incorreto(s)!'
    # Show the login form with message (if any)
    return jsonify({'message': msg, 'error': error})

# http://localhost:5000/pythinlogin/register - this will be the registration page, we need to use both GET and POST requests
@app.route('/HIITA/register', methods=['GET', 'POST'])
def register():
    # Output message if something goes wrong...
    msg = ''
    data = request.get_json()
    error = True
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in data and 'password' in data and 'email' in data and 'name' in data:
        # Create variables for easy access
        username = data['username']
        password = data['password']
        email = data['email']
        name = data['name']
        # Check if account exists using MySQL
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM USERNAME WHERE CPF = %s', (username,))
        account = cur.fetchone()
        # If account exists show error and validation checks
        if account:
            msg = 'Já existe conta com este CPF!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Endereço de email inválido!'
        elif not re.match(r'[0-9]+', username):
            msg = 'CPF deve conter apenas números'
        elif not username or not password or not email:
            msg = 'Por favor termine o preenchimento!'
        else:
            # Account doesnt exists and the form data is valid, now insert new account into accounts table
            cur.execute('INSERT INTO USERNAME VALUES (DEFAULT, %s, %s, %s, %s)', 
                            (username, name, email, password,))
            conn.commit()
            cur.close()
            conn.close()
            msg = 'Registro com sucesso!'
            error = False
    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Por favor preencha o formulário!'
    # Show registration form with message (if any)
    return jsonify({'message': msg, 'error': error})

# http://localhost:5000/pythinlogin/home - this will be the home page, only accessible for loggedin users
@app.route('/HIITA/loggedin', methods=['GET', 'POST'])
def loggedin():
    ### O ideal é verificar se o token ainda é valido
    data = request.get_json()
    # Check if user is loggedin
    if request.method == 'POST' and 'token' in data:
        user_id = check_login(data['token'])
        if user_id == 0:
            return jsonify({'loggedin': False})
        else:
            return jsonify({'loggedin': True})

def check_login(token):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT USER_ID FROM SESSION WHERE TOKEN = %s', (token,))
    user_id = cur.fetchone()
    cur.close()
    conn.close()
    if user_id:
        return user_id
    else:
        return 0

# http://localhost:5000/pythinlogin/ficha - this will be the train page, only accessible for loggedin users
@app.route('/HIITA/fichas', methods=['GET','POST'])
def fichas():
    # Check if user is loggedin
    data = request.get_json()
    # Check if user is loggedin
    if request.method == 'POST' and 'token' in data:
        user_id = check_login(data['token'])
        if user_id:
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute('SELECT ID, TITULO, DESCRICAO FROM FICHA WHERE USERNAME_ID = %s', (user_id,))
            training_sheets = cur.fetchall()
            cur.close()
            conn.close()
            return jsonify({'fichas': training_sheets})
    return jsonify({'fichas': {}})

# http://localhost:5000/pythinlogin/treino - this will be the train page, only accessible for loggedin users
@app.route('/HIITA/treino', methods=['POST'])
def treino():
    # Check if user is loggedin
    data = request.get_json()
    # Check if user is loggedin
    if request.method == 'POST' and 'token' in data:
        user_id = check_login(data['token'])
        if user_id:
            conn = get_db_connection()
            cur = conn.cursor()
            ## O IDEAL SERIA CHECAR SE A FICHA PERTENCE A QUEM PEDIU
            cur.execute('SELECT ID, NOME_EXERCICIO, DESCRICAO FROM EXERCICIO WHERE FICHA_ID = %s', (data['trainID'],))
            exercises = cur.fetchall()
            cur.close()
            conn.close()
            return jsonify({'exercises': exercises})
    # User is not loggedin redirect to login page
    return jsonify({'exercises': {}})

@app.route('/HIITA/realizados', methods=['GET','POST'])
def realizados():
    
    performed_final = []
    data = request.get_json()
    # Check if user is loggedin
    if request.method == 'POST' and 'token' in data:
        user_id = check_login(data['token'])
        if user_id:
            conn = get_db_connection()
            cur = conn.cursor()
            ## O IDEAL SERIA CHECAR SE A FICHA PERTENCE A QUEM PEDIU
            cur.execute('SELECT TREINO.DATAHORA AS DATAHORA, FICHA.TITULO AS TITULO FROM TREINO '
                        'INNER JOIN FICHA ON TREINO.FICHA_ID = FICHA.ID '+
                        'WHERE FICHA.USERNAME_ID = %s', (user_id,))
            performed = cur.fetchall()
            print(performed)
            cur.close()
            conn.close()
            for p in performed:
                print(p)
                temp = {}
                temp['TITULO'] = p[1]
                temp['DATA'] = p[0].date()
                temp['HORA'] = str(p[0].time())
                performed_final.append(temp)
            return jsonify({'realizeds': performed_final})
    return jsonify({'realized': {}})

@app.route('/HIITA/salvar', methods=['POST'])
def save():
    # Check if user is loggedin
    data = request.get_json()
    # Check if user is loggedin
    if request.method == 'POST' and 'token' in data:
        user_id = check_login(data['token'])
        if user_id:
            conn = get_db_connection()
            cur = conn.cursor()
            ## O IDEAL SERIA CHECAR SE A FICHA PERTENCE A QUEM PEDIU
            cur.execute('INSERT INTO TREINO VALUES (DEFAULT, %s, %s, DEFAULT)', 
                        (user_id, data['trainID'],))
            conn.commit()
            cur.close()
            conn.close()
            return jsonify({'error': False})
    # User is not loggedin redirect to login page
    return jsonify({'error': True})