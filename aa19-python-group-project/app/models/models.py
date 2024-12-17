from .db import db, environment, SCHEMA, add_prefix_for_prod
from flask_login import UserMixin
from sqlalchemy.orm import relationship

class Song(db.Model):
    __tablename__ = 'songs'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    artist = db.Column(db.String(255), nullable=False)
    released_date = db.Column(db.Date, nullable=False)
    created_at = db.Column(db.Date)
    album_id = db.Column(db.Integer, db.ForeignKey('albums.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    lyrics = db.Column(db.String(50000))

    user = relationship("User", back_populates="songs")
    album = relationship("Album", back_populates="songs")
    playlist = relationship("Playlist", back_populates="songs")
    likes = relationship("Like", back_populates="songs")
    image = relationship("Image", back_populates="songs")

class Playlist(db.Model):
    __tablename__ = 'playlists'

    id = db.Column(db.Integer, primary_key=True)
    user_id= db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.Date)
    updated_at = db.Column(db.Date)

    user = relationship("User", back_populates="playlists")
    song = relationship("Song", back_populates="playlists")


class Like(db.Model):
    __tablename__ = 'likes'

    id = db.Column(db.Integer, primary_key=True)
    user_id= db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    song_id = db.Column(db.Integer, db.ForeignKey("songs.id"), nullable=False)
    album_id = db.Column(db.Integer,db.ForeignKey("albums.id"), nullable=False)
    created_at = db.Column(db.Date)

    album = relationship("Album", back_populates="likes")
    song = relationship("Song", back_populates="likes")
    user = relationship("User", back_populates="likes")


class Album(db.Model):
    __tablename__ = 'albums'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    artist = db.Column(db.String(255), nullable=False)
    released_year = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.Date)
    song_id = db.Column(db.Integer, db.ForeignKey('songs.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    playlist_id = db.Column(db.Integer, db.ForeignKey('playlists.id'), nullable=False)

    likes = relationship("Like", back_populates="albums")
    song = relationship("Song", back_populates="albums")



class Image(db.Model):
    __tablename__ = 'images'

    id = db.Column(db.Integer, primary_key=True)
    song_id = db.Column(db.Integer, db.ForeignKey('songs.id'), nullable=False)
    album_id = db.Column(db.Integer, db.ForeignKey('albums.id'), nullable=False)
    url = db.Column(db.String(1000), nullable=False)


    song = relationship("Song", back_populates="images")
    album = relationship("Album", back_populates="images")

class Playlist_song(db.Model):
    __tablename__ = 'playlist_songs'

    id = db.Column(db.Integer, primary_key=True)
    song_id = db.Column(db.Integer, db.ForeignKey('songs.id'), nullable=False)
    playlist_id = db.Column(db.Integer, db.ForeignKey('playlist.id'), nullable=False)

