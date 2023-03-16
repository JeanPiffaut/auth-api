import os
import requests

from flask import Flask, redirect, request, url_for
from flask_restful import Api
from flask.cli import load_dotenv
from flask_login import (LoginManager, current_user, login_required, login_user, logout_user)
from oauthlib.oauth2 import WebApplicationClient

from app.users import users_bp

# Get env values
load_dotenv()

# Create flask project
api = Flask(__name__, template_folder='templates')
api.secret_key = os.getenv('SECRET_KEY')

# Config login manager
login_manager = LoginManager()
login_manager.init_app(api)

# Config Web Application
client = WebApplicationClient(os.getenv('GOOGLE_CLIENT_ID'))

if __name__ == '__main__':
    # Config flask_restful
    Api(api, catch_all_404s=True)
    api.url_map.strict_slashes = False

    api.register_blueprint(users_bp)

    # Run project
    api.run(debug=True)
