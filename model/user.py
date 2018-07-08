
from sqlalchemy import Column, Integer, String

from model.db import Base, get_session

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (
                             self.name, self.fullname, self.password)

    def to_dict(self):
        return {
                   "id": self.id,
                   "name": self.name,
                   "fullname": self.fullname
               }

def get_users():
    session = get_session()
    users = session.query(User).order_by(User.id)
    
    return users



