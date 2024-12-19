from flask import Blueprint, jsonify
from app.models import Album , Song
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

@albums_routes.route('/<albumId>/songs', methods=['GET'])
def songs_in_album(albumId):
    """
    Query for all albums and return the songs in a list of dictoinaires.
    """
    album = Album.query.options(joinedload(Album.songs)).get(albumId)

    if not album:
        return jsonify({"message": "No Album found"}),404

    return jsonify({"Songs": [song.to_dict() for song in album.songs]})