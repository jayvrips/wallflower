
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from model.db import Base, get_session, commit

class DbUser(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)
    profile = relationship("DbProfile", uselist=False, back_populates='user')

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (
                             self.name, self.fullname, self.password)

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
