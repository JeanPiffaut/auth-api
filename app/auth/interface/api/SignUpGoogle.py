import os

import requests
from flask import request, redirect
from flask_restful import Resource

from app.common.interface.Miscellaneous import get_google_provider_cfg
from config.web_aplication_client import client


class SignUpGoogle(Resource):
    def get(self):
        google_provider_cfg = get_google_provider_cfg()

        request_uri = client.prepare_request_uri(
            google_provider_cfg["authorization_endpoint"],
            redirect_uri=os.getenv('BASE_URL') + "/v1/oauth2/google/callback/sign_up_callback",
            scope=['openid', 'email', 'profile']
        )

        return redirect(request_uri)
