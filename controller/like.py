import json

from flask import Blueprint, jsonify, Response, request
from model import db
from model.like import DbLike
from model.profile import DbProfile

like_bp = Blueprint('like', __name__)

class Like:

    @like_bp.route('/like', methods=['OPTIONS'])
    def option_message():
        resp = Response();
        resp.headers['Access-Control-Allow-Origin'] = '*'
        resp.headers["Allow"] = "POST, OPTIONS"
        resp.headers["Access-Control-Allow-Headers"] = "X-Requested-With, X-HTTP-Method-Override, Content-Type, Cache-Control, Accept"
        return resp

    @like_bp.route('/like', methods=['POST'])
    def like_message():
        like_data = request.get_json()

        session = db.get_session()
        db_like = DbLike(sender_id=like_data["sender_id"],
                        recipient_id=like_data["recipient_id"]
                        )

        session.add(db_like)
        db.commit(session)

        resp = jsonify(db_like.to_dict())
        resp.headers['Access-Control-Allow-Origin'] = '*'
        resp.headers["Allow"] = "POST, OPTIONS"
        resp.headers["Access-Control-Allow-Headers"] = "X-Requested-With, X-HTTP-Method-Override, Content-Type, Cache-Control, Accept"
        return resp


    @like_bp.route('/likes/<int:profile_id>', methods=['GET'])
    def get_profile_likes(profile_id):
        session = db.get_session()
        db_profile = session.query(DbProfile).filter_by(id=profile_id).first()
        db_profile_likes = session.query(DbLike).filter_by(
            recipient_id=profile_id).all()

        profile_likes = {}
        for db_profile_like in db_profile_likes:
            profile_likes[db_profile_like.id] = db_profile_like.to_dict()

        resp = jsonify(profile_likes)
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp
