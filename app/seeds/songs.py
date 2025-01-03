from app.models import db, Song
from sqlalchemy.sql import text
from datetime import datetime, date
from app.models.db import environment, SCHEMA

audio_path = '../audio/audio.mp3'

def seed_songs():
    song1 = Song(
            title = "first song",
            artist = "Daft Punk2",
            released_date = date(2013, 1, 1),
            created_at = datetime.now(),
            album_id = 1,
            user_id = 1,
            duration = 400,
            lyrics = "brbrr brrr brrr",
            audio_file = audio_path
            )
    # song2 = Song(
    #         title = "second song",
    #         artist = "Daft Punk3",
    #         released_date = date(2013, 2, 1),
    #         created_at = datetime.now(),
    #         album_id = 1,
    #         user_id = 1,
    #         duration = 450,
    #         lyrics = "brbrr gadgaegaegabrrr brrr"
    #         )
    db.session.add(song1)
    # db.session.add(song2)
    # db.session.add()
    db.session.commit()

def undo_songs():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.songs RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM songs"))
        
    db.session.commit()
        