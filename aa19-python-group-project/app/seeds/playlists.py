from app.models import db, Playlist, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import datetime


def seed_playlists():
    playlist1 = Playlist(
        playlist_id = 1,
        user_id = 1,
        name = "Top Hits"
    )
    playlist2 = Playlist(
        playlist_id = 2,
        user_id = 2,
        name = "Chill Vibes"
    )
    playlist3 = Playlist(
        playlist_id = 3,
        user_id = 2,
        name = "Workout Tunes"
    )
    db.session.add(playlist1)
    db.session.add(playlist2)
    db.session.add(playlist3)
    db.session.commit()

def undo_playlist():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.playlists RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM playlists"))

    db.session.commit()
