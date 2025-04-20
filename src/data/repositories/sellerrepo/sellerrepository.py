from abc import ABC

from pymongo import MongoClient

from src.data.models.seller import Seller
from src.data.repositories.sellerrepo.sellerinterface import SellerInterface


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