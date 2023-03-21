from flask import Blueprint

from app import ExtendAPI

auth_bp = Blueprint('auth', __name__)
api = ExtendAPI(auth_bp)

# Add endpoints
# api.add_resource(Login, '/', endpoint='login')
