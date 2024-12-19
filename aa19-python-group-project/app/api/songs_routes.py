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
    data = request.json

    if not data.get('Songs'):
        return jsonify({ "message": "Bad Request"}), 400

    song_data = data['Songs'][0]
    song_data['user_id'] = current_user.id

    new_song = Song(**song_data)

    db.session.add(new_song)

    response = {'Songs': [new_song.to_dict()]}

    if data.get('Images'):
        new_image = Image(
            song_id=new_song.id,
            album_id=song_data['album_id'],
            url=data['Images'][0]['url']
        )
        db.session.add(new_image)
        response['Images'] = [{
            "id": new_image.id,
            "url": new_image.url
        }]
    db.session.commit()
    return jsonify(response), 201


@songs_routes.route('/<int:songId>', methods=['PUT'])
@login_required
def update_song():
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
    song.release_year = song_data['release_year']
    song.album_id = song_data['album_id']
    song.lyrics = song_data['lyrics']

    db.session.add(song)

    response = {'Songs': [song.to_dict()]}

    if data.get('Images'):
        image = Image.query


# something random
