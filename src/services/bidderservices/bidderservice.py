from datetime import timedelta

from bson import ObjectId
from flask_jwt_extended import create_access_token

from src.data.models.bid import Bid
from src.data.models.bidder import Bidder
from src.data.models.cardtype import CardType
from src.data.models.creditcardinformation import CreditCardInformation
from src.data.models.productphase import ProductPhase
from src.data.repositories.bidderrepo.bidderrepository import BidderRepository
from src.data.repositories.bidrepo.bidrepository import BidRepository
from src.data.repositories.productrepo.productrepository import ProductRepository
from src.dtos.bidderdto.bidderresponse import BidderResponseDTO
from src.exceptions.allexceptions import *
from src.services.passwordsecurity.passwordencrypt import PasswordEncrypt


class BidderService:

    def __init__(self, bidder_repo: BidderRepository, bid_repo: BidRepository, product_repo: ProductRepository):
        self.bidder_repo = bidder_repo
        self.bid_repo = bid_repo
        self.product_repo = product_repo

    def register(self, bidder_data_request):
        if self.bidder_repo.email_exists(bidder_data_request["email"]):
            raise EmailAlreadyExistException("A User with this email already exists.")

        hashed_password = PasswordEncrypt.encrypt_password(bidder_data_request["password"])

        credit_card_data = bidder_data_request["credit_card_information"]
        credit_card_info = CreditCardInformation(
            card_cvv=credit_card_data["card_cvv"],
            card_number=credit_card_data["card_number"],
            expiry_date=credit_card_data["expiry_date"],
            card_type=CardType(credit_card_data["card_type"])
        )
        bidder = Bidder (
            first_name=bidder_data_request["first_name"],
            last_name=bidder_data_request["last_name"],
            email=bidder_data_request["email"],
            password=hashed_password,
            credit_card_information=credit_card_info
        )
        saved_bidder = self.bidder_repo.save_bidder(bidder)
        access_token = create_access_token(
            identity= str(saved_bidder.bidder_id),
            expires_delta=timedelta(minutes=45)
        )
        bidder_response_dto = BidderResponseDTO()
        response_data = {"message": "You have successfully registered.", "token": access_token}
        return bidder_response_dto.dump(response_data)

    def login_bidder(self, bidder_login_request):

        email = bidder_login_request['email']
        password = bidder_login_request['password'].strip()

        bidder = self.bidder_repo.find_by_email(email)
        if not bidder:
            raise NotFoundException("Bidder not found.")

        hashed_password = bidder.password

        access_token = create_access_token(
            identity=str(bidder.bidder_id),
            expires_delta=timedelta(minutes=45)
        )

        if not PasswordEncrypt.verify_password(password, hashed_password):
            raise InvalidDetailsException("Invalid details.")
        return {
            "message": "login successful.",
            "first_name": f"Welcome {bidder.first_name} {bidder.last_name}",
            "bidder_id": str(bidder.bidder_id),
            "token": access_token
        }

    def place_bid(self, product_id, amount: int, bidder_id):
        self.__validation_of_bid(product_id, amount)
        bid = Bid(
            product_id=product_id,
            amount=amount,
            bidder_id= bidder_id
        )
        bid_id = self.bid_repo.save_bid(bid)
        self.product_repo.update_product_price(product_id=ObjectId(product_id), current_price=amount)
        return {
            "product_id": product_id,
            "amount": amount,
            "bid_id": bid_id,
            # "bidder_id": bidder_id,
            "bid_time": bid.bid_time
        }

    def __validation_of_bid(self, product_id, amount):
        product = self.bid_repo.get_product(ObjectId(product_id))
        print(f"product {product}")

        if not product:
            raise NotFoundException("Product not found")

        if 'bid_minimum_price' not in product:
            raise InvalidAmountException("Product has no minimum price set")

        if amount <= product['bid_minimum_price']:
            raise InvalidAmountException(
                f"Bid amount must be greater {product['bid_minimum_price']}"
            )

    # def update_bid(self, product_id, bid_price):
    #     product = self.bid_repo.get_product(ObjectId(product_id))
    #     if product is None or product.product_phase != ProductPhase.ONGOING:
    #         raise NotFoundException("Product not found or not yet auctioned")
    #     if bid_price <= product.
    #     # self.bidder_repo.update_bid(product_id, bid_price)

    def get_current_price(self, product_id):
        return self.bidder_repo.get_current_price(product_id)