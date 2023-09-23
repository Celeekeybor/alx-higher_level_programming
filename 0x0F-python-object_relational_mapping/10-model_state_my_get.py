#!/usr/bin/python3
"""
lists all State objects from the database hbtn_0e_6_usa
"""
import MySQLdb
from sys import argv
from sqlalchemy import (create_engine)
from model_state import Base, State
from sqlalchemy.orm import Session


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)

    flag = 0
    for state in session.query(State).filter_by(name=argv[4])\
                                     .order_by(State.id).all():
        print("{}".format(state.id))
        flag = 1
    if flag != 1:
        print("Not found")
    session.close()
