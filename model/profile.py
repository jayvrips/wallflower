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
    networth = Column(Integer, nullable=True)

    def to_dict(self):
        return {
                   "id": self.id,
                   "user_id": self.user.id,
                   "summary": self.summary,
                   "height": self.height,
                   "networth": self.networth
               }

    def from_dict(self, profile_dict):
        if 'summary' in profile_dict:
            self.summary = profile_dict["summary"]
        self.height = profile_dict["height"]
        self.networth = profile_dict["networth"]
