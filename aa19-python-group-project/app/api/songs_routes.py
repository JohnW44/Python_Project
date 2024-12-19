from flask import Blueprint, jsonify, request
from app.models import Song, Image 
from flask_login import login_required, current_user
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


@songs_routes.route('/', methods=['POST'])
@login_required
def add_song():
    """
    Adds and Returns a new song when a user is signed in
    """
    song_data = request.json

    if not song_data.get('Songs'):
        return jsonify({ "message": "Bad Request"}), 400

    song_data = ['Songs'][0]
    song_data['user_id'] = current_user.id

    new_song = Song(**song_data)

    db.session.add(new_song)

    response = {'Songs': [new_song.to_dict()]}

    if song_data.get('Images'):
        new_image = Image(
            song_id=new_song.id,
            album_id=song_data['album_id'],
            url=song_data['Images'][0]['url']
        )
        db.session.add(new_image)
        response['Images'] = [{
            "id": new_image.id,
            "url": new_image.url
        }]
    db.session.commit()
    return jsonify(response), 201


