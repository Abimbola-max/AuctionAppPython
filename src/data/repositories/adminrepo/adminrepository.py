import os
from typing import Optional

from marshmallow import ValidationError
from pymongo import MongoClient

from src.data.models.UserType import UserType
from src.data.models.admin import Admin
from src.data.repositories.adminrepo.admininterface import AdminInterface
from src.services.passwordsecurity.passwordencrypt import PasswordEncrypt


class AdminRepository(AdminInterface):

    def __init__(self):
        self.client = MongoClient(os.getenv('MONGODB_URI', 'mongodb://localhost:27017/'))
        self.database = self.client['Auction_Application']
        self.collection = self.database['admins']
        self.create_default_admin()

    def create_default_admin(self):
        first_name = os.getenv('ADMIN_FIRST_NAME', 'Bolaji')
        last_name = os.getenv('ADMIN_LAST_NAME', 'Gafar')
        email = os.getenv('ADMIN_EMAIL', 'abolajig@gmail.com')
        password = os.getenv('ADMIN_PASSWORD', 'password')

        hashed_password = PasswordEncrypt.encrypt_password(password)

        admin = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            "password": hashed_password,
            "user_type": UserType.ADMIN.value,
        }
        self.collection.insert_one(admin)

    def find_one(self, email):
        return self.collection.find_one({'email': email})


