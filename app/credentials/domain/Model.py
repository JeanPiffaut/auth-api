from typing import Optional

from app.common.domain.ParentModel import ParentModel


class Credential(ParentModel):
    _id: Optional[str]
    _username: Optional[str]
    _token: Optional[str]
    _user: Optional[str]
    _type: Optional[str]

    def __int__(self, credential_id=None, credential_username=None, credential_token=None, credential_user=None,
                credential_type=None):
        self.id = credential_id
        self.username = credential_username
        self.token = credential_token
        self.user = credential_user
        self.type = credential_type

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, credential_id):
        self._id = credential_id

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, credential_username):
        self._username = credential_username

    @property
    def token(self):
        return self._token

    @token.setter
    def token(self, credential_token):
        self._token = credential_token

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, credential_user):
        self._user = credential_user

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, credential_type):
        self._type = credential_type
