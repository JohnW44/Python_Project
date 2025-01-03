from flask import Blueprint, jsonify, request
from app.models import Song, Image
from flask_login import login_required, current_user
from datetime import datetime
import os
from app.api.melody_songs_aws import (
     upload_file_to_s3,
     get_unique_filename
)
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
    Add song to Database while a user is logged in
    """
    if "audio_file" not in request.files:
        return jsonify({"errors": "audio file required"}), 400

    audio_file = request.files["audio_file"]
    if not audio_file.filename:
        return jsonify({"errors": "valid audio file required"}), 400
    
    
    audio_file.filename = get_unique_filename(audio_file.filename)
    upload = upload_file_to_s3(audio_file)
    
    if "errors" in upload:
        return jsonify({"errors": upload["errors"]}), 400

   
    song_data = {
        'title': request.form.get('title'),
        'artist': request.form.get('artist'),
        'released_date': datetime.strptime(request.form.get('released_date'), '%Y-%m-%d').date(),
        'duration': request.form.get('duration'),
        'lyrics': request.form.get('lyrics'),
        'audio_file': upload["url"],
        'user_id': current_user.id
    }
    
    new_song = Song(**song_data)
    db.session.add(new_song)
    
    if 'image_file' in request.files:
        image_file = request.files['image_file']
        image_file.filename = get_unique_filename(image_file.filename)
        image_upload = upload_file_to_s3(image_file)
        
        if "url" in image_upload:
            new_image = Image(
                song_id=new_song.id,
                url=image_upload["url"]
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

    if "audio_file" in request.files:
        audio_file = request.files["audio_file"]
        audio_file.filename = get_unique_filename(audio_file.filename)
        upload = upload_file_to_s3(audio_file)

        if "url" not in upload:
            return jsonify({"errors": upload}), 400
            
        song.audio_url = upload["url"]

    song_data = data['Songs'][0]

    if "title" in song_data and song_data["title"] == "":
        return jsonify({"error": "Title cannot be empty"}), 400 
    if "title" in song_data:
        song.title = song_data['title']
    if "artist" in song_data and song_data["artist"] == "":
        return jsonify({"error": "Artist cannot be empty"}), 400     
    if "artist" in song_data:
        song.artist = song_data['artist']
    if "released_date" in song_data and song_data["released_date"] == "":
        return jsonify({"error": "Released date cannot be empty"}), 400     
    if "released_date" in song_data:    
        song.released_date = datetime.strptime(song_data['released_date'], '%Y-%m-%d').date()
    if "album_id" in song_data:
        song.album_id = song_data['album_id']
    if "lyrics" in song_data:
        song.lyrics = song_data['lyrics']
    if "duration" in song_data and song_data["duration"] == "":
        return jsonify({"error": "Duration cannot be empty"}), 400     
    if "duration" in song_data:
        song.duration = song_data['duration']    
    
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
   

