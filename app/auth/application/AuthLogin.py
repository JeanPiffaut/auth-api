from flask_login import login_user
from app.auth.domain.AuthApplicationModel import AuthApplicationModel
from app.users.application.ShowUsers import ShowUsers


class AuthLogin(AuthApplicationModel):
    def google_auth(self, userinfo_response):
        email = userinfo_response['email']

        show_user = ShowUsers()
        users_result = show_user.by_params(email=email)

        if len(users_result) == 0:
            return False

        user = users_result[0]
        return True



