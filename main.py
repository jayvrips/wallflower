
import os
from flask import Flask, send_from_directory, render_template
from flask_cors import CORS

from controller.user import User, user_bp
from controller.profile import Profile, profile_bp
from controller.message import Message, message_bp
from controller.like import Like, like_bp

from model import db
from model.user import DbUser
from model.profile import DbProfile
from model.message import DbMessage
from model.like import DbLike

from flask_login import LoginManager, login_required, login_user, current_user, logout_user


app = Flask(__name__)
CORS(app)
app.secret_key = b'\x06\x9fT\x18\xbc]Q\x9d\xa5!~-\xe5\xea^\x0f\x8fo\xa7Yx\xd6\xbb)'

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    try:
        #TODO: fetch user from db
        # return User.get(user_id)
        session = db.get_session()
        db_user = session.query(DbUser).filter_by(id=user_id).first()
        return db_user
    except:
        raise ERROR("error")
    #TODO: if invalid ID:
    return None


def seed_user_db():
    user_data = [
        ["cyp", "cyp weis", "password1"],
        ["jay", "jay vr", "password1"],
        ["curt", "curt vr", "password1"]
    ]
    for data in user_data:
        session = db.get_session()
        db_user = DbUser(name=data[0],
                         fullname=data[1],
                         password=data[2])
        session.add(db_user)
        db.commit(session)
        db_profile = DbProfile(user_id = db_user.id)
        session.add(db_profile)
        db.commit(session)
        session.commit()

def seed_msg_db():
    msg_data = [
        [1, 2, "Hi there"],
        [1, 2, "Umm, ok"],
        [2, 1, "Hi yourself"],
        [1, 3, "Yo!"],
        [3, 1, "Whadup"]
    ]

    for data in msg_data:
        session = db.get_session()
        db_msg = DbMessage(sender_id=data[0],
                        recipient_id=data[1],
                        text=data[2])
        session.add(db_msg)
        db.commit(session)
        session.commit()

def seed_like_db():
    like_data = [
        [1, 2],
        [3, 2],
        [2, 1],
        [3, 1],
        [1, 3],
        [1, 3]
    ]

    for data in like_data:
        session = db.get_session()
        db_like = DbLike(sender_id=data[0],
                        recipient_id=data[1]
                        )
        session.add(db_like)
        db.commit(session)
        session.commit()


if __name__ == "__main__":
    needs_drop = True
    db.initialize(needs_drop=needs_drop)

    app.register_blueprint(user_bp)
    app.register_blueprint(profile_bp)
    app.register_blueprint(message_bp)
    app.register_blueprint(like_bp)

    if needs_drop:
        seed_user_db()
        seed_msg_db()
        seed_like_db()

    app.run("0.0.0.0", 8000)
