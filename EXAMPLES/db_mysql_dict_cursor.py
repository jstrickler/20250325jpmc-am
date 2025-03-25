import pymysql
import pymysql.cursors

myconn = pymysql.connect(
    host="localhost",
    db="presidents",
    user="scripts",
    passwd="scripts",
    cursorclass=pymysql.cursors.DictCursor
)

# c = myconn.cursor(pymysql.cursors.DictCursor)
c = myconn.cursor()

# select first name, last name from all presidents
num_recs = c.execute('''
    select lastname, firstname
    from presidents
''')

print(c.description)

for row in c.fetchall():
    print(row['firstname'], row['lastname'])
print()


