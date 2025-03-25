import sqlite3

RESTORE_DATA = [
    (1, 'no party'),
    (5, 'Democratic - Republican'),
    (19, 'Republican'),
    (22, 'Democratic'),
    (36, 'Democratic')
]

PARTY_UPDATE = '''
update presidents 
set party = ?
where termnum = ?
'''  # ? is SQLite3 placeholder; other DBMSs may use other placeholders

PARTY_QUERY = """
select termnum, firstname, lastname, party
from presidents
where termnum = ?
"""

with sqlite3.connect("../DATA/presidents.db") as s3conn:
    s3cursor = s3conn.cursor()

    for termnum, party in RESTORE_DATA:
        s3cursor.execute(PARTY_UPDATE, [party, termnum])  # second argument to execute() is iterable of values to fill in placeholders from left to right
    s3conn.commit()

    for termnum, _ in RESTORE_DATA:
        s3cursor.execute(PARTY_QUERY, [termnum])
        print(s3cursor.fetchone())
