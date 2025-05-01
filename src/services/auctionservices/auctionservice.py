from datetime import datetime

from bson import ObjectId

from src.data.models.productphase import ProductPhase
from src.data.repositories.auctionrepo.auctionrepository import AuctionRepository


class AuctionService:
    def __init__(self, auction_repo: AuctionRepository):
        self.auction_repo = auction_repo

