#!/usr/bin/python3
"""
script that lists all states from the database hbtn_0e_0_usa:
"""

if __name__ == "__main__":

    import MySQLdb
    from sys import argv

    # connect database using the command-line arguments
    my_db = MySQLdb.connect(host='localhost', user=argv[1], password=argv[2],
                            db=argv[3], port=3306)
    # create the cursor object to iterate with database
    my_cursor = my_db.cursor()

    # exercuting the SELECT quary to fatch the data
    my_cursor.execute(
        """SELECT cities.id, cities.name
        FROM cities
        JOIN states
        ON cities.state_id = states.id
        WHERE states.name
        LIKE BINARY %(state_name)s
        ORDER BY cities.id ASC
        """, 'state_name': argv[4])

    # fetching all the data returned by the quary
    my_data = my_cursor.fetchall()

    # iterate the fatch data and print each row
    if my_date is not None:
        print(", ".join([row[1] for row in my_data]))

    # closing all the cursor
    my_cursor.close()

    # closing all the database
    my_db.close
