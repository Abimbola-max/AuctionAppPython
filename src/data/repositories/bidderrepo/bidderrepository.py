from pymongo import MongoClient

from src.data.models.bidder import Bidder
from src.data.models.creditcardinformation import CreditCardInformation
from src.data.repositories.bidderrepo.bidderinterface import BidderInterface
from src.exceptions.allexceptions import *


class BidderRepository(BidderInterface):

    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.database = self.client['Auction_Application']
        self.collection = self.database['bidder']

    def save_bidder(self, bidder: Bidder):

        bidder_data = {
            "first_name": bidder.first_name,
            "last_name": bidder.last_name,
            "email": bidder.email,
            "password": bidder.password,
            "credit_card_information": BidderRepository.__credit_card_entry(bidder.credit_card_information)
        }
        insert_document = self.collection.insert_one(bidder_data)
        bidder.bidder_data = str(insert_document.inserted_id)
        return bidder

    @staticmethod
    def __credit_card_entry(card_info: CreditCardInformation):
        return {
            "card_cvv": card_info.card_cvv,
            "card_number": card_info.card_number,
            "expiry_date": card_info.expiry_date,
            "card_type": card_info.card_type.value
        }

    def email_exists(self, email: str) -> bool:
        return self.collection.find_one({"email": email}) is not None

    def exists_by_id(self, bidder_id: str) -> bool:
        from bson import ObjectId
        try:
            _id = ObjectId(bidder_id)
        except InvalidDetailsException:
            return False
        return self.collection.find_one({"_id": _id}) is not None

    def find_by_email(self, email: str) -> Bidder:
        data = self.collection.find_one({'email': email})
        if not data:
            raise NotFoundException("Not found.")
        return Bidder(**data)

    def update_bid(self, product_id: str, bid_price: int):
        product = self.collection.find_one({'_id': product_id})
        if not product:
            raise NotFoundException("Product Not found.")
        if bid_price <= product['current_price']:
            raise InvalidAmountException('Bid must be higher than the current price')
        self.collection.update_one({'_id': product_id}, {'$set': {'current_price': bid_price}})

    def get_current_price(self, product_id):
        product = self.collection.find_one({'_id': product_id})
        if not product:
            raise NotFoundException("Product Not found.")
        return product['current_price']