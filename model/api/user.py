
from flask import jsonify
from model.db import get_users

class User:
    @app.route('/users', methods=['GET'])
    def get_users():
        return jsonify(get_users())
        


