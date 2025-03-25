from contextlib import closing
from collections import namedtuple
import pymysql


def named_tuple_cursor(cursor):
    '''Generate rows as named tuple'''
    column_names = [desc[0] for desc in cursor.description]
    row_tuple = namedtuple('row_tuple', column_names)
    # "row_tuple" is internal name of row_tuple class
    for cursor_row in cursor.fetchall():
        yield row_tuple(*cursor_row)


with closing(pymysql.connect(
    host="localhost",
    db="presidents",
    user="scripts",
    passwd="scripts",
)) as myconn:
    c = myconn.cursor()

    # select first name, last name from all presidents
    num_recs = c.execute('''
        select lastname, firstname
        from presidents
    ''')

    for row in named_tuple_cursor(c):
        print(row.firstname, row.lastname)
