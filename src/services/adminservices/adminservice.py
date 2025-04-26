from typing import Optional

from marshmallow import ValidationError

from src.data.models.UserType import UserType
from src.data.models.admin import Admin
from src.data.repositories.adminrepo.adminrepository import AdminRepository
from src.services.passwordsecurity.passwordencrypt import PasswordEncrypt


class AdminService:

    def __init__(self, admin_repo: AdminRepository):
        self.admin_repo = admin_repo

    def login_admin(self, data: dict) -> Optional[Admin]:
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            raise ValidationError("Email and password are required.")

        admin_doc = self.admin_repo.find_one(email)
        if not admin_doc:
            raise ValidationError("Admin not found.")

        if not PasswordEncrypt.verify_password(password, admin_doc['password']):
            raise ValidationError("Invalid password.")

        return Admin(
            first_name=admin_doc['first_name'],
            last_name=admin_doc['last_name'],
            email=admin_doc['email'],
            password=admin_doc['password'],
            _id=str(admin_doc['_id'])
        )