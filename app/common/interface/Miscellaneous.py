import os

import requests


def get_google_provider_cfg():
    return requests.get(os.getenv('GOOGLE_DISCOVERY_URL')).json()