import pymssql  #  pip install pymssql

conn = pymssql.connect(
    host="host",
    db="database",
    user="username",
    passwd="l0lz"
)

cursor = conn.cursor()

# select first name, last name from all presidents
row_count = cursor.execute('''
    select lname, fname
    from presidents
''')

print(f"{row_count} rows in result set\n")

for row in cursor.fetchall():
    print(' '.join(row))
print()

# cursor.fetchone() and cursor.fetchmany() are also available
