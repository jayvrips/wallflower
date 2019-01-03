
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
Session = None

def initialize(needs_drop=False):
    global Session


    engine = create_engine('sqlite:///wallflower.db', echo=True)
    Session = sessionmaker(bind=engine)
    if needs_drop:
        Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

def get_session():
    return Session()

def commit(session):
    try:
        session.commit()
    except:
        session.rollback()
        raise

# NOTE: THIS MAIN FUNCTION IS CALLED DIRECTLY ONLY IF THE FILE IS RUN DIRECTLY
if __name__ == "__main__":
    initialize(needs_drop=False)

    session = Session()

    for instance in session.query(User).order_by(User.id):
        print(instance.name, instance.fullname)
