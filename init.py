import os
import requests

from flask import Flask
from flask_restful import Api
from flask.cli import load_dotenv
from oauthlib.oauth2 import WebApplicationClient

from app.auth import auth_bp
from app.users import users_bp
from config.login_manager import login_manager

# Get env values
load_dotenv()

# Create flask project
api = Flask(__name__, template_folder='templates')
api.secret_key = os.getenv('SECRET_KEY')

if __name__ == '__main__':
    # Config flask_restful
    Api(api, catch_all_404s=True)
    api.url_map.strict_slashes = False

    # User session management
    login_manager.init_app(api)

    api.register_blueprint(auth_bp)
    api.register_blueprint(users_bp)

    # Run project
    api.run(debug=True, ssl_context="adhoc")
