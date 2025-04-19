from abc import ABC, abstractmethod

from src.data.models.seller import Seller


class SellerInterface(ABC):

    @abstractmethod
    def save_seller(self, seller: Seller):
        pass