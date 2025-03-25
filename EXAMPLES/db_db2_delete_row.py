import ibm_db_dbi as db2

conn = db2.connect("DATABASE=testdb;HOSTNAME=localhost;PORT=50000;PROTOCOL=TCPIP;UID=db2inst1;PWD=scripts;", "", "")

sql_delete = """
delete from presidents
where TERMNUM = 47 
"""

cursor = conn.cursor()

try:
    cursor.execute(sql_delete)
except (db2.DatabaseError, db2.OperationalError, db2.DataError) as err:
    print(err)
    conn.rollback()
else:
    conn.commit()

cursor.close()
conn.close()
