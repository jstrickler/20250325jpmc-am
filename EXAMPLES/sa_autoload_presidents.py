from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    'sqlite:///../DATA/presidents.db',
    echo=False
)

metadata = MetaData(bind=engine)

conn = engine.connect()

sm = sessionmaker(bind=engine)
session = sm()

pres = Table(
    'presidents',
    metadata,
    autoload=True,
)

q = session.query(pres).first()
print(q)
print(q.firstname)
print(q.lastname)

q = session.query(pres).filter_by(party='Republican').first()
print(q, '\n')

q = session.query(pres).all()

print(q[:3], '\n')  # first 3 rows

for row in q:
    print(row)
