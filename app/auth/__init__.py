from flask import Blueprint

from app import ExtendAPI
from app.auth.interface.api.CallbackGoogle import CallbackGoogle
from app.auth.interface.api.LoginGoogle import LoginGoogle
from app.auth.interface.html.Login import Login
from app.auth.interface.html.SignUp import SignUp

auth_bp = Blueprint('auth', __name__)
api = ExtendAPI(auth_bp)

# Add endpoints
api.add_resource(Login, '/', endpoint='login')
api.add_resource(SignUp, '/sign_up', endpoint='sign_up')
api.add_resource(LoginGoogle, '/v1/oauth2/google', endpoint='google_login')
api.add_resource(CallbackGoogle, '/v1/oauth2/google/callback/<string:callback_type>', endpoint='google_callback')
api.add_resource(Login, '/v1/oauth2/google/logout', endpoint='google_logout')
