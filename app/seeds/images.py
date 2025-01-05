from app.models import db, Image
from sqlalchemy.sql import text
# from datetime import datetime
from app.models.db import environment, SCHEMA

def seed_images():
    image1 = Image(
        url="https://melody-images.s3.us-east-1.amazonaws.com/1a358c22eccd4c98bc81cd1f9fbe1986.jpg",
        album_id=album1.id,
        song_id=1 
    )
    
    db.session.add(image1)
    db.session.commit()

def undo_images():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.images RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM images"))
        
    db.session.commit()