from flask import Blueprint, jsonify, request
from app.models import Album , Song
from app import db  
from flask_login import current_user, login_required

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

@albums_routes.route('users/<userId>', methods =['GET'])
@login_required
def my_albums(userId):
    """
    Query for all albums and return the albums owned by current user.
    """

    if current_user.is_authenticated:
        user_albums=  Album.query.filter_by(user_id=userId).options(joinedload(Album.songs)).all()
        
        if not user_albums:
            return jsonify({"message": "User has no Albums"}),404
        
        return jsonify({'Albums': [album.to_dict() for album in user_albums]})

    return jsonify({"error": "Unauthorized access"}), 401

@albums_routes.route('/<albumId>/<userId>/songs', methods=['POST'])
@login_required
def add_song_to_album(albumId, userId):
    """
    Find album and then add song to album owned by current user, only possible if song isnt already in another album.
    """

    if not current_user.is_authenticated:
        return jsonify({"error": "Authentication required"}), 401
    
    album = Album.query.get(albumId)
    if not album:
        return jsonify({"message": "Album Not Found"}), 404
    
    if album.user_id != current_user.id:
        return jsonify({"message": "You must be owner of this album"}),402
    
    if album.user_id != int(userId):
        return jsonify({"message": "You must be owner of this album"}), 402
    
    song_data = request.json
    song_id= song_data.get('songid')

    song = Song.query.get(song_id)
    if not song:
        return jsonify({"message": "Song Not Found"}), 404
    
    # this checks if its already in another album
    existing_album = Album.query.join(Album.songs).filter(Song.id == song_id).first()
    if existing_album:
        return jsonify({"message": "Song is already in another album"}), 400
    
    album.songs.append(song)
    db.session.commit()

    return jsonify({
        "message": "Song successfully added to Album",
        'Album': [album.to_dict()]
        })
