from abc import ABC, abstractmethod

from src.data.models.seller import Seller


class SellerInterface(ABC):

    @abstractmethod
    def save_seller(self, seller: Seller):
        pass

    @abstractmethod
    def email_exists(self, email: str) -> bool:
        pass

    @abstractmethod
    def exists_by_id(self, seller_id: str) -> bool:
        pass