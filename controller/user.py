
import json

from flask import Blueprint, jsonify, Response, request, session
from model import db
from model.user import DbUser
from model.profile import DbProfile


user_bp = Blueprint('user', __name__)


 # response.headers["Allow"] = "HEAD,GET,PUT,POST,DELETE,OPTIONS"
 #  response.headers["Access-Control-Allow-Headers"] = "X-Requested-With, X-HTTP-Method-Override, Content-Type, Cache-Control, Accept"
 #  #Dont need 44...i think because we have 36
 #  response.headers["Access-Control-Allow-Origin"] = "*"


class User:
    @user_bp.route('/users', methods=['GET'])
    def get_users():
        session = db.get_session()
        db_users = session.query(DbUser).order_by(DbUser.id)
        users = {}
        for db_user in db_users:
            users[db_user.id] = db_user.to_dict()

        resp = jsonify(users)
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp

    @user_bp.route('/users/<int:user_id>', methods=['GET'])
    def get_user():
        session = db.get_session()
        db_user = session.query(DbUser).filter_by(id=user_id).first()

        resp = jsonify(db_user.to_dict())
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp

    @user_bp.route('/user', methods=['OPTIONS'])
    def option_user():
        resp = Response();
        resp.headers['Access-Control-Allow-Origin'] = '*'
        resp.headers["Allow"] = "POST,OPTIONS"
        resp.headers["Access-Control-Allow-Headers"] = "X-Requested-With, X-HTTP-Method-Override, Content-Type, Cache-Control, Accept"
        return resp

    @user_bp.route('/user', methods=['POST'])
    def post_user():
        user_data = request.get_json()

        session = db.get_session()
        db_user = DbUser(name=user_data["name"],
                         fullname=user_data["fullname"],
                         password=user_data["password"])

        session.add(db_user)
        db.commit(session)
        db_profile = DbProfile(user_id = db_user.id)
        session.add(db_profile)
        db.commit(session)

        resp = jsonify(db_user.to_dict())
        resp.headers['Access-Control-Allow-Origin'] = '*'
        resp.headers["Allow"] = "POST,OPTIONS"
        resp.headers["Access-Control-Allow-Headers"] = "X-Requested-With, X-HTTP-Method-Override, Content-Type, Cache-Control, Accept"
        return resp

    @user_bp.route('/users/<int:user_id>', methods=['PUT'])
    def put_user(user_id):
        user_data = request.get_json()

        session = db.get_session()
        db_user = session.query(DbUser).filter_by(id=user_id).first()
        db_user.from_dict(user_data)
        db.commit(session)

        resp = jsonify(db_user.to_dict())
        resp.headers['Access-Control-Allow-Origin'] = '*'
        resp.headers["Allow"] = "PUT,POST,OPTIONS"
        resp.headers["Access-Control-Allow-Headers"] = "X-Requested-With, X-HTTP-Method-Override, Content-Type, Cache-Control, Accept"
        return resp
