from flask import Blueprint

from app import ExtendAPI
from app.auth.interface.CallbackResource import CallbackResource
from app.auth.interface.HTMLResource import HTMLResource
from app.auth.interface.LoginResource import LoginResource

auth_bp = Blueprint('auth', __name__)
api = ExtendAPI(auth_bp)

# Add endpoints
api.add_resource(HTMLResource, '/', endpoint='auth_resource')
api.add_resource(LoginResource, '/v1/login', endpoint='login_resource')
api.add_resource(CallbackResource, '/v1/login/callback', endpoint='callback_resource')
api.add_resource(HTMLResource, '/v1/logout', endpoint='logout_resource')
