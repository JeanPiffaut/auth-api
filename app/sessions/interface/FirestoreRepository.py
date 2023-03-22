from app.common.domain.FirestoreRepositoryModel import FirestoreRepositoryModel
from config.firestore import fr


class SessionRepository(FirestoreRepositoryModel):
    _collection = "Sessions"

    def view(self, credential_id=None, user_reference=None, username=None, credential_type=None):
        coll = fr.collection(self._collection)

        if credential_id is None:
            if username is not None:
                coll = coll.where('username', '==', username)

            if user_reference is not None:
                coll = coll.where('user', '==', user_reference)

            if credential_type is not None:
                coll = coll.where('type', '==', credential_type)

            return coll.limit(100).get()
        else:
            coll = coll.document(credential_id)
            return coll.get()

    def create(self, user_reference, credential_reference, token, creation_date, last_activity, life_time):
        coll = fr.collection(self._collection)
        data = {
            'user': user_reference,
            'credential': credential_reference,
            'token': token,
            'creation_date': creation_date.timestamp(),
            'last_activity': last_activity.timestamp(),
            'life_time': life_time
        }

        date, reference = coll.add(data)
        return reference
