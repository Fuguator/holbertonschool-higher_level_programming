#!/usr/bin/python3
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )
    mycursor = db.cursor()

    try:
        mycursor.execute("SELECT id, name FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
        rows = mycursor.fetchall()
        
        for row in rows:
            print(row)
    except MySQLdb.Error as e:
        print(e)
    finally:
        mycursor.close()
        db.close()
