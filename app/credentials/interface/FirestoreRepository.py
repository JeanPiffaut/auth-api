from app.common.domain.FirestoreRepositoryModel import FirestoreRepositoryModel
from config.firestore import fr


class CredentialRepository(FirestoreRepositoryModel):
    _collection = "Credentials"

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

    def create(self, token_access, username, user_reference, credential_type):
        coll = fr.collection(self._collection)
        data = {
            'token_access': token_access,
            'username': username,
            'user': user_reference,
            'type': credential_type
        }

        date, reference = coll.add(data)
        return reference
