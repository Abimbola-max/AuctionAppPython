from abc import ABC

from bson import ObjectId
from pymongo import MongoClient

from src.data.models.product import Product
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
        }
        insert_document = self.collection.insert_one(product_data)
        product.product_id = str(insert_document.inserted_id)
        return product

    def find_product(self, product_id: ObjectId) -> Product:
        return self.collection.find_one({"_id": product_id})


