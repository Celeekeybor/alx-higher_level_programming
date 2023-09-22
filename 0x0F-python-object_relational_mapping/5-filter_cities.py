#!/usr/bin/python3
"""
Script that lists all `cities` in the `cities` table of `hbtn_0e_4_usa`
where the city's state matches the argument `state name`.

Arguments:
    mysql username (str)
    mysql password (str)
    database name (str)
    state name (str)
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Check if all four arguments are provided
    if len(sys.argv) != 5:
        print("Usage: {} <mysql username> <mysql password>\
        <database name> <state name>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]

    # Connect to the MySQL server
    db = MySQLdb.connect(user=username, passwd=password, db=database)
    cursor = db.cursor()

    # Create and execute the query to fetch cities for the given state
    query = "SELECT name FROM cities WHERE state_id IN\
    (SELECT id FROM states WHERE name = %s) ORDER BY id"
    cursor.execute(query, (state,))

    # Fetch all the results
    results = cursor.fetchall()

    # Display the results
    cities = [row[0] for row in results]
    print(", ".join(cities))

    # Close the cursor and connection
    cursor.close()
    db.close()
