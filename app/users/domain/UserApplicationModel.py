from app.users.domain.Model import User


class UserApplicationModel:
    user: User

    def __int__(self):
        self.user = User()
