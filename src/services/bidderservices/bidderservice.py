from src.data.models.bidder import Bidder
from src.data.models.cardtype import CardType
from src.data.models.creditcardinformation import CreditCardInformation
from src.data.repositories.bidderrepo.bidderrepository import BidderRepository
from src.dtos.bidderdto.bidderRequest import BidderRequestDTO
from src.dtos.bidderdto.bidderresponse import BidderResponseDTO
from src.dtos.sellerdto.sellerresponse import SellerResponseDTO
from src.exceptions.allexceptions import EmailAlreadyExistException
from src.services.passwordsecurity.passwordencrypt import PasswordEncrypt


class BidderService:

    def __init__(self, bidder_repo: BidderRepository):
        self.bidder_repo = bidder_repo

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
        bidder_response_dto = BidderResponseDTO()
        response_data = {"message": "You have successfully registered.", "bidder_id": str(saved_bidder.bidder_id)}
        return bidder_response_dto.dump(response_data)

