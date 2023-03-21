from flask import request
from flask_login import login_required
from flask_restful import Resource

from app import response_structure
from app.users.application.ShowUsers import ShowUsers


class CredentialResource(Resource):
    @login_required
    def get(self):
        show = ShowUsers()
        if request.args.get('user_id') is not None:
            result = show.by_id(request.args.get('user_id'))
            return response_structure(200, result)
        else:
            return response_structure(200)

