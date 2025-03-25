"""
Generic functions that can be used with any DB API compliant
package.

To use, pass in a cursor after execute()-ing a
SQL query. Then iterate over the generator that is
returned
"""
import psycopg
from db_iterrows import *

sql_select = """
SELECT firstname, lastname, party
FROM presidents
WHERE termnum > 39
"""

conn = psycopg.connect(
    host="localhost",
    dbname="postgres",
    user="postgres",
    password='scripts',
)
cursor = conn.cursor()

########################
# iterrows_asdict()
########################
cursor.execute(sql_select)

for row in iterrows_asdict(cursor):
    print(row['firstname'], row['lastname'], row['party'])

print('-' * 60)

########################
# iterrows_asnamedtuple()
########################

cursor.execute(sql_select)

for row in iterrows_asnamedtuple(cursor):
    print(row.firstname, row.lastname, row.party)

print('-' * 60)

########################
# iterrows_asdataclass()
########################

cursor.execute(sql_select)

for row in iterrows_asdataclass(cursor):
    print(row.firstname, row.lastname, row.party)

conn.close()
