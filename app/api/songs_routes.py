from flask import Blueprint, jsonify, request
from app.models import Song, Image
from flask_login import login_required, current_user
from datetime import datetime
import os
from app.api.melody_songs_aws import (
     upload_file_to_s3 as upload_song_to_s3,
     get_unique_filename as get_unique_song_filename
)
from app.api.melody_images import (
    upload_file_to_s3 as upload_image_to_s3,
    get_unique_filename as get_unique_image_filename
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
   
   
    audio_file.filename = get_unique_song_filename(audio_file.filename)
    upload = upload_song_to_s3(audio_file)
   
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
    db.session.flush()
   
    if 'image' in request.files:
        image_file = request.files['image']
        if image_file.filename:
            print("Processing image file:", image_file.filename)
            
            image_file.filename = get_unique_image_filename(image_file.filename)
            image_upload = upload_image_to_s3(image_file)
            
            if "errors" in image_upload:
                print("Image upload error:", image_upload["errors"])
                return jsonify({"errors": image_upload["errors"]}), 400

            new_image = Image(
                song_id=new_song.id,
                url=image_upload["url"],
            )
            db.session.add(new_image)
            # db.session.commit()
            
            print("Image uploaded successfully:", image_upload["url"])
   
    try:
        db.session.commit()
        return jsonify({'Songs': new_song.to_dict()}), 201
    except Exception as e:
        db.session.rollback()
        print(f"Database error: {str(e)}")
        return jsonify({"errors": str(e)}), 500


@songs_routes.route('/<int:songId>', methods=['PUT'])
@login_required
def update_song(songId):
    """
    Updates and returns a song uploaded by user
    """
    song = Song.query.get(songId)
    if not song:
        return jsonify({"error": "Song couldn't be found"}), 404
    if song.user_id != current_user.id:
        return jsonify({"error": "Unauthorized"}), 403

    if "title" in request.form and request.form.get("title") == "":
        return jsonify({"error": "Title cannot be empty"}), 400 
    if "title" in request.form:
        song.title = request.form.get('title')
    if "artist" in request.form and request.form.get("artist") == "":
        return jsonify({"error": "Artist cannot be empty"}), 400     
    if "artist" in request.form:
        song.artist = request.form.get('artist')
    if "released_date" in request.form and request.form.get("released_date") == "":
        return jsonify({"error": "Released date cannot be empty"}), 400     
    if "released_date" in request.form:    
        song.released_date = datetime.strptime(request.form.get('released_date'), '%Y-%m-%d').date()
    if "album_id" in request.form:
        song.album_id = request.form.get('album_id')
    if "lyrics" in request.form:
        song.lyrics = request.form.get('lyrics')
    if "duration" in request.form and request.form.get("duration") == "":
        return jsonify({"error": "Duration cannot be empty"}), 400     
    if "duration" in request.form:
        song.duration = request.form.get('duration')    
    
    if "image" in request.files:
        image_file = request.files["image"]
        if image_file.filename:
            existing_image = Image.query.filter_by(song_id=songId).first()
            if existing_image:
                db.session.delete(existing_image)
                db.session.commit()

            image_file.filename = get_unique_image_filename(image_file.filename)
            image_upload = upload_image_to_s3(image_file)
            
            if "errors" in image_upload:
                return jsonify({"errors": image_upload["errors"]}), 400

            new_image = Image(
                song_id=songId,
                url=image_upload["url"]
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
   

