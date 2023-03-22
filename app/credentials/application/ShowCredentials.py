from app.credentials.domain.CredentialApplicationModel import CredentialApplicationModel
from app.credentials.domain.Model import Credential
from app.credentials.interface.FirestoreRepository import CredentialRepository


class ShowCredentials(CredentialApplicationModel):
    def by_params(self, username, credential_type):
        self.credential = Credential()
        self.credential.username = username
        self.credential.type = credential_type

        repo = CredentialRepository()
        result = repo.view(username=self.credential.username, credential_type=self.credential.type)

        return result

