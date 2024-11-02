#!/usr/bin/python3
"""Get all states"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect(
        host = 'localhost',
        port = 3306,
        user = argv[1],
        password = argv[2],
        database=argv[3]    
    )
    
    cursor = db.cursor()
    cursor.execute('SELECT * FROM states ORDER BY id ASC')
    
    [print(state) for state in cursor.fetchall()]
    
    if cursor:
        cursor.close()
    if db:
        db.close()