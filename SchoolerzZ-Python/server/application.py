from multiprocessing.dummy import Manager
from flask import Flask, jsonify, request
import json, os, shutil
import database_connection

application = Flask(__name__)

path_base = os.path.dirname(os.path.abspath(__file__))

TOKEN_KEY = 'SchoolerzZ-Client'


@application.route('/')
def root():
    return 'BIENVENIDO A SCHOOLERZZ'

@application.route('/login', methods=['POST'])
def main_login():
    user = request.form['username']
    pwd = request.form['password']

    return f'Usuario: {user} | Contraseña: {pwd}'


@application.route('/managers',methods=['GET'])
def GetManagers():
    manager_list = []
    query = 'SELECT * FROM sz_002_students;'
    rows = database_connection.SchoolerzDatabase.ExecuteQuery(database_connection.SchoolerzDatabase, query)
    for item in rows:
        manager_list.append(str(item))
    manager_list.pop(0)
    manager_list.pop(3)
    manager_list.pop(13)
    manager_list.pop()
    manager_list = json.dumps(manager_list)
    return manager_list

if __name__ == '__main__':
    application.run(debug=False)