from flask import Blueprint, jsonify
from app.models import Album 
from app import db  

# use this to cross models to_dict methods
from sqlalchemy.orm import joinedload

albums_routes = Blueprint('albums_routes', __name__)

@albums_routes.route('/', methods=['GET'])
def albums():
    """
    Query for all albums and return them in a list of album dictionaries.
    """
    # joinedload overrides so you can get 2models data
    albums = Album.query.options(joinedload(Album.images)).all() 
    return jsonify({'Albums': [album.to_dict() for album in albums]})