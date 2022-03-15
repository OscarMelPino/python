from sqlite3 import apilevel
from flask import Flask, jsonify, request
import json, os, shutil
import main as app
from main import DataB
import webbrowser
from main import GetSchoolNameFromManager, GetManagerData
from manager import Manager
from main import *

application = Flask(__name__)

manager = None

@application.route('/')
def Index():
    return 'Bienvenidos a SchoolerzZ'

@application.route('/login', methods=['POST'])
def Login():
    global manager
    user = request.form['username']
    pwd = request.form['password']
    tipe = request.form['usertype']
    resp = app.Log(DataB(), tipe, user, pwd)
    if resp == 0:
        manager = GetManagerData(tipe + user, DataB())
        webbrowser.open('file:///C:/Users/oscar/Desktop/python/manager_actions.html', 0, False)
        return '', 200
    if resp != 0:
        return 'Forbidden access', 403

# MANAGER
@application.route('/manager', methods=['GET'])
def GetManagers():
    return GetAllManagers()

@application.route('/manager/<int:id>', methods=['GET'])
def GetManagerById(id):
    manager = GetManagerB()
    return manager

@application.route('/manager', methods=['POST'])
def CreateManager():
    # funcion que coge datos y devuelve resultado
    return True

@application.route('/manager/<int:id>', methods=['PUT'])
def ModifyManager(id):
    # cosas
    return True

@application.route('/manager/<int:id>', methods=['DELETE'])
def DeleteManager(id):
    # cosas
    return True
# END MANAGER

# PARENTS
@application.route('/parents', methods=['GET'])
def GetParents():
    return jsonify(GetAllParents(DataB(), 'Joyfe')), 200

@application.route('/parents/<int:id>', methods=['GET'])
def GetParentsById(id):
    return parent

@application.route('/parents', methods=['POST'])
def CreateParent():
    # funcion que coge datos y devuelve resultado
    return True

@application.route('/parents/<int:id>', methods=['PUT'])
def ModifyParent(id):
    # cosas
    return True

@application.route('/parents/<int:id>', methods=['DELETE'])
def DeleteParent(id):
    # cosas
    return True

# END PARENT


# STUDENTS
@application.route('/students', methods=['GET'])
def GetStudents():
    return jsonify(GetAllStudents(DataB()))

@application.route('/students/<int:id>', methods=['GET'])
def GetStudentById(id):
    return student

@application.route('/students', methods=['POST'])
def CreateStudent():
    # funcion que coge datos y devuelve resultado
    return True

@application.route('/students/<int:id>', methods=['PUT'])
def ModifyStudent(id):
    # cosas
    return True

@application.route('/students/<int:id>', methods=['DELETE'])
def DeleteStudent(id):
    # cosas
    return True

# END STUDENTS

if __name__ == '__main__':
    application.run(debug=False)