from flask import request
from flask_restful import Resource

from app import response_structure


class UserResource(Resource):
    def get(self):
        return response_structure(200)
