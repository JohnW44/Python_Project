from flask import Blueprint, jsonify, request
from app.models import Song, Image
from flask_login import login_required, current_user
from datetime import datetime
from app import db  




songs_routes = Blueprint('songs_routes', __name__)




@songs_routes.route('/', methods=['GET'])
def songs():
    """
    Query for all songs and return them in a list of song dictionaries.
    """
    songs = Song.query.all()
    return jsonify({'Songs': [song.to_dict() for song in songs]})




@songs_routes.route('/<int:songId>', methods=['GET'])
def song_details(songId):
    """
    Query to return details of a song specified by id
    """
    song = Song.query.get(songId)
    if song is None:
        return jsonify({"error": "Song couldn't be found"}), 404
    return jsonify(song.to_dict())
#missing Likes


@songs_routes.route('/', methods=['POST'])
@login_required
def add_song():
    """
    Adds and Returns a new song when a user is signed in
    """
    data = request.json


    if not data.get('Songs'):
        return jsonify({ "message": "Bad Request"}), 400


    song_data = data['Songs'][0]
    song_data['user_id'] = current_user.id
    song_data['released_date'] = datetime.strptime(song_data['released_date'], '%Y-%m-%d').date()
   
    new_song = Song(**song_data)


    db.session.add(new_song)
    db.session.commit()


   
    if data.get('Images'):
        new_image = Image(
            song_id=new_song.id,
            album_id=song_data['album_id'],
            url=data['Images'][0]['url']
        )
        db.session.add(new_image)
        db.session.commit()
    return jsonify({'Songs': new_song.to_dict()}), 201




@songs_routes.route('/<int:songId>', methods=['PUT'])
@login_required
def update_song(songId):
    """
    Updates and returns a song uploaded by user
    """
    data = request.json


    song = Song.query.get(songId)
    if not song:
            return jsonify({"error": "Song couldn't be found"}), 404
    if song.user_id != current_user.id:
            return jsonify({"error": "Unauthorized"}), 403
    if not data.get('Songs'):
            return jsonify({"message": "Bad Request"}), 400
   
    song_data = data['Songs'][0]


    song.title = song_data['title']
    song.artist = song_data['artist']
    song.released_date = datetime.strptime(song_data['released_date'], '%Y-%m-%d').date()
    song.album_id = song_data['album_id']
    song.lyrics = song_data['lyrics']
    if data.get('Images'):
        existing_image = Image.query.filter_by(song_id=songId).first()
        if existing_image:
            db.session.delete(existing_image)


        new_image = Image(
            song_id=songId,
            album_id=song_data['album_id'],
            url=data['Images'][0]['url']
        )
        db.session.add(new_image)
       
    db.session.commit()
    return jsonify({'Songs': song.to_dict()}), 200


@songs_routes.route('/<int:songId>', methods=['DELETE'])
@login_required
def delete_song(songId):
     """
     Deletes a users song by songId
     """
     song = Song.query.get(songId)
     if not song:
          return jsonify({"message" : "Song couldn't be found"}), 404
     if song.user_id != current_user.id:
          return jsonify({"message" : "Unauthorized"}), 403
     db.session.delete(song)
     db.session.commit()
     return jsonify({"message" : "Song Successfully deleted"})
   

