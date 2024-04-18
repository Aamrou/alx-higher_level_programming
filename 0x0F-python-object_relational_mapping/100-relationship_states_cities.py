#!/usr/bin/python3
'''creates the State “California” with the City “San Francisco” '''

import sys
from relationship_state import State
from relationship_city import Base, City
from sqlalchemy import (create_engine)
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
    california = State(name="California")

    # now create City San francisco and assign California State
    sanFrancisco = City(name="San Francisco")
    california.cities.append(sanFrancisco)

    session.add(sanFrancisco)
    session.commit()
    session.close()
