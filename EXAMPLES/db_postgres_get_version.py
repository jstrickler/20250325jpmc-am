import psycopg

pg_conn = psycopg.connect(
    host="localhost",
    dbname="postgres",
    user="postgres",
    password='scripts',
)
pg_cursor = pg_conn.cursor()

# select first name, last name from all presidents
pg_cursor.execute('''
select version()
''')
print(pg_cursor.fetchone())

pg_cursor.execute("Select * from presidents where 1 = 2")
print(pg_cursor.description)

pg_conn.close()

