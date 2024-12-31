from app.models import db, Song
from sqlalchemy.sql import text
from datetime import datetime, date
from app.models.db import environment, SCHEMA


def seed_songs():
    song1 = Song(
            title = "One more time",
            artist = "Daft Punk",
            released_date = date(2013, 1, 1),
            created_at = datetime.now(),
            album_id = 1,
            user_id = 1,
            duration = 400,
            lyrics = "brbrr brrr brrr",
            link = "https://www.youtube.com/watch?v=FGBhQbmPwH8&pp=ygUNb25lIG1vcmUgdGltZQ%3D%3D"
            )
    song2 = Song(
            title = "Harder, Better, Faster, Stronger",
            artist = "Daft Punk",
            released_date = date(2013, 2, 1),
            created_at = datetime.now(),
            album_id = 1,
            user_id = 1,
            duration = 450,
            lyrics = "brbrr gadgaegaegabrrr brrr",
            link = "https://www.youtube.com/watch?v=gAjR4_CbPpQ&pp=ygUnZGFmdCBwdW5rIGhhcmRlciBiZXR0ZXIgZmFzdGVyIHN0cm9uZ2Vy"
            )
    db.session.add(song1)
    db.session.add(song2)
    db.session.commit()

def undo_songs():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.songs RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM songs"))
        
    db.session.commit()
        