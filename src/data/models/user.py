from abc import ABC

from src.data.models.UserType import UserType
from src.services.passwordsecurity.passwordencrypt import PasswordEncrypt


class User(ABC):

    def __init__(self, first_name: str, last_name: str, email: str, password: str, user_type: UserType, _id=None):
        self._id = _id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.user_type = user_type

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name):
        self.__first_name = first_name

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name):
        self.__last_name = last_name

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = PasswordEncrypt.encrypt_password(password)

    @property
    def user_type(self):
        return self.__user_type

    @user_type.setter
    def user_type(self, user_type):
        self.__user_type = user_type

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value


