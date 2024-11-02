#!/usr/bin/python3
"""Get all states"""
from sys import argv
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(
        user = argv[1],
        password = argv[2],
        database=argv[3]    
    )
    
    cursor = db.cursor()
    cursor.execute('select * from states')
    
    [print(state) for state in cursor.fetchall()]