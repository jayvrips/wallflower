from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from model.db import Base, get_session, commit

class DbMessage(Base):
    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True)
    sender_id = Column(Integer, ForeignKey('profiles.id'))
    recipient_id = Column(Integer, ForeignKey('profiles.id'))
    sender = relationship("DbProfile", foreign_keys=[sender_id])
    recipient = relationship("DbProfile", foreign_keys=[recipient_id])
    text = Column(String, nullable=False)

    def to_dict(self):
        return {
                    "id": self.id,
                    "sender_id": self.sender_id,
                    #"sender_fullname": self.sender.user_fullname,
                    "recipient_id": self.recipient_id,
                    "recipient_fullname": self.recipient.user.fullname,
                    "text": self.text
               }

    def from_dict(self, message_dict):
        self.sender_id = message_dict["sender_id"]
        self.recipient_id = message_dict["recipient_id"]
        self.recipient.user.fullname: message_dict["recipient_fullname"]
        self.text = message_dict["text"]

    # db.create_all()
    # db.session.commit()
