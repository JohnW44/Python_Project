from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import Like, Song, Album
from app import db

likes_routes = Blueprint('likes', __name__)

@likes_routes.route('/users/<int:user_id>/likedsongs', methods=['GET'])
@login_required
def get_liked_songs(user_id):
    """
    Get all songs liked by the current user.
    """
    if user_id != current_user.id:
        return {"error": "Unauthorized access"}, 403
    
    likes = Like.query.filter_by(user_id=user_id, album_id=None).all()
    songs = [like.song.to_dict() for like in likes if like.song]

    return jsonify({"Songs": songs}), 200


@likes_routes.route('/users/<int:user_id>/likedalbums', methods=['GET'])
@login_required
def get_liked_albums(user_id):
    """
    Fet all albums liked by the current user
    """
    if user_id != current_user.id:
        return {"error": "Unauthorized access"}, 403
    
    likes = Like.query.filtter_by(user_id=user_id, song_id=None).all()
    albums = [like.album.to_dict() for like in likes if like.album]

    return jsonify({"Albums": albums}), 200


@likes_routes.route('/users/<int:user_id>/likedsongs', methods=['POST'])
@login_required
def like_song(user_id):
    """
    Like a song based on song_id.
    """
    if user_id != current_user.id:
        return {"error": "Unauthorized access"}, 403
    
    song_id = request.json.get('song_id')
    song = Song.query.get(song_id)
    if not song:
        return {"message": "Song couldn't be found"}, 404
    
    like = Like(user_id=user_id, song_id=song_id)
    db.session.add(like)
    db.session.commit()

    return jsonify({"messege": "Successfully Liked Song", "like": like.to_dict()}), 200


@likes_routes.route('/users/<int:user_id>/likedalbums', methods=['POST'])
@login_required
def like_album(user_id):
    """
    Like an album based on a album_id.
    """
    if user_id != current_user.id:
        return {"error": "Unauthorized access"}, 403
    
    album_id = request.json.get('album_id')
    album = Album.query.get(album_id)
    if not album: 
        return {"messege": "Album couldn't be found"}, 404
    
    like = Like(user_id=user_id, album_id=album_id)
    db.session.add(like)
    db.session.commit()

    return jsonify({"messege": "Successfully Like Album", "like": like.ro_dict()}), 200


@likes_routes.route('/users/<int:user_id>/likedsongs', methods=['DELETE'])
@login_required
def unlike_song(user_id):
    """
    Unlike a song based on song_id.
    """
    if user_id != current_user.id:
        return {"error": "Unauthorized access"}, 403

    song_id = request.json.get('song_id')
    like = Like.query.filter_by(user_id=user_id, song_id=song_id).first()
    if not like:
        return {"messege": "Song couldn't be found"}, 404
    
    db.session.delete(like)
    db.session.commit()

    return jsonify({"messege": "Successfully Unliked Song"}), 200


@likes_routes.route('/users/<int:user_id>/likedalbums', methods=['DELETE'])
@login_required
def unlike_album(user_id):
    """
    Unlike an album based on album_id.
    """
    if user_id != current_user.id:
        return {"error": "Unauthorized access"}, 403
    
    album_id = request.json.get('album_id')
    like = Like.query.filter_by(user_id=user_id, album_id=album_id).first()
    if not like: 
        return {"messege": "Album couldn't be found"}, 404
    
    db.session.delete(like)
    db.session.commit()

    return jsonify({"messege": "Successfully Unliked Album"}), 200