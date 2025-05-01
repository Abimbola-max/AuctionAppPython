from datetime import datetime
from typing import Optional

from marshmallow import ValidationError

from src.data.models.UserType import UserType
from src.data.models.admin import Admin
from src.data.models.auction import Auction
from src.data.models.productphase import ProductPhase
from src.data.repositories.adminrepo.adminrepository import AdminRepository
from src.data.repositories.auctionrepo.auctionrepository import AuctionRepository
from src.data.repositories.bidderrepo.bidderrepository import BidderRepository
from src.data.repositories.productrepo.productrepository import ProductRepository
from src.exceptions.allexceptions import NotFoundException, ProductNotApprovedException
from src.services.passwordsecurity.passwordencrypt import PasswordEncrypt


class AdminService:

    def __init__(self, admin_repo: AdminRepository, product_repo: ProductRepository, bidder_repo: BidderRepository, auction_repo: AuctionRepository):
        self.admin_repo = admin_repo
        self.bidder_repo = bidder_repo
        self.product_repo = product_repo
        self.auction_repo = auction_repo

    def login_admin(self, data: dict) -> Optional[Admin]:
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            raise ValidationError("Email and password are required.")

        admin_doc = self.admin_repo.find_one(email)
        if not admin_doc:
            raise ValidationError("Admin not found.")

        if not PasswordEncrypt.verify_password(password, admin_doc['password']):
            raise ValidationError("Invalid password.")

        return Admin(
            first_name=admin_doc['first_name'],
            last_name=admin_doc['last_name'],
            email=admin_doc['email'],
            password=admin_doc['password'],
            _id=str(admin_doc['_id'])
        )

    def start_auction(self):
        self.product_repo.start_all_auctions()
        ongoing_products = self.product_repo.get_ongoing_products()
        for product in ongoing_products:
            self.auction_repo.create_auction(
                Auction(
                    product_id=product.product_id,
                    start_time=datetime.utcnow(),
                    end_time=None,
                    highest_bidder=None,
                    final_price=product.bid_minimum_price
                )
            )

    def accept_product(self, product_id):
        if not self.product_repo.update_product_status(product_id, ProductPhase.APPROVED):
            raise ProductNotApprovedException('product is yet to be approved')

    def reject_product(self, product_id: str) -> None:
        if not self.product_repo.update_product_status(product_id, ProductPhase.REJECTED):
            raise ValueError("Product not found")