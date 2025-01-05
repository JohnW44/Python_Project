from app.models import db, Image
from sqlalchemy.sql import text
# from datetime import datetime
from app.models.db import environment, SCHEMA

def seed_images():
    image1 = Image(
        url="https://melody-images.s3.us-east-1.amazonaws.com/7eb32ce387784b559195335eceb290f0.png",
        album_id=album1.id,
        song_id=1 
    )
    
    image2 = Image(
        url="https://cdn-p.smehost.net/sites/35faef12c1b64b21b3fda052d205af13/wp-content/uploads/2023/02/230222-daftpunk-ram10.jpg",
        album_id=album2.id,
        song_id=2
    )

    db.session.add(image1)
    db.session.add(image2)
    db.session.commit()

def undo_images():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.images RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM images"))
        
    db.session.commit()