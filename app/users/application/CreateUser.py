from app.users.domain.Model import User
from app.users.domain.UserApplicationModel import UserApplicationModel
from app.users.interface.FirestoreRepository import UserFirestoreRepository


class CreateUser(UserApplicationModel):
    def by_params(self, name, email, picture=None):
        self.user = User()
        self.user.email = email
        self.user.name = name
        self.user.picture = picture

        repo = UserFirestoreRepository()
        result = repo.create(self.user.name, self.user.email, self.user.picture)

        return result
