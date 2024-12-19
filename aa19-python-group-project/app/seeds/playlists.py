from app.models import db, Playlist
from sqlalchemy.sql import text
from datetime import datetime
from app.models import environment, SCHEMA

def seed_playlists():
    playlist = Playlist(
        user_id = 2,
        name = "testing playlist",
        created_at = datetime.now(),

    )

    playlist2 = Playlist(
        user_id = 2,
        name = "testing playlist2",
        created_at = datetime.now(),
    )


    db.session.add(playlist)
    db.session.add(playlist2)
    db.session.commit()


def undo_playlist():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.playlists RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM playlists"))

    db.session.commit()
