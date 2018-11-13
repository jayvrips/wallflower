from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy orm import relationship

from model.db import Base, get_session, commit

class DbMessage(Base):
    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True)
    sender_id = Column(Integer, ForeignKey('profiles.id'))
    recipient_id = Column(Integer, ForeignKey('profiles.id'))
    # profile = relationship("DbUser", back_populates='profile')
    text = Column(String, nullable=False)

    def to_dict(self):
        return {
                    "id": self.id,
                    "sender_id": self.sender_id,
                    "recipient_id": self.recipient_id,
                    "text": self.text
               }

    def from_dict(self, message_dict):
        self.sender_id = message_dict["sender_id"]
        self.recipient_id = message_dict["recipient_id"]
        self.text = message_dict["text"]
