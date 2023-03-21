from flask_login import login_user
from app.auth.domain.AuthApplicationModel import ApplicationModel
from app.users.application.ShowUsers import ShowUsers


class AuthLogin(ApplicationModel):
    def google_auth(self, userinfo_response):
        email = userinfo_response['email']

        show_user = ShowUsers()
        users_result = show_user.by_params(email=email)

        if users_result.count() == 0:
            return False

        user = users_result[0]
        print(user)
        return True



