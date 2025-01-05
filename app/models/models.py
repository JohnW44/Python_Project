from .db import db, environment, SCHEMA, add_prefix_for_prod
from flask_login import UserMixin
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .user import User
from sqlalchemy import CheckConstraint
from datetime import datetime


class Song(db.Model):
    __tablename__ = 'songs'


    if environment == "production":
        __table_args__ = {'schema': SCHEMA}


    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    artist = db.Column(db.String(255), nullable=False)
    released_date = db.Column(db.Date, nullable=False)
    created_at = db.Column( db.DateTime, nullable=False, server_default=func.now())
    album_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('albums.id')), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    lyrics = db.Column(db.String(50000))
    audio_file = db.Column(db.String(500), nullable=False)


    users = relationship("User", back_populates="songs")
    albums = relationship("Album", back_populates="songs")
    playlist_songs = relationship("PlaylistSong", back_populates="songs")
    likes = relationship("Like", back_populates="songs", cascade="all, delete-orphan")
    images = relationship("Image", back_populates="songs", cascade="all, delete-orphan")


    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "artist": self.artist,
            "released_date":self.released_date,
            "created_at": self.created_at,
            "album_id": self.album_id,
            "user_id": self.user_id,
            "duration": self.duration,
            "lyrics": self.lyrics,
            "audio_file": self.audio_file,
            "likes": [like.to_dict() for like in self.likes],
            "images": [image.to_dict() for image in self.images]
        }




class Like(db.Model):
    __tablename__ = 'likes'

    if environment == "production":
        __table_args__ ={'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id= db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable=False)
    song_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("songs.id")), nullable=True)
    album_id = db.Column(db.Integer,db.ForeignKey(add_prefix_for_prod("albums.id")), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, server_default=func.now())

    albums = relationship("Album", back_populates="likes")
    songs = relationship("Song", back_populates="likes")
    users = relationship("User", back_populates="likes")

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "song_id": self.song_id,
            "album_id": self.album_id,
        }


class Album(db.Model):
    __tablename__ = 'albums'


    if environment == "production":
        __table_args__ = {'schema': SCHEMA}


    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    artist = db.Column(db.String(255), nullable=False)
    released_year = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, server_default=func.now())
    # song_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
   
    users = relationship("User", back_populates="albums")
    likes = relationship("Like", back_populates="albums", cascade="all, delete-orphan")
    songs = relationship("Song", back_populates="albums")
    images = relationship("Image", back_populates="albums", cascade="all, delete-orphan")


    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "artist": self.artist,
            "released_year":self.released_year,
            "created_at": self.created_at,
            "user_id": self.user_id,
            "duration": self.duration,
            "images": [image.to_dict() for image in self.images],
            "songs" :[song.to_dict() for song in self.songs]
        }


class Image(db.Model):
    __tablename__ = 'images'


    if environment == "production":
        __table_args__ = {'schema': SCHEMA}


    id = db.Column(db.Integer, primary_key=True)
    song_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('songs.id')), nullable=True, unique=True)
    album_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('albums.id')), nullable=True) #!Changed this to True for Image troubleshooting
    url = db.Column(db.String(1000), nullable=False)




    songs = relationship("Song", back_populates="images")
    albums = relationship("Album", back_populates="images")


    def to_dict(self):
        return {
            "id": self.id,
            "song_id": self.song_id,
            "album_id": self.album_id,
            "url": self.url
        }

class Playlist(db.Model):
    __tablename__ = 'playlists'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    playlist_id = db.Column(db.Integer, unique=True, nullable=False)
    user_id= db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    users = db.relationship('User', back_populates='playlists')
    songs = db.relationship('PlaylistSong', back_populates='playlist', cascade='all, delete-orphan')

    def to_dict(self):
        return {
        "id": self.id,
        "user_id": self.user_id,
        "name": self.name,
        "created_at": self.created_at,
        "updated_at": self.updated_at
         }

class PlaylistSong(db.Model):
    __tablename__ = 'playlist_songs'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    playlist_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('playlists.id')), nullable=False)  # ForeignKey to Playlist model
    song_name = db.Column(db.String(255), nullable=False)
    song_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('songs.id')), nullable=False)
    playlist = db.relationship('Playlist', back_populates='songs')
    songs = db.relationship("Song", back_populates="playlist_songs")

    def to_dict(self):
        return {
        "id": self.id,
        "playlist_id": self.playlist_id,
        "song_name": self.song_name,
         }
