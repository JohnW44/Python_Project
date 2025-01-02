from flask import Blueprint, request, jsonify
from app.models import Playlist, PlaylistSong, User
from app import db
from flask_login import current_user, login_required
from datetime import datetime


playlists_routes = Blueprint('playlists', __name__)

@playlists_routes.route('/', methods=["GET"])
def get_playlists():
    playlists = Playlist.query.all()
    return jsonify([playlist.to_dict() for playlist in playlists]), 200

@playlists_routes.route('/users/<int:user_id>/playlists', methods=['GET'])
def get_user_playlists(user_id):

    """
    Returns all the playslists that belong to a userId specified by id.
    """
    playlists = Playlist.query.filter_by(user_id=user_id).all()

    if playlists:
        return jsonify({
            "playlist": [
                {
                    "id": playlist.id,
                    "playlistId": playlist.playlist_id,
                    "name": playlist.name,
                    "created_at": playlist.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                    "updated_at": playlist.updated_at.strftime('%Y-%m-%d %H:%M:%S')
                }
                for playlist in playlists
            ]
        }), 200
    else:
        # If no playlists are found for the user, return an error response
        return jsonify({"message": "Playlists couldn't be found"}), 404



@playlists_routes.route('/users/<int:user_id>/playlists/<int:playlist_id>', methods=["POST"])
@login_required
def create_playlist():
    """
    Creates a playlist if the user is logged in, and checks for authorization and existence of the user.
    """

    data = request.json
    user_id = data.get('user_id')
    name = data.get('name')


    if user_id != current_user.id:
        return jsonify({"message": "Unauthorized"}), 403


    user = User.query.get(user_id)
    if not user:
        return jsonify({"message": "User not found"}), 404


    existing_playlist = Playlist.query.filter_by(user_id=user_id, name=name).first()
    if existing_playlist:
        return jsonify({"message": "Playlist already exists for this user"}), 400


    if not name:
        return jsonify({"message": "Please enter required fields"}), 400

    new_playlist = Playlist(
        user_id=user_id,
        name=name,
        created_at=datetime.now(),
        updated_at=datetime.now()
    )

    db.session.add(new_playlist)
    db.session.commit()

    return jsonify({"message": "Playlist successfully created", "Playlist": new_playlist.to_dict()}), 200

@playlists_routes.route('/users/<int:user_id>/playlists/<int:playlist_id>/song/<int:song_id>', methods=["POST"])
@login_required

def add_song_to_playlist(user_id, playlist_id, song_id):
    """
    Add Songs to an User created Playlist based on Playlist's id
    """
    if current_user.id != user_id:
        return jsonify({"message": "Unauthorized"}), 403

    playlist = Playlist.query.filter_by(id=playlist_id, user_id=user_id).first()
    if not playlist:
        return jsonify({"message": "Playlist Not Found"}), 404

    existing_song_in_playlist = PlaylistSong.query.filter_by(playlist_id=playlist_id, song_name=song_id).first()
    if existing_song_in_playlist:
        return jsonify({"message": "Song already exists in this playlist"}), 400

    try:
        new_playlist_song = PlaylistSong(
            playlist_id=playlist_id,
            song_name=song_id
        )

        db.session.add(new_playlist_song)
        db.session.commit()

        return jsonify({
            "playlist": [
                {
                "id": playlist.id,
                "playlistId": playlist.playlist_id,
                "name": playlist.name,
                "created_at": playlist.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                "updated_at": playlist.updated_at.strftime('%Y-%m-%d %H:%M:%S')
                }
            ]
        }), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "Error adding song to playlist"}), 500

@playlists_routes.route('/users/<int:user_id>/playlists/<int:playlist_id>/song/<int:song_id>', methods=["DELETE"])
@login_required
def delete_song_from_playlist(user_id, playlist_id, song_id):
    """
      Delete a song on users playlist
    """

    if current_user.id != user_id:
        return jsonify({"message": "Unauthorized"}), 403

    playlist = Playlist.query.filter_by(id=playlist_id, user_id=user_id).first()
    if not playlist:
        return jsonify({"message": "Playlist Not Found"}), 404

    song_in_playlist = PlaylistSong.query.filter_by(playlist_id=playlist_id, song_name=song_id).first()
    if not song_in_playlist:
        return jsonify({"message": "Song Not Found in Playlist"}), 404

    try:
        db.session.delete(song_in_playlist)
        db.session.commit()

        return jsonify({
            "message": "Song successfully deleted from Playlist"
        }), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "error deleting song from playlist"}), 500


@playlists_routes.route('/users/<int:user_id>/playlists/<int:playlist_id>', methods=["DELETE"])
@login_required
def delete_playlist(user_id, playlist_id):
    """
      Users should be able DELETE playlists based on PlaylistId
    """

    if current_user.id != user_id:
        return jsonify({"message": "Unauthorized"}), 403

    playlist = Playlist.query.filter_by(id=playlist_id, user_id=user_id).first()

    if not playlist:
        return jsonify({"message": "Playlist couldn't be found"}), 404


    try:
        db.session.delete(playlist)
        db.session.commit()

        return jsonify({
            "message": "Successfully deleted"
        }), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "Error deleting playlist"}), 500
