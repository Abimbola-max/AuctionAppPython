from src.data.models.seller import Seller
from src.data.repositories.sellerrepo.sellerrepository import SellerRepository
from src.dtos.sellerdto.sellerrequest import SellerRequestDTO
from src.dtos.sellerdto.sellerresponse import SellerResponseDTO
from src.exceptions.allexceptions import EmailAlreadyExistException


class SellerService:

    def __init__(self, seller_repo: SellerRepository):
        self.seller_repo = seller_repo

    # def get_seller_by_id(self, seller_id):
    #     return self.seller_repo.f

    def register_seller(self, seller_data_request):
        if self.seller_repo.email_exists(seller_data_request['email']):
            raise EmailAlreadyExistException("A user with this email already exists.")
        seller = Seller(
            first_name=seller_data_request["first_name"],
            last_name=seller_data_request["last_name"],
            email=seller_data_request["email"],
            password=seller_data_request["password"],
            account_number=seller_data_request["account_number"],
            bank_name=seller_data_request["bank_name"]
        )
        saved_seller = self.seller_repo.save_seller(seller)
        seller_response_dto = SellerResponseDTO()
        response_data = {"message": "You have successfully registered.", "seller_id": str(saved_seller.seller_id)}
        return seller_response_dto.dump(response_data)