#!/usr/bin/python3
'''Prints state object that contains a from the db hbtn_0e_6_usa'''

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1],
                                  sys.argv[2],
                                  sys.argv[3]),
                           pool_pre_ping=True)
    session = sessionmaker(bind=engine)()
    result = session.query(State).all()
    for row in result:
        if 'a' in str(row):
            print(row)
    session.close()
