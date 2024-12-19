from flask import Blueprint, request, jsonify
from app.models import User, Playlist, PlaylistSong
from app import db
from flask_login import current_user


playlists_routes = Blueprint('playlist_routes', __name__)


@playlists_routes.route('/', methods=['GET'])
def playlist():

    playlists = Playlist.query.all()
    return jsonify({'Playlist': [playlist.to_dict() for playlist in playlists ]})
