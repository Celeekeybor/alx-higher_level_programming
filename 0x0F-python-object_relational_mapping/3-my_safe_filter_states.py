#!/usr/bin/python3

"""
This script lists all values in the `states` table of the
`hbtn_0e_0_usa` database
where `name` matches the argument `state name searched`.

The script takes four arguments:
    * The MySQL username
    * The MySQL password
    * The database name
    * The state name to search for

The script connects to the MySQL database on the
default host (localhost) and port (3306).

The script uses the `sys` module to get the MySQL username, password,
and database name from the command line arguments.

The script uses the `MySQLdb` module to execute the SQL query `SELECT *
FROM states WHERE name = %s ORDER BY id`.

The results of the query are then printed to the console.
"""


import sys
import MySQLdb


def main():
    """
    This function connects to the MySQL database and lists all values in the
    states table
    where name matches the argument.
    """

    # Get the MySQL username from the command line arguments.
    username = sys.argv[1]

    # Get the MySQL password from the command line arguments.
    password = sys.argv[2]

    # Get the database name from the command line arguments.
    database = sys.argv[3]

    # Get the state name to search for from the command line arguments.
    city_name = sys.argv[4]

    # Connect to the MySQL database.
    connection = MySQLdb.connect(user=username, passwd=password, db=database)

    # Create a cursor object.
    cursor = connection.cursor()

    # Execute the SQL query.
    query = "SELECT * FROM states WHERE name = %s ORDER BY id"
    cursor.execute(query, (city_name,))

    # Iterate over the results and print each row.
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close the cursor object.
    cursor.close()
    # Close the connection to the database.
    connection.close()


if __name__ == "__main__":
    main()

