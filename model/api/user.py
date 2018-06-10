
from flask import Blueprint, jsonify
from model.db import get_users

user_bp = Blueprint('user', __name__)

class User:
    @user_bp.route('/users', methods=['GET'])
    def get_users():
        users = get_users()
        
        return jsonify([user.to_dict() for user in users])
        


