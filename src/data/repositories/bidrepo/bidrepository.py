from bson import ObjectId
from pymongo import MongoClient

from src.data.models.bid import Bid
from src.data.repositories.bidrepo.bidinterface import BidInterface
from src.data.repositories.productrepo.productrepository import ProductRepository


class BidRepository(BidInterface):
    def __init__(self, product_repo: ProductRepository):
        self.product_repo = product_repo
        self.client = MongoClient('mongodb://localhost:27017/')
        self.database = self.client['Auction_Application']
        self.collection = self.database['bids']

    def save_bid(self, bid: Bid):
        bid_data = {
            "product_id": bid.product_id,
            "amount": bid.amount,
            "bidder_id": bid.bidder_id,
            "bid_time": bid.bid_time
        }
        result = self.collection.insert_one(bid_data)
        return str(result.inserted_id)

    def get_product(self, product_id: ObjectId):
        return self.product_repo.find_product(product_id)
