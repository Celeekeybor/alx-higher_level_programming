#!/usr/bin/python3
"""
changes the name of a State object from the database hbtn_0e_6_usa
"""
from sys import argv
from sqlalchemy import (create_engine)
from model_state import Base, State
from sqlalchemy.orm import Session


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)

    for state in session.query(State).order_by(State.id).all():
        for c in state.name:
            if c == 'a':
                session.delete(state)
                break
    session.commit()
    session.close()
