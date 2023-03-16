import os

from flask.cli import load_dotenv
from oauthlib.oauth2 import WebApplicationClient

load_dotenv()

# Config Web Application
client = WebApplicationClient(os.getenv('GOOGLE_CLIENT_ID'))
