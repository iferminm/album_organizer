#coding=utf-8
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from sqlalchemy.orm import relationship, backref
Base = declarative_base()

album_song_association = Table('album_song', Base.metadata,
    Column('album_id', Integer, ForeignKey('albums.id')),
    Column('song_id', Integer, ForeignKey('songs.id'))
)

artist_album_association = Table('artist_album', Base.metadata,
    Column('artist_id', Integer, ForeignKey('artists.id')),
    Column('album_id', Integer, ForeignKey('albums.id'))
)


class Country(Base):
    """docstring for Country"""
    __tablename__ = 'countries'
    id = Column(Integer, Sequence('country_id_sequence'), primary_key=True)
    name = Column(String(64))
    artists = relationship('Artist', backref='country')

    def __repr__(self):
        return '<Country {0}>'.format(self.name)


class Artist(Base):
    """
    
    """
    __tablename__ = 'artists'

    id = Column(Integer, Sequence('artist_id_sequence'), primary_key=True)
    name = Column(String(128))
    genre = Column(String(64))
    bio = Column(String(3500))
    country_id = Column(Integer, ForeignKey('countries.id'))
    albums = relationship('Album', secondary=artist_album_association, backref='artists')

    def __repr__(self):
        return '<Artist {0} {1}>'.format(self.name, self.genre)


class Album(Base):
    """
    docstring for Album
    """
    __tablename__ = 'albums'

    id = Column(Integer, Sequence('album_id_sequence'), primary_key=True)
    name = Column(String(256))
    year = Column(Integer)
    producer = Column(String(100))
    songs = relationship('Song', secondary=album_song_association, backref='albums')

    def __repr__(self):
        return '<Album {0}>'.format(self.name)


class Song(Base):
    """
    docstring for Song
    """
    __tablename__ = 'songs'

    id = Column(Integer, Sequence('song_id_sequence'), primary_key=True)
    name = Column(String(100))
    duration = Column(Integer)

    def __repr__(self):
        return '<Song {0}>'.format(self.name)


