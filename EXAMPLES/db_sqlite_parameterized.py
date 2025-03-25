import sqlite3

TERMS_TO_UPDATE = [1, 5, 19, 22, 36]

PARTY_UPDATE = '''
update presidents 
set party = "SURPRISE!"
where termnum = ?
'''  # ? is SQLite3 placeholder for SQL statement parameter; different DBMSs use different placeholders

PARTY_QUERY = """
select termnum, firstname, lastname, party
from presidents
where termnum = ?
"""

with sqlite3.connect("../DATA/presidents.db") as s3conn:
    s3cursor = s3conn.cursor()

    for termnum in TERMS_TO_UPDATE:
        s3cursor.execute(PARTY_UPDATE, [termnum])  # second argument to execute() is iterable of values to fill in placeholders from left to right

    s3conn.commit()

    for termnum in TERMS_TO_UPDATE:
        s3cursor.execute(PARTY_QUERY, [termnum])
        print(s3cursor.fetchone())