#!/usr/bin/python3
"""
script that lists all states from the database hbtn_0e_0_usa:
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":

    # connect database using the command-line arguments
    my_db = MySQLdb.connect(host='localhost', user=argv[1], password=argv[2],
                            db=argv[3], port=3306)
    # create the cursor object to iterate with database
    my_cursor = my_db.cursor()

    # exercuting the SELECT quary to fatch the data
    my_cursor.execute(
        """SELECT * FROM states WHERE name LIKE BINARY '{}'
        ORDER BY states.id ASC
        """.format(argv[4]))

    # fetching all the data returned by the quary
    my_data = my_cursor.fetchall()

    # iterate the fatch data and print each row
    for row in my_data:
        print(row)

    # closing all the cursor
    my_cursor.close()

    # closing all the database
    my_db.close
