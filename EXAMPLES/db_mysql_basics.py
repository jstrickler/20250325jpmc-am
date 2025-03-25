from contextlib import closing
import pymysql

with closing(
    pymysql.connect(
        host="localhost",
        db="presidents",
        user="scripts",
        passwd="scripts",
    )
) as myconn:
    mycursor = myconn.cursor()

    # select specified columns from all presidents
    row_count = mycursor.execute("""
    SELECT termnum, firstname, lastname, party
    FROM presidents
    """)  # execute a SQL statement

    print(f"{row_count} rows in result set\n")

    for term, firstname, lastname, party in mycursor.fetchall():
        print(f"{term:2d} {firstname:25} {lastname:20} {party}")
    print()
