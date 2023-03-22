import os

from app.credentials.domain.CredentialApplicationModel import CredentialApplicationModel
from app.credentials.domain.Model import Credential
from app.credentials.interface.FirestoreRepository import CredentialRepository


class CreateCredential(CredentialApplicationModel):

    def by_google(self, token, email, user_reference):
        self.credential = Credential()
        self.credential.user = user_reference
        self.credential.token = token
        self.credential.username = email
        self.credential.type = os.getenv('GOOGLE_CREDENTIAL_TYPE')

        repo = CredentialRepository()
        result = repo.create(token_access=self.credential.token, username=self.credential.username,
                             user_reference=self.credential.user, credential_type=self.credential.type)

        return result

    def by_params(self):
        pass
