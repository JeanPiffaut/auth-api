import os

import requests
from flask import request, redirect
from flask_restful import Resource

from app.common.interface.Miscellaneous import get_google_provider_cfg
from config.web_aplication_client import client


class LoginResource(Resource):
    def get(self):
        # Find out what URL to hit for Google login
        google_provider_cfg = get_google_provider_cfg()
        authorization_endpoint = google_provider_cfg["authorization_endpoint"]

        request_uri = client.prepare_request_uri(
            authorization_endpoint,
            redirect_uri=request.base_url + "/callback",
            scope=["email"],
        )

        return redirect(request_uri)