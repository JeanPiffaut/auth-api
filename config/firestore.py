import os

from google.cloud import firestore

fr = firestore.Client.from_service_account_json(os.getenv('GOOGLE_APPLICATION_CREDENTIALS'))
