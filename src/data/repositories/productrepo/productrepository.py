from abc import ABC

from bson import ObjectId
from pymongo import MongoClient

from src.data.models.product import Product
from src.data.models.productphase import ProductPhase
from src.data.repositories.productrepo.productinterface import ProductInterface


class ProductRepository(ProductInterface):

    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.database = self.client['Auction_Application']
        self.collection = self.database['products']

    def create_product(self, product: Product) -> Product:
        product_data = {
            "name": product.name,
            "description": product.description,
            "seller_id": product.seller_id,
            "bid_minimum_price": product.bid_minimum_price,
            "image_url": product.image_url,
            # "bid_start_time": product.bid_start_time,
            # "bid_end_time": product.bid_end_time,
            "added_at": product.added_at,
            "product_phase": product.product_phase.value,
            "current_price": product.current_price
        }
        insert_document = self.collection.insert_one(product_data)
        product.product_id = str(insert_document.inserted_id)
        return product

    def find_product(self, product_id: ObjectId) -> Product:
        return self.collection.find_one({"_id": product_id})

    def update_product(self, product_id, product):
        return self.collection.update_one({"_id": product_id}, {"$set": product})

    def update_product_status(self, product_id: str, phase: ProductPhase):
        update = self.collection.update_one({'_id': product_id}, {'$set': {'phase': phase}})
        return update.modified_count > 0

    def start_all_auctions(self):
        products = self.collection.update_many({"product_phase": "APPROVED"}, {"$set": {"product_phase": "ONGOING"}})
        return products.modified_count

    def end_auction(self):
        products = self.collection.update_many({"product_phase": "ONGOING"}, {"$set": {"product_phase": "ENDED"}})
        return products.modified_count

    def get_ongoing_products(self):
        return list(self.collection.find({"product_phase": "ONGOING"}))

    def update_product_price(self, product_id, current_price):
        self.collection.update_one(
            {"_id": product_id},
            {"$set": {"current_price": current_price}}
        )



