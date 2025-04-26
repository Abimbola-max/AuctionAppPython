from src.data.models.UserType import UserType
from src.data.models.user import User


class Admin(User):

    def __init__(self, first_name: str, last_name: str, email: str, password: str, user_type: UserType= UserType.ADMIN, _id=None):
        super().__init__(first_name, last_name, email, password, UserType.ADMIN)

