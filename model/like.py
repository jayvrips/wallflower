from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime

from model.db import Base, get_session, commit

class DbLike(Base):
    __tablename__ = 'likes'

    id = Column(Integer, primary_key=True)
    sender_id = Column(Integer, ForeignKey('profiles.id'))
    recipient_id = Column(Integer, ForeignKey('profiles.id'))
    sender = relationship("DbProfile", foreign_keys=[sender_id])
    recipient = relationship("DbProfile", foreign_keys=[recipient_id])
    read = Column(Boolean, nullable=False, default=False)

    def to_dict(self):
        return {
                    "id": self.id,
                    "sender_id": self.sender_id,
                    "sender_fullname": self.sender.user.fullname,
                    "recipient_id": self.recipient_id,
                    "read": self.read
               }

    def from_dict(self, like_dict):
        self.sender_id = like_dict["sender_id"]
        self.recipient_id = like_dict["recipient_id"]
        self.sender.user.fullname: like_dict["sender_fullname"]
        self.read = like_dict["read"]
