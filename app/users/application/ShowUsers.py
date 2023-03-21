from app.users.domain.Model import User
from app.users.domain.UserApplicationModel import UserApplicationModel
from app.users.interface.FirestoreRepository import UserFirestoreRepository
from config.login_manager import login_manager


class ShowUsers(UserApplicationModel):

    @login_manager.user_loader
    def by_id(self, user_id):
        self.user = User()
        self.user.id = user_id

        repo = UserFirestoreRepository()
        result = repo.view(user_id=self.user.id)

        users = [result.to_dict()]

        return users

    def by_params(self, email=None, name=None):
        self.user = User()
        self.user.email = email
        self.user.name = name

        repo = UserFirestoreRepository()
        result = repo.view(user_email=self.user.email, user_name=self.user.name)
        users = []
        if len(result) != 0:
            users = []
            for doc in result:
                if doc.exists:
                    users.append(doc.to_dict())

        return users

