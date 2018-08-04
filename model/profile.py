from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from model.db import Base, get_session, commit

class DbProfile(Base):
    __tablename__ = 'profiles'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("DbUser", back_populates='profile')
    summary = Column(String, nullable=True)
    height = Column(Integer, nullable=True)
