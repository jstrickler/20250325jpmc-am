from collections import namedtuple
import sqlite3


def named_tuple_cursor(cursor):
    '''Generate rows as named tuples'''
    column_names = [desc[0] for desc in cursor.description]
    name_str = ' '.join(column_names)
    # "row_tuple" is an arbitrary name -- any name could be used here
    row_tuple = namedtuple('row_tuple', name_str)

    for cursor_row in cursor.fetchall():
        row_tuple = row_tuple(*cursor_row)
        yield row_tuple


with sqlite3.connect("../DATA/presidents.db") as s3conn:
    c = s3conn.cursor()

    # select first name, last name from all presidents
    num_recs = c.execute('''
        select firstname, lastname
        from presidents
    ''')

    for row in named_tuple_cursor(c):
        print(row.firstname, row.lastname)
