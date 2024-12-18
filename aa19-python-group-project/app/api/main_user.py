from flask import Blueprint, jsonify
from flask_login import current_user
from app.models import User
from app.models import db

mainuser_routes = Blueprint('mainuser', __name__)

@mainuser_routes.route('/')
def user():
    # current_user = db.session.query(User)

    if current_user.is_authenticated:
        return jsonify(current_user)
