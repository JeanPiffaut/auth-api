from flask_restful import abort

from app.auth.domain.AuthApplicationModel import AuthApplicationModel
from app.credentials.application.CreateCredential import CreateCredential
from app.users.application.CreateUser import CreateUser
from app.users.application.ShowUsers import ShowUsers


class AuthSignUp(AuthApplicationModel):
    @staticmethod
    def google_auth(self, userinfo_response, token):
        name = userinfo_response['name']
        email = userinfo_response['email']
        picture = userinfo_response['picture']

        show_user = ShowUsers()
        users_result = show_user.by_params(email=email)
        if len(users_result) == 0:
            create_user = CreateUser()
            user_reference = create_user.by_params(name, email, picture)

            create_credential = CreateCredential()
            credential_reference = create_credential.by_google(token=token, email=email, user_reference=user_reference)

            return True
        else:
            abort(400)
