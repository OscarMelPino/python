from flask import Flask, jsonify, request
import json, os, shutil
import main as app
from main import DataB
import webbrowser





application = Flask(__name__)

@application.route('/')
def Index():
    return 'Bienvenidos a SchoolerzZ'

@application.route('/login', methods=['POST'])
def Login():
    pal = ''
    lista = []
    user = request.form['username']
    pwd = request.form['password']
    tipe = request.form['usertype']
    cosa = app.Log(DataB(), tipe, user, pwd)
    if cosa == 0:
        webbrowser.open('http://localhost:5000', 0, False)
        # lista = app.Parents(DataB())
        # for l in lista:
        #     print(l)
    # if ret is not None :
    #     return ret
    # return 'Ocurrió un error.'

if __name__ == '__main__':
    application.run(debug=False)