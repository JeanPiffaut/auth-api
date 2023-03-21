from typing import Optional

from app.common.domain.ParentModel import ParentModel


class User(ParentModel):
    _id: Optional[str]
    _name: Optional[str]
    _email: Optional[str]
    _picture: Optional[str]

    def __int__(self, user_id=None, user_name=None, user_email=None, user_picture=None):
        self.id = user_id
        self.name = user_name
        self.email = user_email
        self.picture = user_picture

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, user_id):
        self._id = user_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, user_name):
        self._name = user_name

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, user_email):
        self._email = user_email

    @property
    def picture(self):
        return self._picture

    @picture.setter
    def picture(self, user_picture):
        self._picture = user_picture
