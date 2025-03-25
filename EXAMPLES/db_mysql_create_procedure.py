from contextlib import closing
import pymysql

# pymysql can't execute multiple statements, so we execute one at a time
sql_statements = [
    """DROP PROCEDURE IF EXISTS `pres_full_name`;""",
    """
    CREATE PROCEDURE pres_full_name (IN term_num int)
    BEGIN
      select concat(firstname, ' ', lastname)
      from presidents
      where termnum = term_num;
    END
    """,
]

with closing(
    pymysql.connect(
        host="localhost",
        db="presidents",
        user="scripts",
        passwd="scripts",
    )
) as my_conn:
    my_cursor = my_conn.cursor()

    for sql_statement in sql_statements:
        my_cursor.execute(sql_statement)
