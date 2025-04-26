from abc import ABC, abstractmethod


class BidInterface(ABC):

    @abstractmethod
    def save_bid(self, bid: Bid):
        pass

    @abstractmethod
    def get_product(self, product_id: str):
        pass