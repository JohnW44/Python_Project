from flask import Blueprint, request
from app.models import User, db
from app.forms import LoginForm
from app.forms import SignUpForm
from flask_login import current_user, login_user, logout_user, login_required
from .melody_images import upload_file_to_s3, get_unique_filename 

auth_routes = Blueprint('auth', __name__)


@auth_routes.route('/')
def authenticate():
    """
    Authenticates a user.
    """
    if current_user.is_authenticated:
        return current_user.to_dict()
    return {
      "user": "null"
    }, 401


@auth_routes.route('/login', methods=['POST'])
def login():
    """
    Logs a user in
    """
    form = LoginForm()
    # Get the csrf_token from the request cookie and put it into the
    # form manually to validate_on_submit can be used
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        # Add the user to the session, we are logged in!
        user = User.query.filter(User.email == form.data['email']).first()
        login_user(user)
        return user.to_dict()
    return form.errors, 401


@auth_routes.route('/logout', methods=['POST'])
def logout():
    """
    Logs a user out
    """
    logout_user()
    return {'message': 'User logged out'}


@auth_routes.route('/signup', methods=['POST'])
def sign_up():
    """
    Creates a new user and logs them in
    """
    form = SignUpForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    
    if form.validate_on_submit():
        profile_image_url = None
        if 'profile_image' in request.files:
            image = request.files['profile_image']
            if image:
                image.filename = get_unique_filename(image.filename)
                upload_response = upload_file_to_s3(image)
                
                if "url" not in upload_response:
                    return {"errors": "Failed to upload image"}, 400
                profile_image_url = upload_response["url"]

        user = User(
            username=form.data['username'],
            email=form.data['email'],
            password=form.data['password'],
            first_name=form.data['first_name'],
            last_name=form.data['last_name'],
            profile_image=profile_image_url
        )
        
        db.session.add(user)
        try:
            db.session.commit()
            login_user(user)
            return user.to_dict()
        except Exception as e:
            db.session.rollback()
            return {"errors": str(e)}, 400
    
    # If form validation fails, return the errors
    return {"errors": form.errors}, 401
    return form.errors, 401


@auth_routes.route('/unauthorized')
def unauthorized():
    """
    Returns unauthorized JSON when flask-login authentication fails
    """
    return {'errors': {'message': 'Unauthorized'}}, 401