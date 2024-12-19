from app.models import db, Song
from sqlalchemy.sql import text
from datetime import datetime, date
from app.models.db import environment, SCHEMA


def seed_songs():
    song1 = Song(
            title = "first song",
            artist = "Daft Punk2",
            released_date = date(2013, 1, 1),
            created_at = datetime.now(),
            album_id = 1,
            user_id = 1,
            duration = 400,
            lyrics = "brbrr brrr brrr"
            )
    song2 = Song(
            title = "second song",
            artist = "Daft Punk3",
            released_date = date(2013, 2, 1),
            created_at = datetime.now(),
            album_id = 1,
            user_id = 1,
            duration = 450,
            lyrics = "brbrr gadgaegaegabrrr brrr"
            )
    song3 = Song(
            title = "Electric Dreams",
            artist = "Daft Punk",
            released_date = date(2013, 5, 12),
            created_at = datetime.now(),
            album_id = 2,
            user_id = 1,
            duration = 420,
            lyrics = "electric dreams, they are coming for me"
            )
    song4 = Song(
            title = "Digital Love",
            artist = "Daft Punk",
            released_date = date(2001, 3, 12),
            created_at = datetime.now(),
            album_id = 3,
            user_id = 2,
            duration = 240,
            lyrics = "one more time, digital love, your love"
            )
    song5 = Song(
            title = "Harder, Better, Faster, Stronger",
            artist = "Daft Punk",
            released_date = date(2001, 5, 21),
            created_at = datetime.now(),
            album_id = 3,
            user_id = 3,
            duration = 280,
            lyrics = "work it, make it, do it, makes us harder, better, faster, stronger"
            )
    song6 = Song(
            title = "Around the World",
            artist = "Daft Punk",
            released_date = date(1997, 10, 12),
            created_at = datetime.now(),
            album_id = 1,
            user_id = 1,
            duration = 320,
            lyrics = "around the world, around the world"
            )
    song7 = Song(
            title = "One More Time",
            artist = "Daft Punk",
            released_date = date(2000, 11, 12),
            created_at = datetime.now(),
            album_id = None,
            user_id = 1,
            duration = 330,
            lyrics = "one more time, we're gonna celebrate, oh yeah, alright"
            )
    song8 = Song(
            title = "Technologic",
            artist = "Daft Punk",
            released_date = date(2005, 5, 17),
            created_at = datetime.now(),
            album_id = None,
            user_id = 1,
            duration = 200,
            lyrics = "buy it, use it, break it, fix it, trash it, change it, mail, upgrade it"
            )

    
    db.session.add(song1)
    db.session.add(song2)
    db.session.add(song3)
    db.session.add(song4)
    db.session.add(song5)
    db.session.add(song6)
    db.session.add(song7)
    db.session.add(song8)
    db.session.commit()

def undo_songs():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.songs RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM songs"))
        
    db.session.commit()
        