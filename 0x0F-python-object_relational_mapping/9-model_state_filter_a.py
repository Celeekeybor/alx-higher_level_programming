#!/usr/bin/python3
# lists all State objects that contain the letter a from a database


if __name__ == "__main__":
    from model_state import Base, State
    from sys import argv
    import sqlalchemy
    from sqlalchemy.engine.url import URL
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session

    mysql = {'drivername': 'mysql+mysqldb',
             'host': 'localhost',
             'port': '3306',
             'username': argv[1],
             'password': argv[2],
             'database': argv[3],
             }

    url = URL(**mysql)

    engine = create_engine(url, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)

    query = session.query(State).filter(State.name.like('%a%'))\
                                .order_by(State.id)
    for r in query.all():
        print("{}: {}".format(r.id, r.name))

    session.close()

