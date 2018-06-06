
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///:memory:', echo=True)
Session = sessionmaker(bind=engine)

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (
                             self.name, self.fullname, self.password)

def get_users():
    users = session.query(User).order_by(User.id)
    return dict(users)


def commit(session):
    try:
        session.commit()
    except:
        session.rollback()

if __name__ == "__main__":
    Base.metadata.create_all(engine)

    session = Session()

    user = User(name='ed', fullname='Ed Jones', password='edspassword')
    session.add(user)
    commit(session)

    for instance in session.query(User).order_by(User.id):
        print(instance.name, instance.fullname)



