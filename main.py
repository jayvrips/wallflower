
import os

from flask import Flask, send_from_directory, render_template
from flask_cors import CORS

from model import db

from controller.user import User, user_bp
from controller.profile import Profile, profile_bp
from controller.message import message_bp

app = Flask(__name__)
CORS(app)

if __name__ == "__main__":
    db.initialize()

    app.register_blueprint(user_bp)
    app.register_blueprint(profile_bp)
    app.register_blueprint(message_bp)
    app.run("0.0.0.0", 8000)
