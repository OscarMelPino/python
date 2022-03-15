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
@application.route('/managers', methods=['GET'])
def GetManagers():
    return GetAllManagers(DataB())

@application.route('/managers/<int:id>', methods=['GET'])
def GetManagerById(id):
    manager = GetManagerById(DataB())
    return manager

@application.route('/managers', methods=['POST'])
def CreateManager():
    # funcion que coge datos y devuelve resultado
    return True

@application.route('/managers/<int:id>', methods=['PUT'])
def ModifyManager(id):
    ModifyManager(DataB(), GetManagerById(id))
    return True

@application.route('/managers/<int:id>', methods=['DELETE'])
def DeleteManager(id):
    # cosas
    return True
# END MANAGER


# PARENTS
@application.route('/parents', methods=['GET'])
def GetParent():
    return jsonify(GetAllParents(DataB(),"Joyfe")), 200

@application.route('/delparents', methods=['GET'])
def DeleteParents():
    MyParentsList = GetAllParents(DataB(), "Joyfe")
    if request.form["idD"] is not None:
        DeleteParent(DataB(), MyParentsList[request.form["idD"]]["sz_003_nick"])
        return True
    return MyParentsList.__len__()

@application.route('/idparents', methods=['GET'])
def GetParents():
    id = str(request.form.get["id"], False)
    if id is not None:
        url = "http://localhost:5000/parentdata/" + id
        webbrowser.open(url, 0, False)
    return jsonify(GetAllParents(DataB(), "Joyfe")), 200

@application.route('/parentdata/<int:id>', methods=['GET'])
def GetParentsById(id):
    MyParentsList = GetAllParents(DataB(),"Joyfe")
    parent = MyParentsList[id]
    return jsonify(parent)

@application.route('/addparent', methods=['POST'])
def CreateParent():
    AddParent(DataB(), request.form["name"], request.form["SN1"], request.form["SN2"], 
              request.form["birth"], request.form["nationality"], request.form["country"], 
              request.form["city"], request.form["postalCode"], request.form["address"], 
              request.form["email"], request.form["phone1"], request.form["phone2"],
              "Joyfe", request.form["sNick"])
    return 201

# END PARENT


# STUDENTS
@application.route('/students/', methods=['GET'])
def GetStudents():
    temp = request.form['id']
    print(temp)
    if temp is None:
        return id()
    return jsonify(GetAllStudents(DataB()))

@application.route('/students/<int:id>', methods=['GET'])
def GetStudentById(id):
    MyStudentsList = GetAllStudents(DataB())
    student = MyStudentsList[id]
    return jsonify(student)

@application.route('/students', methods=['POST'])
def CreateStudent():
    AddStudent(DataB, request.form['name'],request.form['sn1'], request.form['sn2'], request.form['birth'], request.form['nation'], request.form['country'], request.form['postalCode'], request.form['address'], request.form['email'], request.form['medical'], request.form['observations'], 'Joyfe')
    return True

@application.route('/students/<int:id>', methods=['PUT'])
def ModifyStudent(id):
    # cosas
    return True

@application.route('/students/<int:id>', methods=['DELETE'])
def DeleteStudent(id):
    DeleteStudent(DataB, request.form['nick'])
    return True

# END STUDENTS

def id():
    url = "http://localhost:5000/students/"
    id = request.form['id']
    url += id
    webbrowser.open(url)

if __name__ == '__main__':
    application.run(debug=False)