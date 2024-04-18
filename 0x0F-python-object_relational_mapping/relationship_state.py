#!/usr/bin/python3
''' Use of SQlALchemy
    contains the class definition of a State and
    an instance Base = declarative_base()
'''

from sqlalchemy import Column,  Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from relationship_city import Base, City


# Mapping table states
class State(Base):
    ''' Table states'''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    # this is how to establish a relation with Cities class "one-to-many"
    cities = relationship("City", backref="states",
                          cascade="all, delete, delete-orphan")
