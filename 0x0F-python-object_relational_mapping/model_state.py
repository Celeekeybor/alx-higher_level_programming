#!/usr/bin/python3
''' Defined State class which inherits from Base class '''
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


# using declarative_base func to return a new base class, mapped class State
# will inherit from Base and generate new Table and mapper()
# declare new mapping
Base = declarative_base()


# map class to inherit from Base
class State(Base):
    """mapped class definition"""

    # 3 important: Table, mapper(), class objects

    # Table
    __tablename__ = 'states'

    # Describe table, column objects, use methods imported from sqlalchemy
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
