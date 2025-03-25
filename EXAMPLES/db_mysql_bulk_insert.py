import pymysql
import csv

DATA_FILE = '../DATA/fruit_data.csv'

DB_HOST = 'localhost'
DB_NAME = 'fruits'
DB_USER = 'scripts'
DB_PASSWORD = 'scripts'
DB_TABLE = 'fruits'

SQL_CREATE_DATABASE = f"""
create database if not exists {DB_NAME}
"""

SQL_DROP_TABLE = f"""
drop table if exists {DB_TABLE}
"""

SQL_CREATE_TABLE = f"""
create table {DB_TABLE} (
    id integer primary key auto_increment,
    name varchar(30),
    unit varchar(30),
    unitprice decimal(6, 2)
)
"""
SQL_USE_DATABASE = f"""use {DB_NAME}"""

SQL_INSERT_ROW = f'''
insert into {DB_TABLE} (name, unit, unitprice) values (%s, %s, %s)
'''  # parameterized SQL statement to insert one record

SQL_SELECT_ALL = f"""
select name, unit, unitprice from {DB_TABLE}
"""

def main():
    """
    Program entry point.

    :return: None
    """
    conn, cursor = get_connection()
    create_database_and_table(conn, cursor)
    populate_database(conn, cursor)
    read_database(cursor)

    cursor.close()
    conn.close()


def get_connection():
    """
    Get a connection to the PRODUCE database

    :return: SQLite3 connection object.
    """

    conn = pymysql.connect(
        host=DB_HOST,
        db='mysql',  # builtin database
        user=DB_USER,
        passwd=DB_PASSWORD,
    )
    cursor = conn.cursor()

    return conn, cursor



def create_database_and_table(conn, cursor):
    """
    Create the fruit table

    :param conn: The database connection
    :return: None
    """
    cursor.execute(SQL_CREATE_DATABASE)
    cursor.execute(SQL_USE_DATABASE)
    cursor.execute(SQL_DROP_TABLE)
    cursor.execute(SQL_CREATE_TABLE)
    conn.commit()


def populate_database(conn, cursor):
    """
    Add rows to the fruit table

    :param conn: The database connection
    :return: None
    """
    with open(DATA_FILE) as file_in:
        fruit_data = csv.reader(file_in, quoting=csv.QUOTE_NONNUMERIC)

        try:
            cursor.executemany(SQL_INSERT_ROW, fruit_data)  # iterate over fruit_data and
                                                            # and add each pair to database
        except pymysql.DatabaseError as err:
            print(err)
            conn.rollback()  # roll back changes to DB
        else:
            conn.commit()  # commit changes to DB

def read_database(cursor):
    cursor.execute(SQL_SELECT_ALL)
    for name, unit, unitprice in cursor.fetchall():
        print(f'{name:12s} {unitprice:5.2f}/{unit}')


if __name__ == '__main__':
    main()
