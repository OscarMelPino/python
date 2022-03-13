from flask import Flask, jsonify, request
import json, os, shutil
import main as app

application = Flask(__name__)

@application.route('/')
def Index():
    return 'Bienvenidos a SchoolerzZ'

@application.route('/login', methods=['POST'])
def Login():
    user = request.form['username']
    pwd = request.form['password']
    tipe = request.form['usertype']
    ret = app.MainLogin(tipe, user, pwd)
    if ret is not None :
        return ret
    return 'Ocurrió un error.'

if __name__ == '__main__':
    application.run(debug=False)