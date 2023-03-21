from flask import request, render_template, make_response
from flask_login import current_user
from flask_restful import Resource

from app import response_structure


class HTMLResource(Resource):
    def get(self):
        if current_user.is_authenticated is False:
            html = render_template('login_template.html')
            response = make_response(html)
            response.headers['Content-Type'] = 'text/html'
            return response
        else:
            return response_structure(200)
