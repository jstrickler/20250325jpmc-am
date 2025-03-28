'''
Create a movie database (only run this once!)
'''
from sqlalchemy import create_engine
from sa_movie_models import MOVIE_BASE


def main():
    engine = create_engine(
        'sqlite:///../DATA/movies.db',
        echo=False
    )
    MOVIE_BASE.metadata.create_all(engine)


if __name__ == '__main__':
    main()
