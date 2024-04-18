#!/usr/bin/python3
''' adds the State object “Louisiana” to the database hbtn_0e_6_usa '''

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    dbConnector = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(dbConnector.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Base.metadata.bind = engine
    DBSession = sessionmaker()
    DBSession.bind = engine
    session = DBSession()

    # create state object
    addState = State(name="Louisiana")
    # commit and close session
    session.add(addState)
    session.commit()

    query = session.query(State).filter(
        State.name == 'Louisiana')

    if query.count() > 0:
        for instance in query:
            print(str(instance.id))

    session.close()
