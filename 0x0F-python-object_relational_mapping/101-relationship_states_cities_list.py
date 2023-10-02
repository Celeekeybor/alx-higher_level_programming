#!/usr/bin/python3
'''List all State objects from the db hbtn_0e_6_usa'''

import sys
from relationship_state import Base, State
from relationship_city import City
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
        print(str(row.id) + ": " + row.name)
        for city in row.cities:
            print("    " + str(city.id) + ": " + city.name)
    session.close()
