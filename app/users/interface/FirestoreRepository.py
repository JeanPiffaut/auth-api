from app.common.domain.FirestoreRepositoryModel import FirestoreRepositoryModel
from config.firestore import fr


class UserFirestoreRepository(FirestoreRepositoryModel):
    _collection = "Users"

    def view(self, user_id=None, user_name=None, user_email=None):
        coll = fr.collection(self._collection)

        if user_id is None:
            if user_name is not None:
                coll = coll.where('name', '==', user_name)

            if user_email is not None:
                coll = coll.where('email', '==', user_email)

            return coll.limit(100).get()
        else:
            coll = coll.document(user_id)
            return coll.get()

    def create(self, user_name, user_email):
        coll = fr.collection(self._collection)
        data = {
            'user_name': str(user_name),
            'user_email': str(user_email)
        }

        result = coll.add(data)
        print(result)
        return result
