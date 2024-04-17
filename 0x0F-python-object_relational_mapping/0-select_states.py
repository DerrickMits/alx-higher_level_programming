#!/usr/bin/env python3
import MySQLdb
import sys


if __name__ == "__main__":
    # Extracting MySQL username, password, and database name
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connecting to the MySQL server
    db = MySQLdb.connect(
        host="localhost", port=3306, user=username, passwd=password, db=db_name
    )
    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id")
    states = cursor.fetchall()

    # Displaying the retrieved states
    for state in states:
        print(state)

    # Closing cursor and database connection
    cursor.close()
    db.close()
