from flask import Blueprint, request, jsonify
from app.models import User, Playlist
from app import db
from flask_login import current_user, login_required


playlists_routes = Blueprint('playlists', __name__)


@playlists_routes.route('/', methods=['GET'])
def playlists():
    """
    Query for all playlists with all being logged in
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
    return jsonify(new_playlist.to_dict())
# return jsonify({"message": "Playlist successfully created"}), 201

@playlists_routes.route('/users/<int:userId>/playlist/<int:playlistId>', methods=["DELETE"])
@login_required
def delete_playlist(userId, playlistId):
    """
    Delete playlist base on userId
    """
    playlist = db.session.query(Playlist).get(playlistId)

    if playlist:
        db.session.delete(playlist)
        db.session.commit()
        return jsonify({"message": "Playlist successfully deleted"}), 200

    return jsonify({"message", "Playlist could not be found"}), 400
