
import json

from flask import Blueprint, jsonify, Response, request
from model import db
import model.user
from model.user import get_users

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
        resp = jsonify([user.to_dict() for user in users])
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp
        
    @user_bp.route('/users/<int:user_id>', methods=['PUT'])
    def put_users(user_id):
        data = request.get_json()
        user = model.user.User(name=data["name"], fullname=data["fullname"], password=data["password"])
        s = db.get_session()
        s.add(user)
        db.commit(s)

        resp = Response("awesome")
        resp.headers["Allow"] = "PUT,POST,OPTIONS"
        resp.headers["Access-Control-Allow-Headers"] = "X-Requested-With, X-HTTP-Method-Override, Content-Type, Cache-Control, Accept"
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp
        


