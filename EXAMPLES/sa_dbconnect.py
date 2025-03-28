from sqlalchemy import create_engine

engine = create_engine(
    'sqlite:///../DATA/presidents.db',
    echo=False
)

# windows: sqlite:///c:\\somewhere\mydatabase.db

conn = engine.connect()

s = conn.execute('select * from presidents where termnum = 16')

row = s.fetchone()

print(row.lastname)
