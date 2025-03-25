import pymysql
import pymysql.cursors

myconn = pymysql.connect(
    host="localhost",
    db="presidents",
    user="scripts",
    passwd="scripts",
    cursorclass=pymysql.cursors.DictCursor
)

c = myconn.cursor()

# call a stored proc two different ways

cur = myconn.cursor(pymysql.cursors.Cursor)

cur.execute('call pres_full_name(16)')
print(cur.fetchone())

cur.callproc('pres_full_name', (16,))
print(cur.fetchone())

myconn.close()
