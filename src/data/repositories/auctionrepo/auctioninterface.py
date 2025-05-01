from abc import ABC, abstractmethod

from src.data.models.auction import Auction


class AuctionInterface(ABC):

    @abstractmethod
    def create_auction(self, auction: Auction):
        pass

