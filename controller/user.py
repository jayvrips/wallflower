
import json

from flask import Blueprint, jsonify, Response, request, session, redirect
from model import db
from model.user import DbUser
from model.profile import DbProfile

from flask_login import login_user, login_required, current_user

user_bp = Blueprint('user', __name__)


 # response.headers["Allow"] = "HEAD,GET,PUT,POST,DELETE,OPTIONS"
 #  response.headers["Access-Control-Allow-Headers"] = "X-Requested-With, X-HTTP-Method-Override, Content-Type, Cache-Control, Accept"
 #  #Dont need 44...i think because we have 36
 #  response.headers["Access-Control-Allow-Origin"] = "*"


class User:
    @user_bp.route('/users', methods=['GET'])
    @login_required
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

    @user_bp.route('/login', methods=['GET', 'POST'])
    def login():
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        user_data = request.get_json()
        if request.method == 'POST':
            #TODO: verify creds correctly
            if user_data['fullname'] == 'curt vr':
                # user = User(request.form['username'])
                session = db.get_session()
                user = session.query(DbUser).filter_by(fullname='curt vr').first()
                user.is_authenticated = True
                user.is_active = True
                try:
                    login_user(user)
                    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
                except:
                    # log.tb()
                    raise ERROR("error")
                print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                print("User logged in as: %s" % current_user.fullname, current_user.is_authenticated, current_user.is_active)
                # return "cool"
                return redirect("http://0.0.0.0:8000/profiles")
            #TODO: else indicate login failure in login.html
        # return render_template('login.html')
        return "cool"

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
