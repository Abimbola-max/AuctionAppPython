import os

from pymongo import MongoClient

from src.data.models.auction import Auction
from src.data.repositories.auctionrepo.auctioninterface import AuctionInterface


class AuctionRepository(AuctionInterface):

    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['Auction_Application']
        self.collection = self.db['auctions']

    def create_auction(self, auction: Auction):
        auction_data = {
            "product_id": auction.product_id,
            "start_time": auction.start_time,
            "end_time": auction.end_time,
            "highest_bidder": auction.highest_bidder,
            "final_price": auction.final_price
            # "product_phase": auction
        }
        self.collection.insert_one(auction_data)
