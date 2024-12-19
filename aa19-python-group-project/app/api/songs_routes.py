from flask import Blueprint, jsonify, request
from app.models import Song 
from flask_login import login_required
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

    new_song = Song(**song_data)

    db.session.add(new_song)
    db.session.commit()

    return jsonify(new_song.to_dict()), 201


