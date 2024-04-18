#!/usr/bin/python3
''' Use of SQlALchemy
    contains the class definition of a State and
    an instance Base = declarative_base()
'''

from sqlalchemy import Column,  Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
Base = declarative_base()


# Mapping table states
class City (Base):
    ''' Table cities'''
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
