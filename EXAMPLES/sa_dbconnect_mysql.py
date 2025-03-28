from sqlalchemy import create_engine

engine = create_engine(
    'mysql+pymysql://presidents',
    echo=False
)

conn = engine.connect()

s = conn.execute('select * from presidents where termnum = 16')

row = s.fetchone()

print(row.lastname)
