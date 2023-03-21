from app.common.domain.FirestoreRepositoryModel import FirestoreRepositoryModel
from config.firestore import fr


class CredentialResource(FirestoreRepositoryModel):
    _collection = "Credentials"

    def view(self, credential_id=None, user_reference=None, user_id=None):
        coll = fr.collection(self._collection)

        if credential_id is None:
            if user_id is not None:
                coll = coll.where('user_id', '==', user_id)

            if user_reference is not None:
                coll = coll.where('user', '==', user_reference)

            return coll.limit(100).get()
        else:
            coll = coll.document(credential_id)
            return coll.get()

    def create(self, token_acceso, user_id, user_reference):
        coll = fr.collection(self._collection)
        data = {
            'token_acceso': token_acceso,
            'user_id': user_id,
            'user': user_reference
        }

        date, reference = coll.add(data)
        return reference
