from sqlalchemy import create_engine
from sqlalchemy import Table, MetaData


engine = create_engine(
    'sqlite:///../DATA/presidents.db',
    echo=False
)

metadata = MetaData(bind=engine)

conn = engine.connect()

pres = Table(
    'presidents',
    metadata,
    autoload=True
)

# find Lincoln
s = pres.select(pres.c.termnum == 16)

results = s.execute()
for row in results:
    print(row.firstname, row.lastname, row.party)

print('-------------')
s = pres.select(pres.c.party == 'Republican')

for row in s.execute():
    full_name = f"{row.firstname} {row.lastname}"
    print(f"{full_name:28s} {row.termstart} {row.birthstate}")
