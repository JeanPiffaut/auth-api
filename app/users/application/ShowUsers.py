from app.users.domain.UserApplicationModel import UserApplicationModel
from app.users.interface.FirestoreRepository import UserFirestoreRepository
from init import login_manager


class ShowUsers(UserApplicationModel):

    @login_manager.user_loader
    def by_id(self, user_id):
        self.user.id = user_id

        repo = UserFirestoreRepository()
        result = repo.view(user_id=self.user.id)

        return result.to_dict()
