#!/usr/bin/python3
"""
Script that takes in an argument and displays entries
in a db where the name matches the arg
Protected from Injection attacks
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE %s ORDER BY \
                id ASC", (sys.argv[4],))
    [print(state) for state in cur.fetchall() if state[1] == sys.argv[4]]
    cur.close()
    db.close()
