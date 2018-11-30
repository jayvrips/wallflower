
import json

from flask import Blueprint, jsonify, Response, request
from model import db
from model.profile import DbProfile
from model.message import DbMessage

profile_bp = Blueprint('profile', __name__)

class Profile:


        @profile_bp.route('/profile/<int:profile_id>', methods=['OPTIONS'])
        def option_profile(profile_id):
            resp = Response();
            resp.headers['Access-Control-Allow-Origin'] = '*'
            resp.headers["Allow"] = "PUT, OPTIONS"
            resp.headers["Access-Control-Allow-Methods"] = "PUT, OPTIONS"
            resp.headers["Access-Control-Allow-Headers"] = "X-Requested-With, X-HTTP-Method-Override, Content-Type, Cache-Control, Accept"
            return resp

        @profile_bp.route('/profile/<int:profile_id>', methods=['PUT'])
        def put_profile(profile_id):
            profile_data = request.get_json()

            session = db.get_session()
            db_profile = session.query(DbProfile).filter_by(id=profile_id).first()
            db_profile.from_dict(profile_data)
            db.commit(session)

            resp = jsonify(db_profile.to_dict())
            resp.headers['Access-Control-Allow-Origin'] = '*'
            resp.headers["Allow"] = "PUT,POST,OPTIONS"
            resp.headers["Access-Control-Allow-Methods"] = "PUT, OPTIONS"
            resp.headers["Access-Control-Allow-Headers"] = "X-Requested-With, X-HTTP-Method-Override, Content-Type, Cache-Control, Accept"
            return resp

        @profile_bp.route('/profile/<int:profile_id>/chats', methods=['GET'])
        def get_profile_chats(profile_id):
            session = db.get_session()
            db_profile = session.query(DbProfile).filter_by(id=profile_id).first()
            db_profile_chats = session.query(DbMessage).filter_by(sender_id=profile_id).all()
            profile_chats = {}
            for db_profile_chat in db_profile_chats:
                profile_chats[db_profile_chat.id] = db_profile_chat.to_dict()

            resp = jsonify(profile_chats)
            resp.headers['Access-Control-Allow-Origin'] = '*'
            return resp

        @profile_bp.route('/profiles', methods=['GET'])
        def get_profiles():
            session = db.get_session()
            db_profiles = session.query(DbProfile).order_by(DbProfile.id)
            profiles = {}
            for db_profile in db_profiles:
                profiles[db_profile.id] = db_profile.to_dict()

            resp = jsonify(profiles)
            resp.headers['Access-Control-Allow-Origin'] = '*'
            return resp
