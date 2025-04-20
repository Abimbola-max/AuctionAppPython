from src.data.models.UserType import UserType
from src.data.models.user import User


class Seller(User):

    def __init__(self, first_name: str, last_name: str, email: str, password: str, account_number: str, bank_name: str, _id= None):
        super().__init__(first_name, last_name, email, password, UserType.SELLER)
        self.seller_id = _id
        self.account_number = account_number
        self.bank_name = bank_name

    @property
    def seller_id(self):
        return self.__id

    @seller_id.setter
    def seller_id(self, value):
        self.__id = value

    @property
    def account_number(self):
        return self.__account_number

    @account_number.setter
    def account_number(self, account_number):
        self.__account_number = account_number

    @property
    def bank_name(self):
        return self.__bank_name

    @bank_name.setter
    def bank_name(self, bank_name):
        self.__bank_name = bank_name

