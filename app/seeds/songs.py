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
            duration = 313,
            lyrics = """Strangers, from strangers into brothers
From brothers into strangers once again
We saw the whole world
But I couldn't see the meaning
I couldn't even recognize my friends
Older, but nothing's any different
Right now feels the same, I wonder why
I wish they told us
It shouldn't take a sickness
Or airplanes falling out the sky
Do I have to die to hear you miss me?
Do I have to die to hear you say goodbye?
I don't wanna act like there's tomorrow
I don't wanna wait to do this one more time
One more time
One more
One more time
One more time
I miss you, took time but I admit it
It still hurts even after all these years
And I know that next time, ain't always gonna happen
I gotta say, "I love you" while we're here
Do I have to die to hear you miss me?
Do I have to die to hear you say goodbye?
I don't wanna act like there's tomorrow
I don't wanna wait to do this one more time
One more time
One more
One more time
One more time
One more time
One more time
One more
One more time
One more time
One more time
I miss you""",
            audio_file = "https://melody-songs.s3.us-east-1.amazonaws.com/07a9740ea7754e2292a349e8d6932620.mp3"
            )
    db.session.add(song1)
    db.session.commit()

def undo_songs():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.songs RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM songs"))
        
    db.session.commit()
        