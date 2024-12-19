from flask import Blueprint, request, jsonify
from app.models import User, Playlist, PlaylistSong
from app import db
from flask_login import current_user, login_required


playlists_routes = Blueprint('playlists', __name__)


@playlists_routes.route('/', methods=['GET'])
def playlists():

    playlists = Playlist.query.all()
    return jsonify({'Playlists': [playlist.to_dict() for playlist in playlists ]})


