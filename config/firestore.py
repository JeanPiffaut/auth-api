import os

from flask.cli import load_dotenv
from google.cloud import firestore

load_dotenv()

fr = firestore.Client.from_service_account_json(os.getenv('GOOGLE_APPLICATION_CREDENTIALS'))
