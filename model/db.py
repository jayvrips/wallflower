
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
Session = None

def initialize():
    global Session

    engine = create_engine('sqlite:///wallflower.db', echo=True)
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)

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
    session = Session()
    users = session.query(User).order_by(User.id)
    
    return users #[user.to_dict() for user in users]


def commit(session):
    try:
        session.commit()
    except:
        session.rollback()

if __name__ == "__main__":
    initialize()

    session = Session()

    user = User(name='ed', fullname='Ed Jones', password='edspassword')
    session.add(user)
    commit(session)

    for instance in session.query(User).order_by(User.id):
        print(instance.name, instance.fullname)



