from app.models import db, Album
from sqlalchemy.sql import text
from datetime import datetime

def seed_albums():
    album1 = Album( 
            title='Random Access Memories',
            artist='Daft Punk',
            release_year=(2013),
            images="https://cdn-p.smehost.net/sites/35faef12c1b64b21b3fda052d205af13/wp-content/uploads/2023/02/230222-daftpunk-ram10.jpg",
            created_at=datetime,
            user_id= 1,
            duration= 4464
            )
    album2 = Album( 
            title='album2',
            artist='Dafter Punk',
            release_year=(2013),
            images="https://cdn-p.smehost.net/sites/35faef12c1b64b21b3fda052d205af13/wp-content/uploads/2023/02/230222-daftpunk-ram10.jpg",
            created_at=datetime,
            user_id= 2,
            duration= 4464
            )
    
    db.session.add(album1)
    db.session.add(album2)
    db.session.commit()
    
        
        
  