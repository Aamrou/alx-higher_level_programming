#!/usr/bin/python3
'''  prints all City objects from the database hbtn_0e_14_usa:'''

import sys
from model_city import City
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    dbConnector = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(dbConnector.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Base.metadata.bind = engine
    DBSession = sessionmaker()
    DBSession.bind = engine
    session = DBSession()

    # query = session.query(State).join(City).all()

    for state, city in\
        session.query(State, City).\
            filter(State.id == City.state_id).order_by(City.id).all():
        print("{}: ({}) {}".format(state.name, city.id, city.name,))

    session.close()
