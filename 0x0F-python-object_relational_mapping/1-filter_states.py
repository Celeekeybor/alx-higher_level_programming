#!/usr/bin/python3
'''Script to list all states with a name starting with N'''


if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    # connect
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    # cursor
    c = db.cursor()

    # execute query
    c.execute("SELECT * FROM states WHERE\
    name LIKE BINARY 'N%' ORDER BY states.id")

    # fetch and print
    rows = c.fetchall()
    for row in rows:
        print(row)

    # close cursor and database
    c.close()
    db.close()
