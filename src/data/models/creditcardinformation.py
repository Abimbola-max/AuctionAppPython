from src.data.models.cardtype import CardType


class CreditCardInformation:

    def __init__(self, card_cvv: str, card_number: str, expiry_date, card_type: CardType):
        self.card_cvv = card_cvv
        self.card_number = card_number
        self.expiry_date = expiry_date
        self.card_type = card_type

    @property
    def card_cvv(self):
        return self.__card_cvv

    @card_cvv.setter
    def card_cvv(self, value):
        self.__card_cvv = value

    @property
    def card_number(self):
        return self.__card_number

    @card_number.setter
    def card_number(self, value):
        self.__card_number = value

    @property
    def expiry_date(self):
        return self.__expiry_date

    @expiry_date.setter
    def expiry_date(self, value):
        self.__expiry_date = value

    @property
    def card_type(self):
        return self.__card_type

    @card_type.setter
    def card_type(self, value):
        self.__card_type = value