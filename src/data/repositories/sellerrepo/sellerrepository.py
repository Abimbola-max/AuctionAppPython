from abc import ABC

from pymongo import MongoClient

from src.data.models.seller import Seller
from src.data.repositories.sellerrepo.sellerinterface import SellerInterface


class SellerRepository(SellerInterface, ABC):

    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.database = self.client['Auction_Application']
        self.collection = self.database['sellers']

    def save_seller(self, seller: Seller):
        seller_data = {

        }