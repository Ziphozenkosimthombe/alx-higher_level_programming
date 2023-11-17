#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa:"""


import MySQLdb
from sys import argv

if __name__ == '__name__':

    # connect database using the command-line arguments
    myDB = MySQLdb.connect(
            host='localhost', user=argv[1],
            port=3306, passwd=argv[2],
            db=argv[3])
    # create the cursor object to iterate with database
    myCur = myDB.cursor()
    # exercuting the SELECT quary to fatch the data
    cur.execute("SELECT * FROM states ORDER BY states.id ASC;")
    # fetching all the data returned by the quary
    rows = cur.fetchall()
    # iterate the fatch data and print each row
    for row in rows:
        print(row)

    # closing all the cursor
    myCursor.close()

    # closing all the database
    myDB.close()
