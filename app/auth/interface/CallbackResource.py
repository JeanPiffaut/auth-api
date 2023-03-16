import json
import os

import requests
from flask import request, abort
from flask_restful import Resource

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
        print(token_url)
        print(headers)
        print(body)
        print(os.getenv('GOOGLE_CLIENT_ID'))
        print(os.getenv('GOOGLE_CLIENT_SECRET'))

        token_response = requests.post(
            token_url,
            headers=headers,
            data=body,
            auth=(os.getenv('GOOGLE_CLIENT_ID'), os.getenv('GOOGLE_CLIENT_SECRET')),
        )

        #TODO: se debe encontrar el error de por que el token no es valido
        if token_response.json()['error'] == "invalid_client":
            abort(401)

        client.parse_request_body_response(json.dumps(token_response.json()))

        userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
        uri, headers, body = client.add_token(userinfo_endpoint)
        userinfo_response = requests.get(uri, headers=headers, data=body)

        if userinfo_response.json().get("email_verified"):
            unique_id = userinfo_response.json()["sub"]
            users_email = userinfo_response.json()["email"]
            picture = userinfo_response.json()["picture"]
            users_name = userinfo_response.json()["given_name"]
            return userinfo_response.json(), 200
        else:
            return "User email not available or not verified by Google.", 400
