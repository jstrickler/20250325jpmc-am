from datetime import date
import ibm_db_dbi as db2

conn = db2.connect("DATABASE=testdb;HOSTNAME=localhost;PORT=50000;PROTOCOL=TCPIP;UID=db2inst1;PWD=scripts;", "", "")

sql_insert = """
insert into presidents 
(TERMNUM, LASTNAME, FIRSTNAME, BIRTHDATE, DEATHDATE, BIRTHPLACE, BIRTHSTATE, TERMSTART, TERMEND, PARTY)
values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?) 
"""

cursor = conn.cursor()

new_row_data = [47, 'Ramirez', 'Mary', date(1968, 9, 22), None,
                'Topeka', 'Kansas', date(2025, 1, 20), None, 'Independent']

try:
    cursor.execute(sql_insert, new_row_data)
except (db2.DatabaseError, db2.OperationalError, db2.DataError) as err:
    print(err)
    conn.rollback()
else:
    conn.commit()

cursor.close()
conn.close()
