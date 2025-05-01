from abc import ABC, abstractmethod

from src.data.models.bidder import Bidder


class BidderInterface(ABC):

    @abstractmethod
    def save_bidder(self, bidder: Bidder):
        pass

    @abstractmethod
    def email_exists(self, email: str) -> bool:
        pass

    @abstractmethod
    def exists_by_id(self, bidder_id: str) -> bool:
        pass

    @abstractmethod
    def find_by_email(self, email: str) -> Bidder:
        pass

    @abstractmethod
    def update_bid(self, product_id: str, bid_price: int):
        pass

    @abstractmethod
    def get_current_price(self, product_id):
        pass