#!/usr/bin/python3
import sys
import os
import sqlite3

if len(sys.argv) > 1:
    db = sys.argv[1]
else:
    print("Please specify database")
    exit()

myconn = sqlite3.connect(db)

cu = myconn.cursor()

with open('populate_potus.sql') as pop_in:
    sql = pop_in.read()

cu.executescript(sql)
myconn.commit()
cu.close()
myconn.close()
