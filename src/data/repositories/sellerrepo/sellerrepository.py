from abc import ABC

from pymongo import MongoClient

from src.data.models.seller import Seller
from src.data.repositories.sellerrepo.sellerinterface import SellerInterface
from src.exceptions.allexceptions import InvalidDetailsException, NotFoundException


class SellerRepository(SellerInterface):

    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.database = self.client['Auction_Application']
        self.collection = self.database['sellers']

    def save_seller(self, seller: Seller):
        seller_data = {
            "first_name": seller.first_name,
            "last_name": seller.last_name,
            "email": seller.email,
            "password": seller.password,
            "account_number": seller.account_number,
            "bank_name": seller.bank_name
        }
        insert_document = self.collection.insert_one(seller_data)
        seller.seller_id = str(insert_document.inserted_id)
        return seller

    def email_exists(self, email: str) -> bool:
        return self.collection.find_one({"email": email}) is not None

    def exists_by_id(self, seller_id: str) -> bool:
        from bson import ObjectId
        try:
            _id = ObjectId(seller_id)
        except InvalidDetailsException:
            return False
        return self.collection.find_one({"_id": _id}) is not None

    def find_by_email(self, email: str) -> Seller:
        data = self.collection.find_one({'email': email})
        if not data:
            raise NotFoundException("Not found.")
        return Seller(**data)