#!/usr/bin/python3
'''List all State objects from the db hbtn_0e_6_usa'''

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1],
                                  sys.argv[2],
                                  sys.argv[3]),
                           pool_pre_ping=True)
    session = sessionmaker(bind=engine)()
    result = session.query(State, City).join(City)
    for row in result:
        print(str(row[0]).split(':')[1][1:] + ":" + str(row[1]).split(':')[1])
    session.close()
