from app.models import db, Image
from sqlalchemy.sql import text
# from datetime import datetime
from app.models.db import environment, SCHEMA

def seed_images():
    image1 = Image(
        url="https://melody-images.s3.amazonaws.com/894af893cf264901abeed04663974000.jpeg",
        album_id=1,
    )
    image1 = Image(
        url="https://melody-images.s3.amazonaws.com/894af893cf264901abeed04663974000.jpeg",
        song_id=1
    )
    image2 = Image(
        url="https://melody-images.s3.amazonaws.com/894af893cf264901abeed04663974000.jpeg",
        song_id=2
    )
    image3 = Image(
        url="https://melody-images.s3.amazonaws.com/894af893cf264901abeed04663974000.jpeg",
        song_id=3
    )
    # drake
    image4 = Image(
        url="https://melody-images.s3.amazonaws.com/8659ae218b594484b2759c88bc3122f8.jpeg",
        album_id=2,
    )
    image4 = Image(
        url="https://melody-images.s3.amazonaws.com/8659ae218b594484b2759c88bc3122f8.jpeg",
        song_id=4,
    )
    image5 = Image(
        url="https://melody-images.s3.amazonaws.com/8659ae218b594484b2759c88bc3122f8.jpeg",
        song_id=5,
    )
    image6 = Image(
        url="https://melody-images.s3.amazonaws.com/8659ae218b594484b2759c88bc3122f8.jpeg",
        song_id=6,
    )
    # kanye
    image7 = Image(
        url="https://melody-images.s3.us-east-1.amazonaws.com/b782dc5135aa4bb58259a811cfdd8139.jpeg",
        album_id=3,
    )
    image7 = Image(
        url="https://melody-images.s3.us-east-1.amazonaws.com/b782dc5135aa4bb58259a811cfdd8139.jpeg",
        song_id=7,
    )
    image8 = Image(
        url="https://melody-images.s3.us-east-1.amazonaws.com/b782dc5135aa4bb58259a811cfdd8139.jpeg",
        song_id=8,
    )

    
    db.session.add(image1)
    db.session.add(image2)
    db.session.add(image3)
    db.session.add(image4)
    db.session.add(image5)
    db.session.add(image6)
    db.session.add(image7)
    db.session.add(image8)
    db.session.commit()

def undo_images():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.images RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM images"))
        
    db.session.commit()