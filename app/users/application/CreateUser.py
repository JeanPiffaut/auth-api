from app.users.domain.Model import User
from app.users.domain.UserApplicationModel import UserApplicationModel
from app.users.interface.FirestoreRepository import UserFirestoreRepository


class CreateUser(UserApplicationModel):
    def by_params(self, name, email):
        self.user = User()
        self.user.email = email
        self.user.name = name

        repo = UserFirestoreRepository()
        reference = repo.create(self.user.name, self.user.email)

        return reference
