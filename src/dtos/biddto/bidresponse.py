from flask_jwt_extended import jwt_required

from src.data.repositories.bidrepo.bidrepository import BidRepository


class BidService:

    def __init__(self, bid_repo: BidRepository):
        self.bid_repo = bid_repo
