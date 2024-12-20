from flask import Blueprint, request, jsonify
from app.models import Playlist, PlaylistSong
from app import db
from flask_login import current_user, login_required


playlists_routes = Blueprint('playlists', __name__)


@playlists_routes.route('/playlists', methods=['GET'])
def playlists():
    """
    Query for all playlists without being logged in
    """

    playlists = Playlist.query.all()
    return jsonify({'Playlists': [playlist.to_dict() for playlist in playlists ]})



@playlists_routes.route('/users/<int:userId>/playlists', methods=['GET'])
@login_required
def users_playlists(userId):

    """
    Get user playlists by user id
    """

    if userId != current_user.id:
        return { "error": "User could not be found"}, 404

    playlists = Playlist.query.all()
    return jsonify({'Playlists': [playlist.to_dict() for playlist in playlists ]}), 200


@playlists_routes.route('/users/<int:userId>/playlists/<int:playlistId>', methods=["POST"])
@login_required
def create_playlists(userId):
    """
    Create playlist by userId
    """
    if userId != current_user.id:
        return { "error": "User could not be found"}, 404

    playlist = request.json

    new_playlist = Playlist(**playlist)

    db.session.add(new_playlist)

    db.session.commit()
    return jsonify({"Playlists": new_playlist.to_dict()}), 201
# return jsonify({"message": "Playlist successfully created"}), 201

@playlists_routes.route('/users/<int:userId>/playlists/<int:playlistId>/playlistSong/<int:playSongId>', methods=["POST"])
@login_required
def add_song_playlist(userId):

    """
    Add Songs to an User created Playlist based on Playlist's id
    """

    if userId != current_user.id:
        return {"error": "User could not be found"}, 404

    playlist_id = request.json.get('playlist_id')
    playlist = Playlist.query.get(playlist_id)
    if not playlist:
        return jsonify({'message': 'Playlist could not be found'}), 404

    song = PlaylistSong(userId=userId, playlist_id=playlist_id)
    db.session.add(song)
    db.session.commit()

    return jsonify({"message": "Successfully added Song"}), 200

@playlists_routes.route('/users/<int:userId>/playlists/<int:playlistId>/playlistSong/<int:playlistSongId>', methods=["DELETE"])
@login_required
def delete_song_playlist(userId, playlistId, playlistSongId):

    """
    Delete a song on users playlist
    """

    if userId != current_user.id:
        return {"error": "User could not be found"}, 404

    playlist = Playlist.query.get(playlistId)
    if not playlist:
        return jsonify({"message": "Playlist could be found"}), 404

    song = db.session.query(PlaylistSong).get(playlistSongId)
    if song:
        db.session.delete(song)
        db.session.commit()
        return jsonify({"message": "PlaylistSong successfully deleted"}), 201

    return jsonify({"message": "Playlist could not be found"}), 404

@playlists_routes.route('/users/<int:userId>/playlists/<int:playlistId>', methods=["DELETE"])
@login_required
def delete_playlist(userId, playlistId):
    """
    Delete playlist base on userId
    """
    if userId != current_user.id:
        return {"error": "User could not be found"}, 404

    playlist = db.session.query(Playlist).get(playlistId)

    if playlist:
        db.session.delete(playlist)
        db.session.commit()
        return jsonify({"message": "Playlist successfully deleted"}), 200

    return jsonify({"message", "Playlist could not be found"}), 400
