from flask import Flask, request, jsonify, abort
from datetime import timedelta, datetime
from functools import wraps
from enum import IntEnum
import os, json, jwt

application = Flask(__name__)
path_base = os.path.dirname(os.path.abspath(__file__))

TOKEN_KEY = 'SchoolerzZ'

class UserType(IntEnum):
    STUDENT = 1
    TEACHER = 2
    PARENT = 3
    MANAGER = 4


@application.route('route', methods=['GET'])
def Action():
    pass



@application.route('route', methods=['POST'])
def Action2():
    pass

@application.route('route/<string:nick>')
def GetUserByNick(nick):
    print('Parameter nick references the one sent in the url')   



def GenerateToken(nick)):
    token = jwt.encode({'type': 5},
        TOKEN_KEY,
            algorithm='HS256'
            )
            return jsonify({
                'id': user['id'],
                'name': user['name'],
                'token': token
            }), 200


if __name__ == '__main__':
    application.run(debug=True)
