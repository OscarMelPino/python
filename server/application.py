from pickletools import read_uint1
from flask import Flask, jsonify, request
import json, os, shutil
import main as app
from main import DataB
import webbrowser
from main import GetSchoolNameFromManager, GetManagerData
from manager import Manager

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
    cosa = app.Log(DataB(), tipe, user, pwd)
    if cosa == 0:
        manager = GetManagerData(tipe + user, DataB())
        webbrowser.open('file:///C:/Users/oscar/Desktop/python/manager_actions.html', 0, False)
        return '', 200
    if cosa != 0:
        return 'Forbidden access', 403

if __name__ == '__main__':
    application.run(debug=False)