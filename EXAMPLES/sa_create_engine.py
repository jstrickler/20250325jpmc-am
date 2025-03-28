from sqlalchemy import create_engine

# for SQLite3:

engine = create_engine(
    'sqlite:///../DATA/presidents.db',
    echo=False
)

print(engine)
