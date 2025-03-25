"""
Generic functions that can be used with any DB API compliant
package.

To use, pass in a cursor after execute()-ing a
SQL query. Then iterate over the generator that is
returned
"""
import ibm_db_dbi as db2
from db_iterrows import *

sql_select = """
SELECT firstname, lastname, party
FROM presidents
WHERE termnum > 39
"""

conn = db2.connect("DATABASE=testdb;HOSTNAME=localhost;PORT=50000;PROTOCOL=TCPIP;UID=db2inst1;PWD=scripts;", "", "")

cursor = conn.cursor()

########################
# iterrows_asdict()
########################
cursor.execute(sql_select)

for row in iterrows_asdict(cursor):
    print(row['FIRSTNAME'], row['LASTNAME'], row['PARTY'])

print('-' * 60)

########################
# iterrows_asnamedtuple()
########################

cursor.execute(sql_select)

for row in iterrows_asnamedtuple(cursor):
    print(row.FIRSTNAME, row.LASTNAME, row.PARTY)

print('-' * 60)

########################
# iterrows_asdataclass()
########################

cursor.execute(sql_select)

for row in iterrows_asdataclass(cursor):
    print(row.FIRSTNAME, row.LASTNAME, row.PARTY)

conn.close()
