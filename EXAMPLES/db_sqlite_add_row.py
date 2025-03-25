from datetime import date
import sqlite3


with sqlite3.connect("../DATA/presidents.db") as s3conn:  # connect to database

    sql_insert = """
    insert into presidents 
    (termnum, lastname, firstname, termstart, termend, birthplace, birthstate, birthdate, deathdate,  party)
    values (47, 'Ramirez', 'Mary', '2025-01-20', null, 'Topeka', 
    'Kansas', '1968-09-22', null, 'Independent') 
    """

    cursor = s3conn.cursor()

    try:
        cursor.execute(sql_insert)
    except (sqlite3.OperationalError, sqlite3.DatabaseError, sqlite3.DataError) as err:
        print(err)
        s3conn.rollback()
    else:
        s3conn.commit()
    finally:
        cursor.close()
