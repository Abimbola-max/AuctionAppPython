from abc import ABC, abstractmethod

from src.data.models.bid import Bid


class BidInterface(ABC):

    @abstractmethod
    def save_bid(self, bid: Bid):
        pass

    @abstractmethod
    def get_product(self, product_id: str):
        pass