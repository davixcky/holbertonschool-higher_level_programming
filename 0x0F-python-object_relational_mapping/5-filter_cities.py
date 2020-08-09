#!/usr/bin/python3
'''Script that lists all states from the database hbtn_0e_0_usa'''
from sys import argv
import MySQLdb


if __name__ == '__main__':
    user, passwd, db, state = argv[1:]

    db_setting = {
            'host': 'localhost',
            'port': 3306,
            'user': user,
            'passwd': passwd,
            'db': db,
            'charset': "utf8"
            }

    conn = MySQLdb.connect(**db_setting)
    cur = conn.cursor()

    query = "SELECT cities.name " +\
            "FROM states, cities " +\
            "WHERE states.id = cities.state_id " +\
            "AND states.name = %s ORDER BY cities.id"
    cur.execute(query, (state, ))

    query_rows = cur.fetchall()
    cities = ""
    for row in query_rows:
        cities += row[0].strip('(),') + ", "

    print(cities.rstrip(', '))

    cur.close()
    conn.close()
