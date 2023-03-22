import os
from datetime import datetime, timedelta

import pytz
from google.auth import jwt

from app.sessions.domain.Model import Session
from app.sessions.domain.SessionApplicationModel import SessionApplicationModel
from app.sessions.interface.FirestoreRepository import SessionRepository


class CreateSession(SessionApplicationModel):
    def by_params(self, user_reference, credential_reference):
        self.session = Session()
        self.session.user = user_reference
        self.session.credential = credential_reference
        self.session.life_time = os.getenv('TOKEN_LIFE_TIME')

        time_zone = pytz.timezone(os.getenv('TIMEZONE'))
        now = datetime.now(time_zone)

        self.session.creation_date = now
        self.session.last_activity = now

        expiration = now + timedelta(seconds=self.session.life_time)
        payload = {
            'sub': self.session.user.id,
            'exp': expiration
        }

        header = {
            'alg': 'RS256',
            'typ': 'JWT'
        }

        self.session.token = jwt.encode(os.getenv('SECRET_KEY'), payload, header, os.getenv('SECRET_KEY'))
        print(self.session.token)
        print(jwt.decode(self.session.token, os.getenv('secret_key')))

        repo = SessionRepository()
        result = repo.create(self.session.user, self.session.credential, self.session.token, self.session.creation_date,
                             self.session.last_activity, self.session.life_time)

        return self.session.token



