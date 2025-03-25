"""
    Provide metadata (tables and column names) for a Sqlite3 database
"""
from pprint import pprint
import sqlite3

DB_NAME = "../DATA/presidents.db"
TABLE_QUERY = '''select * from presidents where 1 = 2'''

def main():
    cursor = connect_to_db(DB_NAME)
    show_metadata(cursor)

def connect_to_db(database_file):
    with sqlite3.connect(database_file) as s3conn:
        return s3conn.cursor()

def show_metadata(cursor):
    cursor.execute(TABLE_QUERY)
    pprint(cursor.description)
    print()
    column_names = [column_data[0] for column_data in cursor.description]
    print(f"{column_names = }")

if __name__ == '__main__':
    main()
