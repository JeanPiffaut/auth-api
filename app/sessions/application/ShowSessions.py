from app.credentials.domain.Model import Credential
from app.credentials.interface.FirestoreRepository import CredentialRepository
from app.sessions.domain.SessionApplicationModel import SessionApplicationModel


class ShowSessions(SessionApplicationModel):
    def by_params(self, username, credential_type):
        self.credential = Credential()
        self.credential.username = username
        self.credential.type = credential_type

        repo = CredentialRepository()
        result = repo.view(username=self.credential.username, credential_type=self.credential.type)

        credentials = []
        if len(result) != 0:
            for doc in result:
                if doc.exists:
                    credentials.append(doc.to_dict())

        return credentials
