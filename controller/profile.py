
import json

from flask import Blueprint, jsonify, Response, request
from model import db
from model.profile import DbProfile
from model.message import DbMessage
from sqlalchemy import asc, desc, and_, or_
from sqlalchemy.orm import aliased


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

        @profile_bp.route('/profiles/<int:profile_id>', methods=['GET'])
        def get_profile(profile_id):
            session = db.get_session()
            db_profile = session.query(DbProfile).filter_by(id=profile_id).first()

            resp = jsonify(db_profile.to_dict())
            resp.headers['Access-Control-Allow-Origin'] = '*'
            return resp

        @profile_bp.route('/chats/<int:profile_id>', methods=['GET'])
        def get_profile_chats(profile_id):
            session = db.get_session()
            db_profile = session.query(DbProfile).filter_by(id=profile_id).first()

            # ORDER BY DOES NOT SEEM TO BE WORKING, NOR DISTINCT
            # new_db_profile_chats = session.query(DbMessage).filter_by(
            #     sender_id=profile_id).distinct(DbMessage.recipient_id).all()
            db_profile_chats = session.query(DbMessage).filter_by(
                sender_id=profile_id).order_by(asc(DbMessage.recipient_id)).all()

            unique_recipients = []
            new_db_profile_chats = []
            for db_profile_chat in db_profile_chats:
                if not unique_recipients:
                    unique_recipients.append(db_profile_chat.recipient_id)
                    new_db_profile_chats.append(db_profile_chat)

                if db_profile_chat.recipient_id != unique_recipients[-1]:
                    unique_recipients.append(db_profile_chat.recipient_id)
                    new_db_profile_chats.append(db_profile_chat)

            profile_chats = {}
            for db_profile_chat in new_db_profile_chats:
                print(db_profile_chat.recipient_id)
                profile_chats[db_profile_chat.id] = db_profile_chat.to_dict()

            resp = jsonify(profile_chats)
            resp.headers['Access-Control-Allow-Origin'] = '*'
            return resp

        @profile_bp.route('/chathistory/<int:profile_id>/<int:recipient_id>', methods=['GET'])
        def get_chat_history(profile_id, recipient_id):
            session = db.get_session()

            all_msgs = session.query(DbMessage).filter(
                and_(or_(DbMessage.sender_id == profile_id, DbMessage.sender_id == recipient_id),
                or_(DbMessage.recipient_id == recipient_id, DbMessage.recipient_id == profile_id))
                )


            # STILL CANT GET order_by TO WORK
            all_msgs_list = all_msgs.order_by(desc(DbMessage.sender_id)).all()

            chat_history = {}
            for chat in all_msgs_list:
                chat_history[chat.id] = chat.to_dict()

            resp = jsonify(chat_history)
            resp.headers['Access-Control-Allow-Origin'] = '*'
            return resp

        @profile_bp.route('/profiles', methods=['GET'])
        # add param to endpoint so that we can filter the profiles to return all their attributes/data
        # or just a summary ... do a join on profiel & details table for all; just use profile table for summary
        def get_profiles():
            session = db.get_session()
            db_profiles = session.query(DbProfile).order_by(DbProfile.id)
            profiles = {}
            for db_profile in db_profiles:
                profiles[db_profile.id] = db_profile.to_dict()

            resp = jsonify(profiles)
            resp.headers['Access-Control-Allow-Origin'] = '*'
            return resp
