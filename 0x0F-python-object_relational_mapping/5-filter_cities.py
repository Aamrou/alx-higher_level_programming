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
    paramstate = argv[4]

    '''Open Database connection'''
    mydb = MySQLdb.connect(host="localhost",
                           user=MY_USER,
                           passwd=MY_PASSWD,
                           db=MY_DB)

    '''Create cursor for operate over DB'''
    myCursor = mydb.cursor()

    '''pass and execute a SQL sentence'''
    sql = "select cities.name from cities\
           inner join states on cities.state_id = states.id\
           where states.name = %s\
           order by cities.id asc"
    myCursor.execute(sql, (paramstate,))

    '''retrive records and fill cursor'''
    cities = myCursor.fetchall()

    '''Print rows'''
    c = ", ".join(city[0] for city in cities)
    print(c)
    '''close cursor'''
    myCursor.close()

    '''close connection to DB'''
    mydb.close()
