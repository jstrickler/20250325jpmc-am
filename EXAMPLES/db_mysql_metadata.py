from pprint import pprint
import pymysql

DB = 'presidents'
DB_HOST = 'localhost'
DB_USER = 'scripts'
DB_PASSWORD = 'scripts'

TABLE_QUERY = '''select * from presidents where 1 = 2'''

def main():
    cursor = connect_to_db()
    show_metadata(cursor)

def connect_to_db():
    conn = pymysql.connect(
        host=DB_HOST,
        db=DB,
        user=DB_USER,
        passwd=DB_PASSWORD
    )
    return conn.cursor()

def show_metadata(cursor):
    cursor.execute(TABLE_QUERY)
    pprint(cursor.description)
    print()
    column_names = [column_data[0] for column_data in cursor.description]
    print(f"{column_names = }")

if __name__ == '__main__':
    main()


