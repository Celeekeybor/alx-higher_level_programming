#!/usr/bin/python3
"""
Script that lists all State objects that contain the letter a from database.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    """
    Entry point of the script. Retrieves State objects that contain
    the letter 'a' from the database.
    """

    # Get MySQL credentials and database name from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL server
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}'
    )
    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    session = Session()

    states = session.query(State)\
        .filter(State.name.like('%a%'))\
        .order_by(State.id)\
        .all()

    # Print the retrieved State objects
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()

