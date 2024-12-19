from flask import Blueprint, jsonify
from app.models import Song 
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

