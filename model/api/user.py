
from flask import Blueprint, jsonify, Response
from model.db import get_users

user_bp = Blueprint('user', __name__)

'''
 response.headers["Allow"] = "HEAD,GET,PUT,POST,DELETE,OPTIONS"
  response.headers["Access-Control-Allow-Headers"] = "X-Requested-With, X-HTTP-Method-Override, Content-Type, Cache-Control, Accept"
  #Dont need 44...i think because we have 36
  response.headers["Access-Control-Allow-Origin"] = "*"
'''

class User:
    @user_bp.route('/users', methods=['GET'])
    def get_users():
        users = get_users()
        #resp = Response(dumps([user.to_dict() for user in users]))
        resp = jsonify([user.to_dict() for user in users])
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp
        
        


