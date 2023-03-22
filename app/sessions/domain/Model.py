from datetime import datetime
from typing import Optional

from app.common.domain.ParentModel import ParentModel


class Session(ParentModel):
    _id: Optional[str]
    _token: Optional[str]
    _user: Optional[str]
    _credential: Optional[str]
    _life_time: Optional[int]
    _creation_date: Optional[datetime]
    _last_activity: Optional[datetime]

    def __int__(self, session_id=None, session_token=None, session_user=None, session_credential=None,
                session_life_time=None, session_creation_date=None, session_last_activity=None):
        self.id = session_id
        self.token = session_token
        self.user = session_user
        self.credential = session_credential
        self.life_time = session_life_time
        self.creation_date = session_creation_date
        self.last_activity = session_last_activity

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, session_id):
        self._id = session_id

    @property
    def token(self):
        return self._token

    @token.setter
    def token(self, session_token):
        self._token = session_token

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, session_user):
        self._user = session_user

    @property
    def credential(self):
        return self._credential

    @credential.setter
    def credential(self, session_credential):
        self._credential = session_credential

    @property
    def life_time(self):
        return self._life_time

    @life_time.setter
    def life_time(self, session_life_time):
        self._life_time = int(session_life_time)

    @property
    def creation_date(self):
        return self._creation_date

    @creation_date.setter
    def creation_date(self, session_creation_date):
        self._creation_date = session_creation_date

    @property
    def last_activity(self):
        return self._last_activity

    @last_activity.setter
    def last_activity(self, session_last_activity):
        self._last_activity = session_last_activity
