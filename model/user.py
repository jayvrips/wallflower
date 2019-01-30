
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from model.db import Base, get_session, commit


class DbUser(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)
    profile = relationship("DbProfile", uselist=False, back_populates='user')
    is_authenticated = Column(Boolean, default=False)
    is_active = Column(Boolean, default=False)
    is_anonymous = Column(Boolean, default=True)


    @classmethod
    def get(cls, fullname):
        # user = DbUser(username)
        session = db.get_session()
        user = session.query(DbUser).filter_by(fullname=fullname).first()
        user.is_authenticated = True
        user.is_active = True
        return user


    def get_id(self):
        # log.dbg("get_id()")
        return self.fullname


    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (
                             self.name, self.fullname, self.password)


    def to_dict(self):
        return {
                   "id": self.id,
                   "profile_id": self.profile.id,
                   "name": self.name,
                   "fullname": self.fullname,
                   "is_authenticated": self.is_authenticated,
                   "is_active": self.is_active,
                   "is_anonymous": self.is_anonymous
               }


    def from_dict(self, user_dict):
        self.name = user_dict["name"]
        self.fullname = user_dict["fullname"]
        if "password" in user_dict:
            self.password = user_dict["password"]
