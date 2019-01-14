
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from model.db import Base, get_session, commit
from flask_login import UserMixin

#
# class User(UserMixin):


class DbUser(UserMixin, Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)
    profile = relationship("DbProfile", uselist=False, back_populates='user')
    # is_active = Column(Boolean, default=False)

    # def is_active(self):
    #     # Here you should write whatever the code is
    #     # that checks the database if your user is active
    #     return self.active
    #
    # def is_anonymous(self):
    #     return False
    #
    # def is_authenticated(self):
    #     return True
    #
    # def get_id(self):
    #     return unicode(self.id)

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (
                             self.name, self.fullname, self.password)



    # @login_manager.user_loader
    # def load_user(user_id):
    #     # session = db.ge_session()
    #     # db_user = session.query(DbUser).filter_by(id=user_id).first()
    #     # return db_user
    #     return DbUser.query.get(int(user_id))


    def to_dict(self):
        return {
                   "id": self.id,
                   "profile_id": self.profile.id,
                   "name": self.name,
                   "fullname": self.fullname
               }


    def from_dict(self, user_dict):
        self.name = user_dict["name"]
        self.fullname = user_dict["fullname"]
        if "password" in user_dict:
            self.password = user_dict["password"]
