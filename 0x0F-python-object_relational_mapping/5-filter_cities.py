#!/usr/bin/python3

"""
Script that takes in a state as an argument and lists
all cities in that state
"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * from `cities` as `c` \
                INNER JOIN `states` as `s` \
                ON `c`.`state_id` = `s`.`id` \
                ORDER BY `c`.`id`")
    print(", ".join([city[2] for city in cur.fetchall()
                    if city[4] == argv[4]]))
    cur.close()
    db.close()
