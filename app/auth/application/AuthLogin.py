import os

from flask_login import login_user
from flask_restful import abort

from app.auth.domain.AuthApplicationModel import AuthApplicationModel
from app.credentials.application.ShowCredentials import ShowCredentials
from app.sessions.application.CreateSession import CreateSession


class AuthLogin(AuthApplicationModel):
    @staticmethod
    def google_auth(userinfo_response):
        email = userinfo_response['email']

        show_credential = ShowCredentials()
        result = show_credential.by_params(username=email, credential_type=os.getenv('GOOGLE_CREDENTIAL_TYPE'))

        if len(result) == 0:
            abort(400)

        credential_doc = None
        for doc in result:
            if doc.exists:
                credential_doc = doc

        credential = credential_doc.to_dict()

        create_session = CreateSession()
        create_session.by_params(user_reference=credential['user'], credential_reference=credential_doc.reference)
