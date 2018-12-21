
import json

from flask import Blueprint, jsonify, Response, request
from model import db
from model.message import DbMessage

message_bp = Blueprint('message', __name__)

class Message:

        @message_bp.route('/message', methods=['OPTIONS'])
        def option_message():
            resp = Response();
            resp.headers['Access-Control-Allow-Origin'] = '*'
            resp.headers["Allow"] = "POST,OPTIONS"
            resp.headers["Access-Control-Allow-Headers"] = "X-Requested-With, X-HTTP-Method-Override, Content-Type, Cache-Control, Accept"
            return resp

        @message_bp.route('/message', methods=['POST'])
        def post_message():
            message_data = request.get_json()

            session = db.get_session()
            db_message = DbMessage(sender_id=message_data["sender_id"],
                             recipient_id=message_data["recipient_id"],
                             text=message_data["text"])

            session.add(db_message)
            db.commit(session)

            resp = jsonify(db_message.to_dict())
            resp.headers['Access-Control-Allow-Origin'] = '*'
            resp.headers["Allow"] = "POST,OPTIONS"
            resp.headers["Access-Control-Allow-Headers"] = "X-Requested-With, X-HTTP-Method-Override, Content-Type, Cache-Control, Accept"
            return resp
