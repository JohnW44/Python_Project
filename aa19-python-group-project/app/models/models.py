from .db import db, environment, SCHEMA, add_prefix_for_prod
from flask_login import UserMixin


class Song(db.Model):
    __tablename__ = 'songs'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    artist = db.Column(db.String(255), nullable=False)
    released_date = db.Column(db.Date, nullable=False)
    created_at = db.Column(db.Date)
    album_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    lyrics = db.Column(db.String(50000))


class Playlist(db.Model):
    __tablename__ = 'playlists'

    id = db.Column(db.Integer, primary_key=True)
    user_id= db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.Date)
    updated_at = db.Column(db.Date)


class Like(db.Model):
    __tablename__ = 'likes'

    id = db.Column(db.Integer, primary_key=True)
    user_id= db.Column(db.Integer, nullable=False)
    song_id = db.Column(db.Integer, nullable=False)
    album_id = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.Date)


class Album(db.Model):
    __tablename__ = 'albums'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    artist = db.Column(db.String(255), nullable=False)
    released_year = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.Date)
    song_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    playlist_id = db.Column(db.Integer, nullable=False)


class Image(db.Model):
    __tablename__ = 'images'

    id = db.Column(db.Integer, primary_key=True)
    song_id = db.Column(db.Integer, nullable=False)
    album_id = db.Column(db.Integer, nullable=False)
    url = db.Column(db.String(1000), nullable=False)


class Playlist_song(db.Model):
    __tablename__ = 'playlist_songs'

    id = db.Column(db.Integer, primary_key=True)
    song_id = db.Column(db.Integer, nullable=False)
    playlist_id = db.Column(db.Integer, nullable=False)
