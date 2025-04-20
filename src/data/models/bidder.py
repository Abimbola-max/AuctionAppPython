from src.data.models.UserType import UserType
from src.data.models.creditcardinformation import CreditCardInformation
from src.data.models.user import User

class Bidder(User):

    def __init__(self, first_name: str, last_name: str, email: str, password: str, credit_card_information: CreditCardInformation, _id=None):
        super().__init__(first_name, last_name, email, password, UserType.BIDDER)
        self.bidder_id = _id
        self.credit_card_information = credit_card_information

    @property
    def bidder_id(self):
        return self.__id

    @bidder_id.setter
    def bidder_id(self, value):
        self.__id = value

    @property
    def credit_card_information(self):
        return self.__credit_card_information

    @credit_card_information.setter
    def credit_card_information(self, value):
        self.__credit_card_information = value
