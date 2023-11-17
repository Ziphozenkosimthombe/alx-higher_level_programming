#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa:"""


import MySQLdb
from sys import argv

if __name__ == '__name__':
    db = MySQLdb.connect(
            host='localhost', user=argv[1],
            port=3306, passwrd=argv[2],
            db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()

    for row in rows:
        print(row)
