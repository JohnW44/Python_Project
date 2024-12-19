from .db import db, environment, SCHEMA, add_prefix_for_prod
from flask_login import UserMixin
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .user import User


class Song(db.Model):
    __tablename__ = 'songs'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    artist = db.Column(db.String(255), nullable=False)
    released_date = db.Column(db.Date, nullable=False)
    created_at = db.Column( db.DateTime, nullable=False, server_default=func.now())
    album_id = db.Column(db.Integer, db.ForeignKey('albums.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    lyrics = db.Column(db.String(50000))

    users = relationship("User", back_populates="songs")
    albums = relationship("Album", back_populates="songs")
    playlist_songs = relationship("PlaylistSong", back_populates="songs")
    likes = relationship("Like", back_populates="songs")
    images = relationship("Image", back_populates="songs")

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
            "lyrics": self.lyrics
        }

class Playlist(db.Model):
    __tablename__ = 'playlists'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id= db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, server_default=func.now())
    updated_at = db.Column(db.DateTime, onupdate=func.now())

    users = relationship("User", back_populates="playlists")
    playlist_songs = relationship("PlaylistSong", back_populates="playlists", cascade="all, delete-orphan")

    def to_dict(self):
        return {
        "id": self.id,
        "user_id": self.user_id,
        "name": self.name,
        "created_at": self.created_at
         }


class Like(db.Model):
    __tablename__ = 'likes'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id= db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    song_id = db.Column(db.Integer, db.ForeignKey("songs.id"), nullable=False)
    album_id = db.Column(db.Integer,db.ForeignKey("albums.id"), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, server_default=func.now())

    albums = relationship("Album", back_populates="likes")
    songs = relationship("Song", back_populates="likes")
    users = relationship("User", back_populates="likes")


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
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    duration = db.Column(db.Integer, nullable=False)

    users = relationship("User", back_populates="albums")
    likes = relationship("Like", back_populates="albums")
    songs = relationship("Song", back_populates="albums")
    images = relationship("Image", back_populates="albums")

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "artist": self.artist,
            "released_year":self.released_year,
            "created_at": self.created_at,
            "user_id": self.user_id,
            "duration": self.duration,
            "images": [image.to_dict() for image in self.images]
        }

class Image(db.Model):
    __tablename__ = 'images'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    song_id = db.Column(db.Integer, db.ForeignKey('songs.id'), nullable=False)
    album_id = db.Column(db.Integer, db.ForeignKey('albums.id'), nullable=False)
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

class PlaylistSong(db.Model):
    __tablename__ = 'playlist_songs'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    song_id = db.Column(db.Integer, db.ForeignKey('songs.id'), nullable=False)
    playlist_id = db.Column(db.Integer, db.ForeignKey('playlists.id'), nullable=False)
    added_at = db.Column(db.DateTime, default=func.now())

    songs = relationship("Song", back_populates="playlist_songs")
    playlists = relationship("Playlist", back_populates="playlist_songs")
