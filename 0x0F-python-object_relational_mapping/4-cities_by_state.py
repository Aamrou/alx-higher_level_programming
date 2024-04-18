#!/usr/bin/python3
"""
Module States
 cript that lists all cities from the database hbtn_0e_4_usa
"""
from sys import argv
import MySQLdb
if __name__ == '__main__':
    MY_USER = argv[1]
    MY_PASSWD = argv[2]
    MY_DB = argv[3]

    '''Open Database connection'''
    mydb = MySQLdb.connect(host="localhost",
                           user=MY_USER,
                           passwd=MY_PASSWD,
                           db=MY_DB)

    '''Create cursor for operate over DB'''
    myCursor = mydb.cursor()

    '''pass and execute a SQL sentence'''
    myCursor.execute("select cities.id, cities.name, states.name  from cities \
                      inner join states on cities.state_id = states.id\
                      order by 1")

    '''retrive records and fill cursor'''
    cities = myCursor.fetchall()

    '''Print rows'''
    for city in cities:
        print(city)

    '''close cursor'''
    myCursor.close()

    '''close connection to DB'''
    mydb.close()
