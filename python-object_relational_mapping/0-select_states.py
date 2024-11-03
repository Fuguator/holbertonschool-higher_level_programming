#!/usr/bin/python3
"""salam"""

if __name__ == "__main__":
    """salam"""
    import MySQLdb
    from sys import argv

    username = argv[1]
    password = argv[2]
    db_name = argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=db_name)
    cur = db.cursor()
    cur.execute("SELECT * FROM `states` ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
