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
    webbrowser.open('file://C:/Users/admin-dam2b/Desktop/python/python/index.html')

@application.route('/login', methods=['POST'])
def Login():
    global manager
    user = request.form['username']
    pwd = request.form['password']
    tipe = request.form['usertype']
    resp = app.Log(DataB(), tipe, user, pwd)
    if resp == 0:
        manager = GetManagerData(tipe + user, DataB())
        return 'Logeado en Shoolers con éxito.', 200
    if resp != 0:
        return 'Forbidden access', 403

# MANAGER
@application.route('/managers', methods=['GET'])
def GetManagers():
    return jsonify(GetAllManagers(DataB())), 200

@application.route('/managers/<int:id>', methods=['GET'])
def GetManagerById(id):
    return jsonify(GetManagerById(DataB(), id)), 200

@application.route('/managers', methods=['POST'])
def CreateManager():
    data = {'name' : request.form["name"],
            'sn1' : request.form["sn1"],
            'sn2': request.form["sn2"],
            'birth': request.form["birth"],
            'nationality' : request.form["nationality"],
            'country' : request.form["country"],
            'city' : request.form["city"],
            'postalcode': request.form["postalcode"],
            'address': request.form["address"],
            'email': request.form["email"],
            'phone1': request.form["phone1"],
            'passw': request.form["passw"]}
    CreateNewManager(DataB(), data)
    return 'Manager creado'

@application.route('/managers/<int:id>', methods=['PUT'])
def ModifyManager(id):
    return ModifyManager(DataB(), id)

@application.route('/managers/<int:id>', methods=['DELETE'])
def DeleteManager(id):
    return DeleteManager(DataB(), id), 202
# END MANAGER

@application.route('/delman/<int:id>', methods=['GET'])
def RedirectDeleteManager(id):
    request.delete('http://localhost:5000/managers/' + str(id))

@application.route('/updman/<int:id>', methods=['GET'])
def RedirectUpdateManager(id):
    request.put('http://localhost:5000/managers/' + str(id))


# PARENTS
@application.route('/parents', methods=['GET'])
def GetParent():
    return jsonify(GetAllParents(DataB())), 200

@application.route('/parents', methods=['GET'])
def DeleteParents():
    MyParentsList = GetAllParents(DataB(), "Joyfe")
    if request.form["idD"] is not None:
        DeleteParent(DataB(), MyParentsList[request.form["idD"]]["sz_003_nick"])
        return True
    return MyParentsList.__len__()

@application.route('/parents/<int:id>', methods=['GET'])
def GetParentsById(id):
    return jsonify(GetParentById(DataB(),id)), 200

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
@application.route('/students', methods=['GET'])
def GetStudents():
    return jsonify(GetAllStudents(DataB())), 200

@application.route('/students/<int:id>', methods=['GET'])
def GetStudentById(id):
    return jsonify(GetTeacherById(DataB(), id)), 200

@application.route('/students', methods=['POST'])
def CreateStudent():
    AddStudent(DataB, request.form['Name'],request.form['SN1'], request.form['SN2'], request.form['Birth'], request.form['Nacionality'], request.form['Country'], request.form['City'], request.form['PostalCode'], request.form['Addres'], request.form['Email'])
    return True

@application.route('/students/<int:id>', methods=['DELETE'])
def DeleteStudent(id):
    DeleteStudent(DataB, id)
    return 200

@application.route('/delStudents/<int:id>', methods=['GET'])
def RedirectDeleteStudent(id):
    request.delete('http://localhost:5000/students/' + str(id))

# END STUDENTS




# TEACHERS
@application.route('/teachers', methods=['GET'])
def GetTeachers():
    return jsonify(GetAllTeachers(DataB())), 200

@application.route('/teachers/<int:id>', methods=['GET'])
def GetTeacherById(id):
    return jsonify(GetTeacherById(DataB(), id)), 200

@application.route('/teachers', methods=['POST'])
def CreateTeacher():
    AddTeacher(DataB(), request.form['Name'], request.form['SN1'], request.form['SN2'], request.form['Birth'], request.form['Nacionality'], request.form['Country'], request.form['City'], request.form['PostalCode'], request.form['Addres'], request.form['Email'], request.form['Phone1'], request.form['Phone2'], request.form['School'])
    return 200

@application.route('/teachers/<int:id>', methods=['DELETE'])
def DeleteTeacher(id):
    DeleteTeacher(DataB(), id)
    return 200

@application.route('/delTeacher/<int:id>', methods=['GET'])
def RedirectDeleteTeacher(id):
    request.delete('http://localhost:5000/teachers/' + str(id))

def id():
    url = "http://localhost:5000/teachers/"
    id = request.form['id']
    url += id

if __name__ == '__main__':
    application.run(debug=False)