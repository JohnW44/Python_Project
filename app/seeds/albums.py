from app.models import db, Album, Image
from sqlalchemy.sql import text
from datetime import datetime
from app.models.db import environment, SCHEMA

def seed_albums():
    album1 = Album( 
            title='Discovery',
            artist='Daft Punk',
            released_year=2001,
            created_at=datetime.now(),
            user_id=1,
            duration=4464
            )
    album2 = Album( 
            title='Views',
            artist='Drake',
            released_year=2016,
            created_at=datetime.now(),
            user_id=1,
            duration=4000
            )
    album3 = Album( 
            title='My Beautiful Dark Twisted Fantasy',
            artist='Kanye',
            released_year=2010,
            created_at=datetime.now(),
            user_id=1,
            duration=3500
            )
    db.session.add(album1)
    db.session.add(album2)
    db.session.add(album3)
    db.session.commit()


    # image1 = Image(
    #     url="https://cdn-p.smehost.net/sites/35faef12c1b64b21b3fda052d205af13/wp-content/uploads/2023/02/230222-daftpunk-ram10.jpg",
    #     album_id=album1.id,
    #     song_id=1 
    # )
    
    # image2 = Image(
    #     url="https://cdn-p.smehost.net/sites/35faef12c1b64b21b3fda052d205af13/wp-content/uploads/2023/02/230222-daftpunk-ram10.jpg",
    #     album_id=album2.id,
    #     song_id=2
    # )

    # db.session.add(image1)
    # db.session.add(image2)
    # db.session.commit()
    
def undo_albums():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.albums RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM albums"))
        
    db.session.commit()
        
  