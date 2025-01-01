from app.models import db, PlaylistSong, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import datetime


def seed_playlistSongs():
    song1 = PlaylistSong(
        playlist_id = 1,
        song_id = 7,
        song_name = 'Song 1 - Top Hits'
    )
    song2 = PlaylistSong(
        playlist_id = 1,
        song_id = 8,
        song_name = "Song 2 - Top Hits"
    )
    song3 = PlaylistSong(
        playlist_id = 2,
        song_id = 3,
        song_name = "Song 1 - Chill Vibes"
    )
    song4 = PlaylistSong(
        playlist_id = 2,
        song_id = 4,
        song_name = "Song 2 - Chill Vibes"
    )
    song5 = PlaylistSong(
        playlist_id = 3,
        song_id = 5,
        song_name = "Song 1 - Workout Tunes"
    )
    song6 = PlaylistSong(
        playlist_id = 3,
        song_id = 6,
        song_name = "Song 2 - Workout Tunes"
    )
    db.session.add(song1)
    db.session.add(song2)
    db.session.add(song3)
    db.session.add(song4)
    db.session.add(song5)
    db.session.add(song6)
    db.session.commit()



def undo_playlist_song():
    """Deletes all records from the playlist_songs table, truncating it in production."""
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.playlist_songs RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM playlist_songs"))

    db.session.commit()