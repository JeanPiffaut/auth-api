import json
import os

import requests
from flask import request
from flask_restful import Resource

from app.auth.application.AuthLogin import AuthLogin
from app.common.interface.Miscellaneous import get_google_provider_cfg
from config.web_aplication_client import client


class CallbackResource(Resource):
    def get(self):
        code = request.args.get("code")

        google_provider_cfg = get_google_provider_cfg()
        token_endpoint = google_provider_cfg["token_endpoint"]

        token_url, headers, body = client.prepare_token_request(
            token_endpoint,
            authorization_response=request.url,
            redirect_url=request.base_url,
            code=code
        )

        token_response = requests.post(
            token_url,
            headers=headers,
            data=body,
            auth=(os.getenv('GOOGLE_CLIENT_ID'), os.getenv('GOOGLE_CLIENT_SECRET'))
        )

        try:
            client.parse_request_body_response(json.dumps(token_response.json()))
            token_valid = True
        except Exception:
            token_valid = False

        if token_valid:
            userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
            uri, headers, body = client.add_token(userinfo_endpoint)
            userinfo_response = requests.get(uri, headers=headers, data=body)

            if userinfo_response.json().get("email_verified"):
                auth = AuthLogin()
                auth.google_auth(userinfo_response.json())

                return userinfo_response.json(), 200
            else:
                return "User email not available or not verified by Google.", 400
        else:
            return "User email not available or not verified by Google.", 400
