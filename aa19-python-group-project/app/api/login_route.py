from flask import Blueprint, jsonify, request
from flask_login import login_user, current_user
from app.models import User
from app.models import db
from ..forms import LoginForm

login_routes = Blueprint('login', __name__)

@login_routes.route('/', methods=['POST'])
def login():
    if current_user.is_authenticated:
        form = LoginForm()
    if form.validate_on_submit():
        return 'submit complete'
        # user_password = form.hash_password
    # data = request.get.json()
    # credential = data['credential']
    # password = data['password']


    