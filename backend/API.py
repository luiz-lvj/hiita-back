from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
from flask_cors import CORS

app = Flask(__name__)
app.config['DEBUG'] = True

# Enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# Opened connexions
frontend_connexion = {}

# Change this to your secret key (can be anything, it's for extra protection)
app.secret_key = 'your secret key'

# Enter your database connection details below
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'hiita'
app.config['MYSQL_PASSWORD'] = 'hiita'
app.config['MYSQL_DB'] = 'hiita'

# Intialize MySQL
mysql = MySQL(app)

# http://localhost:5000/HIITA/ok - this will be the logout page
@app.route('/HIITA/ping', methods=['GET', 'POST'])
def ping():
    msg = 'pong'
    
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM USERNAME WHERE CPF = %s AND SENHA = %s', (username, password,))
    # Fetch one record and return result
    account = cursor.fetchone()
    print(account)
    return jsonify({'message': msg})

@app.route('/HIITA/backend_ping', methods=['GET', 'POST'])
def backend_ping():
    msg = 'pong'
    
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SHOW TABLES')
    # Fetch one record and return result
    tables = cursor.fetchall()
    return jsonify({'message': msg, 'tables': tables})

# http://localhost:5000/python/logout - this will be the logout page
@app.route('/HIITA/logout')
def logout():
    # Remove session data, this will log the user out
   frontend_connexion.pop('loggedin')
   frontend_connexion.pop('id', None)
   frontend_connexion.pop('username', None)
   # Redirect to login page
   return jsonify({'error': False})

# http://localhost:5000/pythonlogin/ - the following will be our login page, which will use both GET and POST requests
@app.route('/HIITA/login', methods=['GET', 'POST'])
def login():
    # Output message if something goes wrong...
    msg = ''
    data = request.get_json()
    error = True
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in data and 'password' in data:
        # Create variables for easy access
        username = data['username']
        password = data['password']
        # Check if account exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM USERNAME WHERE CPF = %s AND SENHA = %s', (username, password,))
        # Fetch one record and return result
        account = cursor.fetchone()
        print(account)
        # If account exists in accounts table in out database
        if account:
            # Create session data, we can access this data in other routes
            frontend_connexion['loggedin'] = True
            frontend_connexion['ID'] = account['ID']
            frontend_connexion['username'] = account['CPF']
            error = False
            # Redirect to home page
            return jsonify({'message': msg, 'error': error})
        else:
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
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM USERNAME WHERE CPF = %s', (username,))
        account = cursor.fetchone()
        # If account exists show error and validation checks
        if account:
            existingData = account
            msg = 'Já existe conta com este CPF!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Endereço de email inválido!'
        elif not re.match(r'[0-9]+', username):
            msg = 'CPF deve conter apenas números'
        elif not username or not password or not email:
            msg = 'Por favor termine o preenchimento!'
        else:
            # Account doesnt exists and the form data is valid, now insert new account into accounts table
            cursor.execute('INSERT INTO USERNAME (`ID`,`CPF`,`NOME`,`EMAIL`,`SENHA`) VALUES (NULL, %s, %s, %s, %s)', 
                            (username, name, email, password,))
            mysql.connection.commit()
            msg = 'Registro com sucesso!'
            error = False
    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Por favor preencha o formulário!'
    # Show registration form with message (if any)
    return jsonify({'message': msg, 'error': error})

# http://localhost:5000/pythinlogin/home - this will be the home page, only accessible for loggedin users
@app.route('/HIITA/loggedin', methods=['GET'])
def loggedin():
    # Check if user is loggedin
    if 'loggedin' in frontend_connexion:
        # User is loggedin show them the home page
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM USERNAME WHERE CPF = %s', (frontend_connexion['username'],))
        account = cursor.fetchone()
        return jsonify({'loggedin': True, 'username': frontend_connexion['username'], 'account': account})
    if 'loggedin' in frontend_connexion:
        return jsonify({'loggedin': True, 'username': 'OK para gambiarra'}  )
    # User is not loggedin redirect to login page
    return jsonify({'loggedin': False, 'username': ''})

# http://localhost:5000/pythinlogin/ficha - this will be the train page, only accessible for loggedin users
@app.route('/HIITA/fichas', methods=['GET'])
def fichas():
    # Check if user is loggedin
    if 'loggedin' in frontend_connexion:
        # We need all the account info for the user so we can display it on the ficha page
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT ID, TITULO, DESCRICAO FROM FICHA WHERE USERNAME_ID = %s', (frontend_connexion['ID'],))
        training_sheets = cursor.fetchall()

        # Show the profile page with account info
        return jsonify({'fichas': training_sheets})
    # User is not loggedin redirect to login page
    return jsonify({'fichas': {}})

# http://localhost:5000/pythinlogin/treino - this will be the train page, only accessible for loggedin users
@app.route('/HIITA/treino', methods=['POST'])
def treino():
    # Check if user is loggedin
    data = request.get_json()
    if 'loggedin' in frontend_connexion:
        # We need all the account info for the user so we can display it on the profile page
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT ID, NOME_EXERCICIO, DESCRICAO FROM EXERCICIO WHERE FICHA_ID = %s', (data['trainID'],))
        exercises = cursor.fetchall()
        # Show the profile page with account info
        return jsonify({'exercises': exercises})
    # User is not loggedin redirect to login page
    return jsonify({'exercises': {}})

@app.route('/HIITA/realizados')
def realizados():
    # Check if user is loggedin
    performed_final = []
    if 'loggedin' in frontend_connexion:
        # We need all the account info for the user so we can display it on the profile page
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT TREINO.DATAHORA AS DATAHORA, FICHA.TITULO AS TITULO FROM TREINO '
                        'INNER JOIN FICHA ON TREINO.FICHA_ID = FICHA.ID '+
                        'WHERE FICHA.USERNAME_ID = %s', (frontend_connexion['ID'],))
        performed = cursor.fetchall()
        print(type(performed))
        print(performed)
        for p in performed:
            temp = {}
            temp['TITULO'] = p['TITULO']
            temp['DATA'] = p['DATAHORA'].date()
            temp['HORA'] = str(p['DATAHORA'].time())
            performed_final.append(temp)
        # Show the profile page with account info
        return jsonify({'realizeds': performed_final})
    # User is not loggedin redirect to login page
    return jsonify({'realized': {}})

@app.route('/HIITA/salvar', methods=['POST'])
def save():
    # Check if user is loggedin
    data = request.get_json()
    if 'loggedin' in frontend_connexion:
        # We need all the account info for the user so we can display it on the profile page
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        print(frontend_connexion['ID'])
        print(data['trainID'])
        cursor.execute('INSERT INTO TREINO (`ID`,`USERNAME_ID`,`FICHA_ID`,`DATAHORA`) VALUES (NULL, %s, %s, NOW())', 
                        (int(frontend_connexion['ID']), int(data['trainID']),))
        mysql.connection.commit()
        # Show the profile page with account info
        return jsonify({'error': False})
    # User is not loggedin redirect to login page
    return jsonify({'error': True})