import sys

from sqlalchemy import create_engine, select
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey


def read_knights():
    with open('../DATA/knights.txt') as knights_in:
        knight_list = []
        for line in knights_in:
            (name, title, color, quest, cmt) = line[:-1].split(":")
            knight_info = dict(
                name=name, title=title, color=color, quest=quest, comment=cmt
            )
            knight_list.append(knight_info)
    return knight_list


engine = create_engine(
    'sqlite:///../DATA/knights.db',
    echo=False
)

metadata = MetaData(bind=engine)

knights = Table(
    'knights',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(32)),
    Column('quest', String(32)),
    Column('color', String(16)),
    Column('title_id', None, ForeignKey('titles.id'))
)

titles = Table(
    'titles',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('title', String(32)),
)

# build the database
metadata.create_all()

conn = engine.connect()

for knight in read_knights():
    s = titles.select(titles.c.title == knight['title'])
    result = s.execute()
    row = result.fetchone()
    if row is None:
        ins_title = titles.insert().values(title=knight['title'])
        result = conn.execute(ins_title)
        new_title_id = result.inserted_primary_key[0]
    else:
        new_title_id = row.get_id

    s = knights.select(knights.c.name == knight['name'])
    result = s.execute()
    row = result.fetchone()
    if row is None:
        ins_knight = knights.insert().values(
            name=knight['name'],
            quest=knight['quest'],
            color=knight['color'],
            title_id=new_title_id
        )
        ins_knight.execute()

s = select([titles.c.title, knights.c.name], knights.c.title_id == titles.c.get_id)

result = conn.execute(s)

for title, name in result:
    print(f"{title} {name}")
