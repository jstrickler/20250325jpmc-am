'''
Define Director and Movie models (objects)
'''
from sqlalchemy import (
    Column, Integer, String, ForeignKey
)
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

MOVIE_BASE = declarative_base()


class Director(MOVIE_BASE):
    '''A film director.'''
    __tablename__ = 'Director'
    id = Column(Integer, primary_key=True)
    last_name = Column(String(50))
    first_name = Column(String(50))

    movies = relationship(
        "Movie",
        order_by="Movie.year",
        backref="Director"
    )

    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name

    def __repr__(self):
        return f"<Director ({self.first_name} {self.last_name})>"


class Movie(MOVIE_BASE):
    '''A Movie'''
    __tablename__ = 'Movie'
    id = Column(Integer, primary_key=True)
    movie_name = Column(String(100), nullable=False)
    year = Column(Integer, nullable=False)
    director_id = Column(Integer, ForeignKey('Director.id'))
    person = relationship("Director", backref=backref('Movie'))

    def __init__(self, movie_name, year):
        self.movie_name = movie_name
        self.year = year

    def __repr__(self):
        return f"<Movie {self.movie_name} ({self.year})>"
