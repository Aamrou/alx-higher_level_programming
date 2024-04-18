#!/usr/bin/python3
"""
Module States
takes in an argument and displays all values in the states
"""
from sys import argv
import MySQLdb
if __name__ == '__main__':
    MY_USER = argv[1]
    MY_PASSWD = argv[2]
    MY_DB = argv[3]
    param = str(argv[4])

    '''Open Database connection'''
    mydb = MySQLdb.connect(host="localhost",
                           user=MY_USER,
                           passwd=MY_PASSWD,
                           db=MY_DB,
                           port=3306)

    '''Create cursor for operate over DB'''
    myCursor = mydb.cursor()
    query = "select * from states where binary name = '{}'".format(param)

    '''pass and execute a SQL sentence'''
    myCursor.execute(query)

    '''retrive records and fill cursor'''
    states = myCursor.fetchall()

    '''Print rows'''
    for state in states:
        print(state)

    '''close cursor'''
    myCursor.close()

    '''close connection to DB'''
    mydb.close()
